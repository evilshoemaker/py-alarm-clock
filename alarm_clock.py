from PyQt5.QtCore import (
    QObject
)

class AlarmClock(QObject):
    def __init__(self, title, time, parent=None):
        super(AlarmClock, self).__init__(parent)

        self.title = title
        self.time = time
        self.is_active = False

    def tick(self):
        pass
