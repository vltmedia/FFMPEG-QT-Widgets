from PySide2 import QtGui, QtCore, QtWidgets

try:
    from SettingsInputField.SettingsInputField_widget import SettingsInputField
except:
    from .SettingsInputField.SettingsInputField_widget import SettingsInputField


class ExportSettings_Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *argv, **kwargs):
        super(ExportSettings_Window, self).__init__(parent)
        self.widget = SettingsInputField(self, *argv, **kwargs)
        self.widget.show()
        self.widget.Apply.connect(self.close)
        self.widget.Closing.connect(self.close)



def ExportSettings_Widget(parent=None):
    widget = SettingsInputField(parent)
    return widget
