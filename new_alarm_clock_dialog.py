from PyQt5 import (
    uic, 
    QtCore
)

from PyQt5.QtCore import QTime

from PyQt5.QtWidgets import (
    QApplication, 
    QDialog,
    QFileDialog
)

class NewAlarmClockDialog(QDialog):
    def __init__(self, parent=None):
        super(NewAlarmClockDialog, self).__init__(parent)

        uic.loadUi('ui/new_alarm_clock_dialog.ui', self)

        current_time = QTime.currentTime()
        self.timeEdit.setTime(QTime(current_time.hour(), current_time.minute())) #убираем секунды, они не нужны

        self.openFileButton.clicked.connect(self.open_sound_file)

    def open_sound_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Файлы звука (*.wav *.mp3)")[0]
        if len(fname):
            self.filePathLineEdit.setText(fname)
        