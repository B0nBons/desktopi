# NOTE TO SELF ADD A MUSIC PLAYER LINK THING THAT WOULD BE SO COOL!!

from PyQt6.QtCore import QTimer, QObject, pyqtSignal

# I am so unsure on how classes work. It has been like two years
# REVIEW THIS NO WAY ITS RIGHT
# Actually, I have no clue how to run this considering this is github codespaces. uh oh.

class PomodoroTimer(QObject):
    tick = pyqtSignal(int)
    # Show time left
    status = pyqtSignal(str)
    # (Work vs break vs paused)
    # Define variables first

    def __init__(self, work_mins = 25, break_mins = 5):
        # We set default pomodoro time values bc maybe some ppl use default
        super().__init__()
        self.work_seconds = work_mins * 60
        self.break_seconds = break_mins * 60
        self.time_left = self.work_seconds
        self.is_work_time = True
        self.is_on = False
        # Set default values to be referenced later

        self._timer = QTimer()
        self._timer.setInterval(1000) # 1k ms = 1s
        self._timer.timeout.connect(self._on_tick)
        # PRIVATE VARIABLES - leave them alone
    
    # OK im done were actually just gonna define all methods i think we need 

    def start(self):
        if not self.is_on:
            self.is_on = True
            self._timer.start()
            if self.is_work_time:
                current_mode = "work"
            else:
                current_mode = "break"
            self.status.emit(f"now in {current_mode}!")

    def pause(self):
        if self.is_on:
            self.is_on = False
            self._timer.stop()
            self.status.emit("paused")

    def reset(self):
        self.pause()
        self.is_work_time = True
        self.time_left = self.work_seconds
        self.tick.emit(self.time_left)
        self.status.emit("ready to start!")

    def _on_tick(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.tick.emit(self.time_left)
        else:
            self._switch_timer_status()

    def _switch_timer_status(self):
        self.is_work_time = not self.is_work_time

        # Change countdown based on current time status
        if self.is_work_time:
            self.time_left = self.work_seconds
        else:
            self.time_left = self.break_seconds

        if self.is_work_time:
            current_mode = "work"
        else:
            current_mode = "break"

        self.status.emit(f"now in {current_mode}!")
        self.tick.emit(self.time_left)

# OK Lets try this out.........