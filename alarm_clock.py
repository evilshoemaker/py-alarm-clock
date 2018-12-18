from PyQt5.QtCore import (
    pyqtSignal,
    QObject,
    QTime
)

class AlarmClock(QObject):
    alarm = pyqtSignal()

    def __init__(self, title, time, alarm_sound, parent=None):
        super(AlarmClock, self).__init__(parent)

        self.title = title
        self.time = time
        self.alarm_sound = alarm_sound
        self.is_active = True
        self.is_alarm = False

    def tick(self):
        if (not self.is_active) and self.is_alarm:
            return
        
        current_time = QTime.currentTime()
        sec_to = current_time.secsTo(self.time)
        if (sec_to == 0):
            self.is_alarm = True
            self.alarm.emit()
