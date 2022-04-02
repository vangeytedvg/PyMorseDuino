#
# Represents the arduino
#
import time

import serial

class Arduino:

    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.com_port = serial.Serial(self.get_port(), 9600)

    def open(self):

        self.com_port.open()

    def status(self):
        return self.comport.is_open

    def close(self):
        self.comport.close()
        pass

    def send(self):
        pass

    def read(self):
        pass

    def handshake(self):
        """"
            Check if the arduino is available
        :return:
        """
        try:
            self.comport.open()
            self.comport.readall()
            #self.comport.write(bytes("*"))
            # sleep for two seconds and the get the arduino's answer
            time.sleep(2)
            answer = self.comport.readall()
            print(answer)
            self.comport.close()
        except:
            print("Can't open port!")
