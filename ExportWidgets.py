from PySide2 import QtGui, QtCore, QtWidgets

from SettingsInputField.SettingsInputField_widget import SettingsInputField


class ExportSettings_Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ExportSettings_Window, self).__init__(parent)
        self.dialog = SettingsInputField(self)
        self.dialot.show()
