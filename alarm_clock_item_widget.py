from PyQt5 import (
    uic, 
    QtCore
)

from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import (
    QApplication, 
    QWidget,
    QMessageBox
)

from alarm_clock import AlarmClock

class AlarmClockItemWidget(QWidget):

    alarm_clock_remove = pyqtSignal()

    def __init__(self, alarm_clock, list_widget_item, parent=None):
        super(AlarmClockItemWidget, self).__init__(parent)

        uic.loadUi('ui/alarm_clock_item_widget.ui', self)

        self.alarm_clock = alarm_clock
        self.alarm_clock.setParent(self)

        self.list_widget_item = list_widget_item

        self.activeCheckBox.stateChanged.connect(self.change_active)
        self.removeButton.clicked.connect(self.remove)

        self.update_info_for_gui()

    def update_info_for_gui(self):
        self.titleLabel.setText(self.alarm_clock.title)
        self.timeLabel.setText(self.alarm_clock.time.toString('hh:mm'))
        self.activeCheckBox.setChecked(self.alarm_clock.is_active)
        self.titleLabel.setStyleSheet('QLabel { color : black; }' if self.alarm_clock.is_active else 'QLabel { color : gray; }')

    def change_active(self, state):
        self.alarm_clock.is_active = self.activeCheckBox.isChecked()
        self.update_info_for_gui()

    def remove(self):
        reply = QMessageBox.question(self, 'Выход',
                                     'Вы уверены что хотите удалить будильник "' + self.alarm_clock.title + '"', 
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.alarm_clock_remove.emit()

        