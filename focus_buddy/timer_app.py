import sys
from PyQt6.QtWidgets import QApplication
from src.core.timer import PomodoroTimer
from src.ui.widgets.timer_widget import TimerWidget

def run():
    app = QApplication(sys.argv)
    timer = PomodoroTimer(work_mins=25, break_mins=5)
    window = TimerWidget(timer)
    window.setWindowTitle("Pomodoro")
    window.resize(320,220)
    window.show()
    sys.exit(app.exec())
    
run()
# Might change this later, since this is mostly only to have a mvp going
