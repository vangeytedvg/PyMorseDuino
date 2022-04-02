# 
# PyMorse
# Version 1.0
# Author : Danny Van Geyte
# History : - 25/03/2022 SOD
#           - 26/03/2022 Added COM port detection and basic event handlers
#

import sys
import serial
import serial.tools.list_ports

from PyQt6.QtWidgets import (QMainWindow, QApplication,
                             QTextEdit, QMessageBox, QLabel, QWidget)

from frmMain import Ui_MainWindow

from arduino import Arduino


class MorseWindow(QMainWindow, Ui_MainWindow):

    def __delete__(self, instance):
        if ser:
            self.ser.close()

    def __init__(self):
        super(MorseWindow, self).__init__()
        self.setupUi(self)
        # Get the available COM ports
        self.getportlist()
        # variables
        self.morseSpeed = 0
        self.active_comport = ""
        # Bind event handlers
        self.dialSpeed.valueChanged.connect(self.changespeed)
        self.btnRun.clicked.connect(self.runencoder)
        self.cmbComPort.currentIndexChanged.connect(self.comport_changed)
        # other stuff
        self.lcdSpeed.setEnabled(True)
        self.lcdSpeed.display(self.dialSpeed.value())
        self.dialSpeed.setValue(92)
        self.ser = None

    def get_port(self):
        # Get the real COM port from the string in the combobox
        x = self.cmbComPort.currentText()
        pos1 = x.find("(")
        pos2 = x.find(")")
        if pos1 > 0 and pos2 > 0:
            comPort = x[pos1 + 1:pos2]
            return comPort
        else:
            print("Not a COM port!")
            return None

    def comport_changed(self):
        # Check if there is a port open
        self.ser = serial.Serial(self.get_port(), 9600)

    def getportlist(self):
        # fill combo with available COM ports
        ports = serial.tools.list_ports.comports()
        self.cmbComPort.addItem("None")
        for port in ports:
            self.cmbComPort.addItem(port.description)

    def changespeed(self):
        # handle speed of morse encoding
        self.morseSpeed = self.dialSpeed.value()
        self.lcdSpeed.display(self.dialSpeed.value())


    def runencoder(self):
        # Send the morse code to the Arduino
        self.ser.write(b'#100')



if __name__ == '__main__':
    # Application entry point
    app = QApplication(sys.argv)
    main_form = MorseWindow()
    # Run the application
    main_form.show()
    sys.exit(app.exec())
