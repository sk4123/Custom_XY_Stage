'''
Class which handles data transfer between the computer and the Arduino (through Gcode)

This class handles everything about sending
'''

import serial
import time

class ToArduino():

    def __init__(self,port,file):
        super().__init__()

        self.port = port

        self.file = 'G1 F1000 X-5\n'

        self.BAUDRATE = 250000

    #
    def sendToArduino(self):
        # Works but there's a delay
        if self.port and self.file:
            ser = serial.Serial(self.port,self.BAUDRATE,timeout=2)
            ser.write(b"\r\n\r\n") # Wake up microcontroller
            time.sleep(1)
            ser.reset_input_buffer()
            ser.write(self.file.encode())
            response = ser.readline()
            print(f"Port Selection: {self.port} | File Name: {self.file}")
            print(response.decode())
        else:
            print("Error")
            print(f"Port Selection: {self.port} | File Name: {self.file}")



'''
# Example

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=2)

g_code = 'G1 Z30.15\n'

ser.write(g_code.encode())
response = ser.readline()
print(response.decode())
ser.close()
'''