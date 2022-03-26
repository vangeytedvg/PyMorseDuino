# 
# PyMorse.py
# Version 1.0
#
import sys
import serial
import serial.tools.list_ports

from PyQt6.QtWidgets import (QMainWindow, QApplication,
                             QTextEdit, QMessageBox, QLabel, QWidget)

from frmMain import Ui_MainWindow


class MorseWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MorseWindow, self).__init__()
        self.setupUi(self)
        # Get the available COM ports
        self.getportlist()
        # variables
        self.morseSpeed = 0
        # Bind event handlers
        self.dialSpeed.valueChanged.connect(self.changespeed)
        self.btnRun.clicked.connect(self.runencoder)
        self.cmbComPort.currentIndexChanged.connect(self.comport_changed)
        # other stuff
        self.lcdSpeed.setEnabled(True)
        self.lcdSpeed.display(self.dialSpeed.value())
        self.dialSpeed.setValue(92)

    def comport_changed(self):
        # Change comport
        pass

    def getportlist(self):
        # fill combo with available COM ports
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.cmbComPort.addItem(port.description)

    def changespeed(self):
        # handle speed of morse encoding
        self.morseSpeed = self.dialSpeed.value()
        print(self.morseSpeed)
        self.lcdSpeed.display(self.dialSpeed.value())

    def runencoder(self):
        # Send the morse code to the Arduino
        pass


if __name__ == '__main__':
    # Application entry point
    app = QApplication(sys.argv)
    main_form = MorseWindow()
    # Run the application
    main_form.show()
    sys.exit(app.exec())
