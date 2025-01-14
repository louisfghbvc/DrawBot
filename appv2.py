# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pynput.keyboard import Key, Listener
import utils
import drawbot
import threading

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PyQt5.QtWinExtras import QtWin
    myappid = 'louisfghbvc.drawbot.1'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 374, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.title.setStyleSheet("font-weight:bold;")
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.urlTextBox = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.urlTextBox.setText("")
        self.urlTextBox.setObjectName("urlTextBox")
        self.verticalLayout.addWidget(self.urlTextBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.appLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.appLabel.setStyleSheet("")
        self.appLabel.setObjectName("appLabel")
        self.verticalLayout.addWidget(self.appLabel)
        self.appBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.appBox.setObjectName("appBox")
        self.appBox.addItem("")
        self.appBox.addItem("")
        self.appBox.addItem("")
        self.appBox.addItem("")
        self.verticalLayout.addWidget(self.appBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.speedLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.speedLabel.setObjectName("speedLabel")
        self.verticalLayout.addWidget(self.speedLabel)
        self.speedSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.speedSlider.setMinimum(1)
        self.speedSlider.setMaximum(4)
        self.speedSlider.setProperty("value", 3)
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setObjectName("speedSlider")
        self.verticalLayout.addWidget(self.speedSlider)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.skippedPixelsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.skippedPixelsLabel.setObjectName("skippedPixelsLabel")
        self.verticalLayout.addWidget(self.skippedPixelsLabel)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font-size: 10px;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.skippedPixelSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.skippedPixelSlider.setMinimum(1)
        self.skippedPixelSlider.setMaximum(12)
        self.skippedPixelSlider.setSingleStep(1)
        self.skippedPixelSlider.setProperty("value", 5)
        self.skippedPixelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.skippedPixelSlider.setObjectName("skippedPixelSlider")
        self.verticalLayout.addWidget(self.skippedPixelSlider)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ignorePixelBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.ignorePixelBox.setObjectName("ignorePixelBox")
        self.horizontalLayout.addWidget(self.ignorePixelBox)
        self.grayBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.grayBox.setObjectName("grayBox")
        self.horizontalLayout.addWidget(self.grayBox)
        self.ditherBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.ditherBox.setObjectName("ditherBox")
        self.horizontalLayout.addWidget(self.ditherBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dfsBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.dfsBox.setObjectName("dfsBox")
        self.horizontalLayout_2.addWidget(self.dfsBox)
        self.edgeBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.edgeBox.setObjectName("edgeBox")
        self.horizontalLayout_2.addWidget(self.edgeBox)
        self.edgeEXBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.edgeEXBox.setObjectName("edgeEXBox")
        self.horizontalLayout_2.addWidget(self.edgeEXBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.coordinateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.coordinateButton.setObjectName("coordinateButton")
        self.verticalLayout.addWidget(self.coordinateButton)
        self.MouseCoordinateLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.MouseCoordinateLabel.setObjectName("MouseCoordinateLabel")
        self.verticalLayout.addWidget(self.MouseCoordinateLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.setBoundsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.setBoundsButton.setObjectName("setBoundsButton")
        self.verticalLayout.addWidget(self.setBoundsButton)
        self.widthLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.widthLabel.setObjectName("widthLabel")
        self.verticalLayout.addWidget(self.widthLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.drawButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.5, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 134, 22))
        gradient.setColorAt(1.0, QtGui.QColor(0, 74, 26))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.5, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 134, 22))
        gradient.setColorAt(1.0, QtGui.QColor(0, 74, 26))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.5, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 134, 22))
        gradient.setColorAt(1.0, QtGui.QColor(0, 74, 26))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.5, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 134, 22))
        gradient.setColorAt(1.0, QtGui.QColor(0, 74, 26))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.5, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 134, 22))
        gradient.setColorAt(1.0, QtGui.QColor(0, 74, 26))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.5, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 134, 22))
        gradient.setColorAt(1.0, QtGui.QColor(0, 74, 26))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.5, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 134, 22))
        gradient.setColorAt(1.0, QtGui.QColor(0, 74, 26))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.5, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 134, 22))
        gradient.setColorAt(1.0, QtGui.QColor(0, 74, 26))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.5, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 134, 22))
        gradient.setColorAt(1.0, QtGui.QColor(0, 74, 26))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.drawButton.setPalette(palette)
        self.drawButton.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 134, 22, 255), stop:1 rgba(0, 74, 26, 255));\n"
"font-weight: bold;\n"
"color: white;\n"
"height: 30px;\n"
"")
        self.drawButton.setObjectName("drawButton")
        self.verticalLayout.addWidget(self.drawButton)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.errorLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.errorLabel.setStyleSheet("color: rgb(170, 0, 0);\n"
"font-weight: bold;\n"
"")
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout.addWidget(self.errorLabel, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Custom values
        self.width = 0
        self.height = 0
        self.startPosition = (0, 0)
        self.ignorePixels = False
        self.dither = False
        self.isDfs = False
        self.isEdge = False
        self.isEdgeEX = False
        self.isGray = False
        self.speed = 3
        self.pixelInterval = 5
        self.url = ""
        self.app = 0
        self.colors, self.coordinates = utils.getPalette(self.app)
        self.drawingThread = None

        # Signals
        self.coordinateButton.clicked.connect(self.displayMouseCoordinates)
        self.setBoundsButton.clicked.connect(self.setBounds)
        self.ditherBox.clicked.connect(self.setDither)
        self.edgeBox.clicked.connect(self.setEdge)
        self.edgeEXBox.clicked.connect(self.setEdgeEX)
        self.dfsBox.clicked.connect(self.setDFS)
        self.ignorePixelBox.clicked.connect(self.setIgnorePixel)
        self.speedSlider.valueChanged.connect(self.setSpeed)
        self.skippedPixelSlider.valueChanged.connect(self.setPixelInterval)
        self.appBox.currentIndexChanged.connect(self.setApp)
        self.urlTextBox.textChanged.connect(self.setUrl)
        self.drawButton.clicked.connect(self.draw)
        self.grayBox.clicked.connect(self.setGray)

        # Collect keyboard events
        listener = Listener(
            on_press=self.on_press)
        listener.start()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DrawBot"))
        MainWindow.setWindowIcon(QtGui.QIcon('drawEX.ico'))
        self.title.setText(_translate("MainWindow", "DrawBot - @尾玉"))
        self.urlTextBox.setPlaceholderText(_translate("MainWindow", "要繪製的圖像的 URL"))
        self.appLabel.setText(_translate("MainWindow", "選擇遊戲平台"))
        self.appBox.setItemText(0, _translate("MainWindow", "Gartic Phone"))
        self.appBox.setItemText(1, _translate("MainWindow", "Skribbl"))
        self.appBox.setItemText(2, _translate("MainWindow", "Paint"))
        self.appBox.setItemText(3, _translate("MainWindow", "Gartic"))
        self.speedLabel.setText(_translate("MainWindow", "速度"))
        self.skippedPixelsLabel.setText(_translate("MainWindow", "忽略像素"))
        self.label_4.setText(_translate("MainWindow", "忽略像素越少，就越精確（但速度較慢）"))
        self.ignorePixelBox.setText(_translate("MainWindow", "忽略單像素(忽略群大小)"))
        self.grayBox.setText(_translate("MainWindow", "灰階"))
        self.ditherBox.setText(_translate("MainWindow", "抖動"))
        self.dfsBox.setText(_translate("MainWindow", "方位畫法"))
        self.edgeBox.setText(_translate("MainWindow", "輪廓畫法"))
        self.edgeEXBox.setText(_translate("MainWindow", "輪廓畫法+"))
        self.coordinateButton.setText(_translate("MainWindow", "獲取鼠標坐標（下一次點擊）"))
        self.MouseCoordinateLabel.setText(_translate("MainWindow", "座標將顯示在此處"))
        self.setBoundsButton.setText(_translate("MainWindow", "設置繪圖寬度"))
        self.widthLabel.setText(_translate("MainWindow", "目前：無。"))
        self.drawButton.setText(_translate("MainWindow", "畫！"))
        self.errorLabel.setText(_translate("MainWindow", "錯誤信息"))

    def on_press(self, key):
        if key == Key.esc and self.drawingThread != None:
            self.exit_event.set()
    
    def setApp(self, value):
        self.app = value
        self.colors, self.coordinates = utils.getPalette(self.app)

    def setUrl(self, value):
        self.url = value

    def setSpeed(self, value):
        self.speed = value

    def setPixelInterval(self, value):
        self.pixelInterval = value
        self.skippedPixelsLabel.setText("省略像素 : " + str(value))

    def setDither(self):
        self.dither = self.ditherBox.isChecked()
    
    def setEdge(self):
        self.isEdge = self.edgeBox.isChecked()
    
    def setEdgeEX(self):
        self.isEdgeEX = self.edgeEXBox.isChecked()
    
    def setGray(self):
        self.isGray = self.grayBox.isChecked()
    
    def setDFS(self):
        self.isDfs = self.dfsBox.isChecked()

    def setIgnorePixel(self):
        self.ignorePixels = self.ignorePixelBox.isChecked()

    def setBounds(self):
        t = threading.Thread(target=self.setBoundsWorker)
        t.start()

    def setBoundsWorker(self):
        self.widthLabel.setText("正在選擇中...")
        self.MouseCoordinateLabel.adjustSize()
        bounds = utils.getBounds()
        self.width = abs(bounds[0][0] - bounds[1][0])
        self.height = abs(bounds[0][1] - bounds[1][1])
        self.startPosition = (bounds[0][0], bounds[0][1])
        self.widthLabel.setText(str(self.width) + ' x ' + str(self.height) + ' px')
    
    def displayMouseCoordinates(self):
        t = threading.Thread(target=self.displayMouseCoordinatesWorker)
        t.start()
    
    def displayMouseCoordinatesWorker(self):
        self.MouseCoordinateLabel.setText(str(utils.getNextMouseClickPositionCoordinates()))

    def draw(self):
        if self.url != "" and self.width != 0:
            self.exit_event = threading.Event()
            self.errorLabel.setText("")
            self.drawingThread = threading.Thread(target=self.drawWorker)
            self.drawingThread.start()
        else:
            if self.url == "":
                self.errorLabel.setText("請輸入url, please enter url:")
            elif self.width == 0:
                self.errorLabel.setText("請選擇畫畫的範圍")
    
    def drawWorker(self):
        try:
            draw = drawbot.DrawBot(self.width, self.height, self.startPosition, 
                    self.ignorePixels, self.dither, self.speed, self.pixelInterval, 
                    self.url, self.colors, self.coordinates, self.isDfs, 
                    self.isEdge, self.isEdgeEX, self.isGray)
            draw.draw(self.exit_event)
        except Exception as error:
            print(error)
            self.errorLabel.setText(str(error))
            pass
        self.drawingThread = None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
