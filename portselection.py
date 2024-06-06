'''
Simple UI to select the port through which the device communicates with the Arduino
'''


import serial
import serial.tools.list_ports

from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QListWidget, QVBoxLayout

class PortSelection(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Arduino Serial Port Selection")

        v_layout = QVBoxLayout()

        self.label = QListWidget()
        self.label.addItems(self.get_ardus())

        self.type = QLineEdit("Type the number of the chosen Arduino here")
        self.okay = QPushButton("Select")

        self.okay.released.connect(self.selection)

        v_layout.addWidget(self.label)
        v_layout.addWidget(self.type)
        v_layout.addWidget(self.okay)

        self.setLayout(v_layout)

    #
    def get_ardus(self):
        return [a.device for a in serial.tools.list_ports.comports() if 'Arduino' in a.description]
    
    #
    def selection(self):
        print(f"You selected: {self.type.text()}")
        
