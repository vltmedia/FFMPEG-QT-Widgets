# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsInputField.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(895, 387)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 891, 341))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayoutWidget = QWidget(self.tab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 861, 294))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.codecLabel = QLabel(self.formLayoutWidget)
        self.codecLabel.setObjectName(u"codecLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.codecLabel)

        self.codecComboBox = QComboBox(self.formLayoutWidget)
        self.codecComboBox.setObjectName(u"codecComboBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.codecComboBox)

        self.profileLabel = QLabel(self.formLayoutWidget)
        self.profileLabel.setObjectName(u"profileLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.profileLabel)

        self.profileComboBox = QComboBox(self.formLayoutWidget)
        self.profileComboBox.setObjectName(u"profileComboBox")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.profileComboBox)

        self.pixelFormatLabel = QLabel(self.formLayoutWidget)
        self.pixelFormatLabel.setObjectName(u"pixelFormatLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.pixelFormatLabel)

        self.pixelFormatComboBox = QComboBox(self.formLayoutWidget)
        self.pixelFormatComboBox.setObjectName(u"pixelFormatComboBox")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pixelFormatComboBox)

        self.frameRateLabel = QLabel(self.formLayoutWidget)
        self.frameRateLabel.setObjectName(u"frameRateLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.frameRateLabel)

        self.frameRateDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.frameRateDoubleSpinBox.setObjectName(u"frameRateDoubleSpinBox")
        self.frameRateDoubleSpinBox.setMaximum(200.000000000000000)
        self.frameRateDoubleSpinBox.setValue(23.980000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.frameRateDoubleSpinBox)

        self.filePathLabel = QLabel(self.formLayoutWidget)
        self.filePathLabel.setObjectName(u"filePathLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.filePathLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filePathLineEdit = QLineEdit(self.formLayoutWidget)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")

        self.horizontalLayout.addWidget(self.filePathLineEdit)

        self.pushButton_SetFilePath = QPushButton(self.formLayoutWidget)
        self.pushButton_SetFilePath.setObjectName(u"pushButton_SetFilePath")
        self.pushButton_SetFilePath.setMinimumSize(QSize(0, 21))
        self.pushButton_SetFilePath.setMaximumSize(QSize(25, 21))

        self.horizontalLayout.addWidget(self.pushButton_SetFilePath)

        self.pushButton_SetFilePath_Save = QPushButton(self.formLayoutWidget)
        self.pushButton_SetFilePath_Save.setObjectName(u"pushButton_SetFilePath_Save")
        self.pushButton_SetFilePath_Save.setMinimumSize(QSize(0, 21))
        self.pushButton_SetFilePath_Save.setMaximumSize(QSize(25, 21))

        self.horizontalLayout.addWidget(self.pushButton_SetFilePath_Save)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.optionsLabel = QLabel(self.formLayoutWidget)
        self.optionsLabel.setObjectName(u"optionsLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.optionsLabel)

        self.optionsLineEdit = QLineEdit(self.formLayoutWidget)
        self.optionsLineEdit.setObjectName(u"optionsLineEdit")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.optionsLineEdit)

        self.dimensionsLabel = QLabel(self.formLayoutWidget)
        self.dimensionsLabel.setObjectName(u"dimensionsLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.dimensionsLabel)

        self.widget = QWidget(self.formLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(130, 0))
        self.widget.setMaximumSize(QSize(130, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.dimensions_X = QSpinBox(self.widget)
        self.dimensions_X.setObjectName(u"dimensions_X")
        self.dimensions_X.setMinimumSize(QSize(60, 0))
        self.dimensions_X.setMaximumSize(QSize(60, 16777215))
        self.dimensions_X.setMaximum(100000)
        self.dimensions_X.setValue(1920)

        self.horizontalLayout_2.addWidget(self.dimensions_X)

        self.dimensions_Y = QSpinBox(self.widget)
        self.dimensions_Y.setObjectName(u"dimensions_Y")
        self.dimensions_Y.setMinimumSize(QSize(60, 0))
        self.dimensions_Y.setMaximumSize(QSize(60, 16777215))
        self.dimensions_Y.setMaximum(100000)
        self.dimensions_Y.setValue(1080)

        self.horizontalLayout_2.addWidget(self.dimensions_Y)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.widget)

        self.qualityLabel = QLabel(self.formLayoutWidget)
        self.qualityLabel.setObjectName(u"qualityLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.qualityLabel)

        self.qualitySpinBox = QSpinBox(self.formLayoutWidget)
        self.qualitySpinBox.setObjectName(u"qualitySpinBox")
        self.qualitySpinBox.setMaximum(100)
        self.qualitySpinBox.setValue(20)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.qualitySpinBox)

        self.videoBitrateLabel = QLabel(self.formLayoutWidget)
        self.videoBitrateLabel.setObjectName(u"videoBitrateLabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.videoBitrateLabel)

        self.videoBitrateSpinBox = QSpinBox(self.formLayoutWidget)
        self.videoBitrateSpinBox.setObjectName(u"videoBitrateSpinBox")
        self.videoBitrateSpinBox.setMaximum(1000000)
        self.videoBitrateSpinBox.setValue(100000)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.videoBitrateSpinBox)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.widget1 = QWidget(self.formLayoutWidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setMinimumSize(QSize(250, 0))
        self.widget1.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_PresetsComboBox = QComboBox(self.widget1)
        self.comboBox_PresetsComboBox.setObjectName(u"comboBox_PresetsComboBox")

        self.horizontalLayout_4.addWidget(self.comboBox_PresetsComboBox)

        self.pushButton_LoadPreset = QPushButton(self.widget1)
        self.pushButton_LoadPreset.setObjectName(u"pushButton_LoadPreset")
        self.pushButton_LoadPreset.setMinimumSize(QSize(30, 25))
        self.pushButton_LoadPreset.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_LoadPreset)

        self.pushButton_SavePreset = QPushButton(self.widget1)
        self.pushButton_SavePreset.setObjectName(u"pushButton_SavePreset")
        self.pushButton_SavePreset.setMinimumSize(QSize(25, 25))
        self.pushButton_SavePreset.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_SavePreset)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.widget1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayoutWidget_2 = QWidget(self.tab_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 10, 861, 121))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.exportAudioLabel = QLabel(self.formLayoutWidget_2)
        self.exportAudioLabel.setObjectName(u"exportAudioLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.exportAudioLabel)

        self.exportAudioCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.exportAudioCheckBox.setObjectName(u"exportAudioCheckBox")
        self.exportAudioCheckBox.setChecked(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.exportAudioCheckBox)

        self.encoderLabel = QLabel(self.formLayoutWidget_2)
        self.encoderLabel.setObjectName(u"encoderLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.encoderLabel)

        self.encoderComboBox = QComboBox(self.formLayoutWidget_2)
        self.encoderComboBox.setObjectName(u"encoderComboBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.encoderComboBox)

        self.audioBitrateLabel = QLabel(self.formLayoutWidget_2)
        self.audioBitrateLabel.setObjectName(u"audioBitrateLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.audioBitrateLabel)

        self.sampleRateLabel = QLabel(self.formLayoutWidget_2)
        self.sampleRateLabel.setObjectName(u"sampleRateLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.sampleRateLabel)

        self.comboBoxSampleRate = QComboBox(self.formLayoutWidget_2)
        self.comboBoxSampleRate.addItem("")
        self.comboBoxSampleRate.addItem("")
        self.comboBoxSampleRate.addItem("")
        self.comboBoxSampleRate.addItem("")
        self.comboBoxSampleRate.addItem("")
        self.comboBoxSampleRate.addItem("")
        self.comboBoxSampleRate.setObjectName(u"comboBoxSampleRate")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comboBoxSampleRate)

        self.spinBoxBitrate = QSpinBox(self.formLayoutWidget_2)
        self.spinBoxBitrate.setObjectName(u"spinBoxBitrate")
        self.spinBoxBitrate.setMaximum(512)
        self.spinBoxBitrate.setValue(320)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.spinBoxBitrate)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.formLayoutWidget_3 = QWidget(self.tab_3)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 10, 861, 251))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fFMPEGCodeLabel = QLabel(self.formLayoutWidget_3)
        self.fFMPEGCodeLabel.setObjectName(u"fFMPEGCodeLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.fFMPEGCodeLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fFMPEGCodeLineEdit = QLineEdit(self.formLayoutWidget_3)
        self.fFMPEGCodeLineEdit.setObjectName(u"fFMPEGCodeLineEdit")

        self.horizontalLayout_3.addWidget(self.fFMPEGCodeLineEdit)

        self.pushButton_FFMPEGCopyButton = QPushButton(self.formLayoutWidget_3)
        self.pushButton_FFMPEGCopyButton.setObjectName(u"pushButton_FFMPEGCopyButton")
        self.pushButton_FFMPEGCopyButton.setMinimumSize(QSize(40, 0))
        self.pushButton_FFMPEGCopyButton.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_FFMPEGCopyButton)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.widget2 = QWidget(Form)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(720, 350, 168, 23))
        self.horizontalLayout_5 = QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Apply = QPushButton(self.widget2)
        self.pushButton_Apply.setObjectName(u"pushButton_Apply")

        self.horizontalLayout_5.addWidget(self.pushButton_Apply)

        self.pushButton_Close = QPushButton(self.widget2)
        self.pushButton_Close.setObjectName(u"pushButton_Close")

        self.horizontalLayout_5.addWidget(self.pushButton_Close)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.codecLabel.setText(QCoreApplication.translate("Form", u"Codec", None))
        self.profileLabel.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.pixelFormatLabel.setText(QCoreApplication.translate("Form", u"Pixel Format", None))
        self.frameRateLabel.setText(QCoreApplication.translate("Form", u"Frame Rate", None))
        self.filePathLabel.setText(QCoreApplication.translate("Form", u"File Path", None))
#if QT_CONFIG(tooltip)
        self.pushButton_SetFilePath.setToolTip(QCoreApplication.translate("Form", u"Set New Input File Path", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_SetFilePath.setText(QCoreApplication.translate("Form", u"...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_SetFilePath_Save.setToolTip(QCoreApplication.translate("Form", u"Set New Output Filepath", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_SetFilePath_Save.setText(QCoreApplication.translate("Form", u"...", None))
        self.optionsLabel.setText(QCoreApplication.translate("Form", u"Options", None))
        self.dimensionsLabel.setText(QCoreApplication.translate("Form", u"Dimensions", None))
        self.qualityLabel.setText(QCoreApplication.translate("Form", u"Quality", None))
        self.videoBitrateLabel.setText(QCoreApplication.translate("Form", u"Video Bitrate", None))
        self.label.setText(QCoreApplication.translate("Form", u"Preset", None))
#if QT_CONFIG(tooltip)
        self.pushButton_LoadPreset.setToolTip(QCoreApplication.translate("Form", u"Load Preset", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LoadPreset.setText(QCoreApplication.translate("Form", u"L", None))
#if QT_CONFIG(tooltip)
        self.pushButton_SavePreset.setToolTip(QCoreApplication.translate("Form", u"Save Current settings to a Preset file", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_SavePreset.setText(QCoreApplication.translate("Form", u"S", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Video", None))
        self.exportAudioLabel.setText(QCoreApplication.translate("Form", u"Export Audio", None))
        self.encoderLabel.setText(QCoreApplication.translate("Form", u"Encoder", None))
        self.audioBitrateLabel.setText(QCoreApplication.translate("Form", u"Audio Bitrate", None))
        self.sampleRateLabel.setText(QCoreApplication.translate("Form", u"Sample Rate", None))
        self.comboBoxSampleRate.setItemText(0, QCoreApplication.translate("Form", u"16000", None))
        self.comboBoxSampleRate.setItemText(1, QCoreApplication.translate("Form", u"22050", None))
        self.comboBoxSampleRate.setItemText(2, QCoreApplication.translate("Form", u"24000", None))
        self.comboBoxSampleRate.setItemText(3, QCoreApplication.translate("Form", u"32000", None))
        self.comboBoxSampleRate.setItemText(4, QCoreApplication.translate("Form", u"44100", None))
        self.comboBoxSampleRate.setItemText(5, QCoreApplication.translate("Form", u"48000", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Audio", None))
        self.fFMPEGCodeLabel.setText(QCoreApplication.translate("Form", u"FFMPEG Code", None))
        self.pushButton_FFMPEGCopyButton.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Raw", None))
        self.pushButton_Apply.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.pushButton_Close.setText(QCoreApplication.translate("Form", u"Close", None))
    # retranslateUi

