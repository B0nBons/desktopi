from PyQt6.QtWidgets import QMainWindow
from src.core.timer import PomodoroTimer
from src.ui.widgets.timer_widget import TimerWidget
# Import libraries

WORK_MINS = 0.1
BREAK_MINS = 0.05 
# THESE ARE TESTING/PLACEHOLDER VALUES!!! PLS CHANGE

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro Time")
        self.resize(320, 220)

        self.timer = PomodoroTimer(WORK_MINS, BREAK_MINS)
        self.setCentralWidget(TimerWidget(self.timer))