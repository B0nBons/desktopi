import threading
import yt_dlp
from src.ui.widgets.timer_widget import TimerWidget
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl, pyqtSignal, QObject

class AudioRunner(QObject):
    finished = pyqtSignal(str)
    
    def __init__(self, url):
        super().__init__()
        self.url = url
    
    def run(self):
        try:
            ydlparams = {
                'format' : "bestaudio/best",
                "quiet" : True,
                "no_warnings" : True
            }
            with yt_dlp.YoutubeDL(ydlparams) as ydl:
                items = ydl.extract_info(self.url, download = False)
                if 'entries' in items:
                    items = items['entries'][0]
                audio_link = items.get('url')
                if audio_link:
                    self.finished.emit(audio_link)
        except Exception as error:
            print(f"couldnt grab music :( {error}")
            self.finished.emit("")
            
class HomePage(QWidget):
    def __init__(self, timer, parent=None):
        super().__init__(parent)
        self.timer = timer
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(0.8)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()
        self.timer_widget = TimerWidget(self.timer)
        layout.addWidget(self.timer_widget)
        layout.addSpacing(23) # birthday num
        
        music_layout = QHBoxLayout()
        self.music_inp = QLineEdit()
        self.music_inp.setPlaceholderText("YOUTUBE video link here!")
        
        self.play_butt = QPushButton("Play")
        self.pause_butt = QPushButton("Pause")
        
        self.play_butt.clicked.connect(self._fetchplay)
        self.pause_butt.clicked.connect(self._pause_music)
        
        music_layout.addWidget(self.music_inp)
        music_layout.addWidget(self.play_butt)
        music_layout.addWidget(self.pause_butt)
        
        layout.addLayout(music_layout)
        self.setLayout(layout)
        
    def _fetchplay(self):
        url = self.music_inp.text().strip()
        if url:
            self.play_butt.setText("on it!!")
            self.play_butt.setEnabled(False)
            self.runner = AudioRunner(url)
            self.runner.finished.connect(self._on_audio_ready)
            self.worker_thread = threading.Thread(target=self.runner.run)
            self.worker_thread.start()
            
    def _on_audio_ready(self, audio_url):
        if audio_url:
            self.player.setSource(QUrl.fromUserInput(audio_url))
            self.player.play()
        self.play_butt.setText("play!")
        self.pause_butt.setEnabled(True)
  
    def _pause_music(self):
        if self.player.isPlaying():
            self.player.pause()
        else:
            self.player.play()