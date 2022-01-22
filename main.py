# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication

from SettingsInputField.SettingsInputField_widget import SettingsInputField

if __name__ == "__main__":
    app = QApplication([])
    Widget = SettingsInputField(app)
    Widget.show()
    # ...
    sys.exit(app.exec_())
