# Form implementation generated from reading ui file 'frmMain.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout.addWidget(self.lblTitle)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.lblText = QtWidgets.QLabel(self.centralwidget)
        self.lblText.setObjectName("lblText")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblText)
        self.txtEncode = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEncode.setObjectName("txtEncode")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtEncode)
        self.lblSpeed = QtWidgets.QLabel(self.centralwidget)
        self.lblSpeed.setObjectName("lblSpeed")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblSpeed)
        self.dialSpeed = QtWidgets.QDial(self.centralwidget)
        self.dialSpeed.setMinimumSize(QtCore.QSize(150, 150))
        self.dialSpeed.setMinimum(25)
        self.dialSpeed.setMaximum(300)
        self.dialSpeed.setPageStep(20)
        self.dialSpeed.setInvertedAppearance(False)
        self.dialSpeed.setInvertedControls(False)
        self.dialSpeed.setNotchesVisible(True)
        self.dialSpeed.setObjectName("dialSpeed")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dialSpeed)
        self.lcdSpeed = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdSpeed.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.lcdSpeed.setFont(font)
        self.lcdSpeed.setAutoFillBackground(True)
        self.lcdSpeed.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lcdSpeed.setSmallDecimalPoint(True)
        self.lcdSpeed.setDigitCount(7)
        self.lcdSpeed.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdSpeed.setProperty("value", 0.0)
        self.lcdSpeed.setObjectName("lcdSpeed")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lcdSpeed)
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setObjectName("btnRun")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.btnRun)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.cmbComPort = QtWidgets.QComboBox(self.centralwidget)
        self.cmbComPort.setObjectName("cmbComPort")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cmbComPort)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.menu_File.addAction(self.actionE_xit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "Arduino Morse Trainer"))
        self.lblText.setText(_translate("MainWindow", "Text to encode"))
        self.lblSpeed.setText(_translate("MainWindow", "Speed"))
        self.btnRun.setText(_translate("MainWindow", "Encode"))
        self.label.setText(_translate("MainWindow", "COM Port"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit"))
