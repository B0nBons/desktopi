from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class TimerWidget(QWidget):
    def __init__(self, timer, parent = None):
        super().__init__(parent)
        self.timer = timer

        # start with buttons
        self.start_btn = QPushButton("start")
        self.pause_btn = QPushButton("pause")
        self.stop_btn = QPushButton("pause")

        # add in labels
        self.time_label = QLabel(self._format(timer.time_left))
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 64px; font-weight: bold;")

        self.status_label = QLabel("ready to start!!")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Form general layout

        buttons = QHBoxLayout()
        buttons.addWidget(self.start_btn)
        buttons.addWidget(self.pause_btn)
        buttons.addWidget(self.stop_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        layout.addWidget(self.status_label)
        layout.addLayout(buttons)
        self.setLayout(layout)

        # Ok now i need to think about what to add next bc this
        self.start_btn.clicked.connect(self.timer.start)
        self.pause_btn.clicked.connect(self.timer.pause)
        self.stop_btn.clicked.connect(self.timer.reset)

        self.timer.tick.connect(self._update_time)
        self.timer.status.connect(self.status_label.setText)

    def _update_time(self, seconds_left):
        self.time_label.setText(self._format(seconds_left))

    @staticmethod
    def _format(seconds)
        mins, secs = divmod (seconds, 60)
        return f"{mins:02d}:{secs:02d}"
