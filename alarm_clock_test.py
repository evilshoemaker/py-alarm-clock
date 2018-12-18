import sys

from PyQt5 import (
    uic, 
    QtCore
)

from PyQt5.QtCore import (
    QTimer, 
    QTime,
    QUrl
)

from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QMainWindow, 
    QLCDNumber,
    QMessageBox, 
    QTimeEdit, 
    QHBoxLayout,
    QDialog,
    QListWidgetItem
)

from PyQt5.QtMultimedia import (
    QMediaPlayer,
    QMediaContent
)

from digital_clock import DigitalClock
from new_alarm_clock_dialog import NewAlarmClockDialog
from alarm_clock_item_widget import AlarmClockItemWidget
from alarm_clock_item import AlarmClockItem

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('ui/alarm_clock_form.ui', self)
        self.initUI()

        self.alarm_clock_list = []
        self.player = QMediaPlayer()

    def initUI(self):
        self.digital_clock = DigitalClock(self.clockWidget)
        self.digital_clock.time_tick.connect(self.time_tick)

        clock_widget_layout = QHBoxLayout()
        clock_widget_layout.addWidget(self.digital_clock)
        self.clockWidget.setLayout(clock_widget_layout)

        self.addAlarmClockButton.clicked.connect(self.add_alarm_clock)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выход',
                                     "Вы уверены что хотите выйти? Будильники перестанут работать", 
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def add_alarm_clock(self):
        dialog = NewAlarmClockDialog()
        dialog_result = dialog.exec_()

        if (dialog_result == QDialog.Accepted):
            widget_item = QListWidgetItem(self.listWidget);

            alarm_clock_item = AlarmClockItem(dialog.nameLineEdit.text(), 
                                            dialog.timeEdit.time(),
                                            dialog.filePathLineEdit.text())
            alarm_clock_item.alarm.connect(self.alarm)
            self.alarm_clock_list.append(alarm_clock_item)

            alarm_clock_item_widget = AlarmClockItemWidget(alarm_clock_item, widget_item, self)
            alarm_clock_item_widget.alarm_clock_remove.connect(self.alarm_clock_remove)
            
            widget_item.setSizeHint(alarm_clock_item_widget.sizeHint());
            self.listWidget.setItemWidget(widget_item, alarm_clock_item_widget);
        
        dialog.deleteLater()

    def alarm_clock_remove(self):
        self.listWidget.takeItem(self.listWidget.row(self.sender().list_widget_item))
        self.alarm_clock_list.remove(self.sender().alarm_clock)

    def time_tick(self):
        for alarm_clock in self.alarm_clock_list:
            if alarm_clock.is_active:
                alarm_clock.tick()

    def alarm(self):
        alarm_clock = self.sender()

        self.play_sound(alarm_clock.alarm_sound)

        QMessageBox.information(self, 'Будильник',
                                     'Будильник "' + alarm_clock.title + '"', 
                                     QMessageBox.Ok)
        alarm_clock.is_alarm = False

    def play_sound(self, sound):
        if len(sound):
            media_content = QMediaContent(QUrl.fromLocalFile(sound))
            self.player.setMedia(media_content);
            self.player.play()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
