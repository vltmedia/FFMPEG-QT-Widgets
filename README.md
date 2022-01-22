# Description

A QT Widget for setting FFMPEG export settings.

# Usage

```python
import sys
from PySide2.QtWidgets import QApplication
from FFMPEGQTWidgets.SettingsInputField.SettingsInputField_widget import SettingsInputField
if __name__ == "__main__":
    app = QApplication([])
    Widget = SettingsInputField(app)
    Widget.show()
    # ...
    sys.exit(app.exec_())
```

![Vid1](https://github.com/vltmedia/FFMPEG-QT-Widgets/blob/master\images\screenshots\FFMPEGQTW_Video.png?raw=true)
![Vid2](https://github.com/vltmedia/FFMPEG-QT-Widgets/blob/master\images\screenshots\FFMPEGQTW_Video2.png?raw=true)
![Audio](https://github.com/vltmedia/FFMPEG-QT-Widgets/blob/master\images\screenshots\FFMPEGQTW_Audio.png?raw=true)