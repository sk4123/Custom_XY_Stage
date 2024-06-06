'''
Class which handles data transfer between the computer and the Arduino (through Gcode)
'''

import serial

class ToArduino():
    BAUDRATE = 115200

    def __init__(self,port,file):
        super().__init__()

        ser = serial.Serial(port,BAUDRATE,timeout=2)

        ser.write(file.encode())



'''
# Example

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=2)

g_code = 'G1 Z30.15\n'

ser.write(g_code.encode())
response = ser.readline()
print(response.decode())
ser.close()
'''