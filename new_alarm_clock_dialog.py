import sys
from PyQt5 import (
    uic, 
    QtCore
)

from PyQt5.QtCore import QTime

from PyQt5.QtWidgets import (
    QApplication, 
    QDialog 
)

class NewAlarmClockDialog(QDialog):
    def __init__(self, parent=None):
        super(NewAlarmClockDialog, self).__init__(parent)

        uic.loadUi('ui/new_alarm_clock_dialog.ui', self)

        self.timeEdit.setTime(QTime.currentTime())