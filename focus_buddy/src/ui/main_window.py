import webbrowser
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from src.core.timer import PomodoroTimer
from src.ui.widgets.timer_widget import TimerWidget
from src.ui.home_page import HomePage
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Focus Buddy!!!")
        self.resize(420,450)
        self.timer = PomodoroTimer()
        self.home_page = HomePage(self.timer)
        self.setCentralWidget(self.home_page)
        