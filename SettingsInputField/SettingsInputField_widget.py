import json
import sys
import os
import qtawesome as qta

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QHeaderView, QFileDialog, QStackedWidget, \
    QListView, QMessageBox, QLabel, QGraphicsScene, QStyle
from PySide2.QtCore import QFile, QObject
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtUiTools import QUiLoader
from Qt import QtCore, QtGui, QtWidgets
from shutil import copyfile
from PySide2.QtCore import Signal, QThread

try:
    from SettingsInputField.SettingsInputField import Ui_Form
    from ffmpegData.GetFFMPEGCodecs import GetAudioCodecs, GetVideoCodecs, GetPixelFormats
except:
    from .SettingsInputField import Ui_Form
    from ..ffmpegData.GetFFMPEGCodecs import GetAudioCodecs, GetVideoCodecs, GetPixelFormats


class SettingsInputField(QWidget):

    def __init__(self, parent=None, context=None, *argv, **kwargs):
        super(SettingsInputField, self).__init__()
        self.parent = parent
        self.argv = argv
        self.kwargs = kwargs
        self.CurrentPreset = None
        self.codec = None
        self.dirName = os.path.dirname(__file__)
        self.loaded = False
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Settings")

        self.loaded = True
        self.ui.codecComboBox.currentTextChanged.connect(self.CodecChanged)
        self.ui.pushButton_SavePreset.clicked.connect(self.SavePresetClicked)
        self.ui.pushButton_LoadPreset.clicked.connect(self.LoadPresetClicked)
        self.ui.pushButton_SetFilePath.clicked.connect(self.LoadFileClicked)
        self.ui.pushButton_SetFilePath_Save.clicked.connect(self.LoadOutputFileClicked)
        self.ui.pushButton_Apply.clicked.connect(self.ApplyClicked)
        self.ui.pushButton_Close.clicked.connect(self.CloseClicked)
        self.SetIcons()
        self.PopulateCodecs()
        self.ApplyPreset()
        self.LoadFromKwargs()

    Apply = Signal(dict)
    Closing = Signal()

    def SetIcons(self):
        self.ui.pushButton_LoadPreset.setText("")
        self.ui.pushButton_SavePreset.setText("")
        self.ui.pushButton_SetFilePath.setText("")
        self.ui.pushButton_SetFilePath_Save.setText("")
        pixmapiOpen = qta.icon('fa5s.folder-open')
        self.ui.pushButton_LoadPreset.setIcon(pixmapiOpen)
        self.ui.pushButton_SetFilePath.setIcon(pixmapiOpen)
        pixmapiSave = qta.icon('fa5s.save')
        self.ui.pushButton_SavePreset.setIcon(pixmapiSave)
        self.ui.pushButton_SetFilePath_Save.setIcon(pixmapiSave)

        cogs = qta.icon('fa5s.cogs')
        self.setWindowIcon(cogs)

    def PopulateCodecs(self):
        self.ui.codecComboBox.addItems(GetVideoCodecs())
        self.ui.encoderComboBox.addItems(GetAudioCodecs())
        self.ui.pixelFormatComboBox.addItems(GetPixelFormats())

    def CodecChanged(self, newCodec):
        self.codec = newCodec
        self.PopulateProfiles()

    def PopulateProfiles(self):
        self.ui.profileComboBox.clear()
        if 'prores' in self.codec:
            profiles = ['proxy', 'lt', 'standard', 'hq', '4444', '4444xq']
            self.ui.profileComboBox.addItems(profiles)
            self.ui.profileComboBox.setEnabled(True)
        else:
            self.ui.profileComboBox.setEnabled(False)

    def ApplyPreset(self, codecName='h264', pixelFormatName='yuv420p', audioEncoder='aac', videoBitrate='100000',
                    audioBitrate='320', sampleRate='16000', profile='hq'):

        indexCodec = self.GetMatchingIndex(self.ui.codecComboBox, codecName)
        indexPixelFormat = self.GetMatchingIndex(self.ui.pixelFormatComboBox, pixelFormatName)
        indexAudioEncoder = self.GetMatchingIndex(self.ui.encoderComboBox, audioEncoder)
        indexSampleRate = self.GetMatchingIndex(self.ui.comboBoxSampleRate, sampleRate)

        self.ui.codecComboBox.setCurrentIndex(indexCodec)
        self.ui.pixelFormatComboBox.setCurrentIndex(indexPixelFormat)
        self.ui.encoderComboBox.setCurrentIndex(indexAudioEncoder)
        self.ui.comboBoxSampleRate.setCurrentIndex(indexSampleRate)
        self.ui.videoBitrateSpinBox.setValue(int(videoBitrate))
        self.ui.spinBoxBitrate.setValue(int(audioBitrate))
        if 'prores' in codecName:
            self.PopulateProfiles()
            indexProfile = self.GetMatchingIndex(self.ui.profileComboBox, profile)
            self.ui.profileComboBox.setCurrentIndex(indexProfile)

    def GetAsPreset(self):
        outjs = {
            "FilePath": self.ui.filePathLineEdit.text(),
            "Codec": self.ui.codecComboBox.currentText(),
            "PixelFormat": self.ui.pixelFormatComboBox.currentText(),
            "AudioEncoder": self.ui.encoderComboBox.currentText(),
            "AudioSampleRate": self.ui.comboBoxSampleRate.currentText(),
            "VideoBitRate": float(self.ui.videoBitrateSpinBox.value),
            "AudioBitRate": float(self.ui.spinBoxBitrate.value),
            "VideoProfile": self.ui.profileComboBox.currentText(),
            "Quality": float(self.ui.qualitySpinBox.value()),
            "Width": int(self.ui.dimensions_X.value()),
            "Height": int(self.ui.dimensions_Y.value()),
            "FrameRate": float(self.ui.frameRateDoubleSpinBox.value()),
            "Options": self.ui.optionsLineEdit.text(),
            "ExportAudio": str(self.ui.exportAudioCheckBox.isChecked()),
        }
        return outjs

    def LoadFromKwargs(self):
        self.ui.filePathLineEdit.setText(self.kwargs['FilePath'])
        if self.kwargs['Preset'] != None:
            self.CurrentPreset = self.kwargs['Preset']
            self.ApplyPreset(
                             videoBitrate=self.kwargs['VideoBitRate'])

        # self.ui.qualitySpinBox.setValue(int(PresetDict['Quality']))

        # self.ui.dimensions_X.setValue(int(PresetDict['Width']))
        # self.ui.dimensions_Y.setValue(int(PresetDict['Height']))
        # self.ui.optionsLineEdit.setText(PresetDict['Options'])



    def LoadPreset(self, PresetDict):
        self.CurrentPreset = PresetDict
        self.ui.qualitySpinBox.setValue(int(PresetDict['Quality']))
        self.ui.dimensions_X.setValue(int(PresetDict['Width']))
        self.ui.dimensions_Y.setValue(int(PresetDict['Height']))
        self.ui.optionsLineEdit.setText(PresetDict['Options'])
        self.ui.filePathLineEdit.setText(PresetDict['FilePath'])
        self.ApplyPreset(codecName=PresetDict['Codec'], pixelFormatName=PresetDict['PixelFormat'],
                         audioEncoder=PresetDict['AudioEncoder'],
                         videoBitrate=PresetDict['VideoBitRate'], audioBitrate=PresetDict['AudioBitRate'],
                         sampleRate=PresetDict['AudioSampleRate'],
                         profile=PresetDict['VideoProfile'])

    def SavePresetClicked(self):
        fileName = QFileDialog.getSaveFileName(self, self.tr("Save Preset"), "/", self.tr("PresetFile (*.ffp)"))
        if fileName[0]:
            file = open(fileName[0], 'w', encoding='utf-8')
            file.write(json.dumps(self.GetAsPreset(), indent=2))
            file.close()

            if os.path.exists(fileName[0]):
                msgBox = QMessageBox()
                msgBox.setText("Saved your Preset!")
                msgBox.setInformativeText("Successfully Saved your Preset!\n" + fileName[0])
                msgBox.exec()

    def LoadPresetClicked(self):
        fileName = QFileDialog.getOpenFileName(self, self.tr("Load Preset"), "/", self.tr("PresetFile (*.ffp)"))
        if fileName[0]:
            file = open(fileName[0], 'r', encoding='utf-8')
            js = json.loads(file.read())
            file.close()
            self.LoadPreset(js)
            msgBox = QMessageBox()
            msgBox.setText("Success")
            msgBox.setInformativeText("Successfully Loaded your Preset!\n" + fileName[0])
            msgBox.exec()

    def LoadFileClicked(self):
        fileName = QFileDialog.getOpenFileName(self, self.tr("Set Input Filepath"), "/", self.tr("Any (*)"))
        if fileName[0]:
            self.ui.filePathLineEdit.setText(fileName[0])

    def LoadOutputFileClicked(self):
        fileName = QFileDialog.getSaveFileName(self, self.tr("Set Output Filepath"), "/", self.tr("Any (*)"))
        if fileName[0]:
            self.ui.filePathLineEdit.setText(fileName[0])

    def GetMatchingIndex(self, comboBox, target):
        count = 0
        for item in [comboBox.itemText(i) for i in range(comboBox.count())]:
            if target in item:
                return count
            count += 1
        return -1

    def ApplyClicked(self):
        self.Apply.emit(self.GetAsPreset())
        self.close()


    def CloseClicked(self):
        self.Closing.emit()
        self.close()
