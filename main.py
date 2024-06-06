'''
File which runes the program

To do:
Get the pc to arduino connection working
Add errors
Automatic connecting to arduino??
Styling
'''

import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow(app)
    widget.show()
    sys.exit(app.exec())