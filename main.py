'''
File which runes the program

To do:
Fix the save feature in the main window?? - default settings, saved settings
Get the pc to arduino connection working
Add errors - for ex, if no port or file is selected before running
Automatic connecting to arduino??
Styling
Adding the connected button up top (as well as an indication of the port)
Setting up the clickers

Need a way to home the z as a 3d printer does (touching the lowest point it'll every go)

When you open a file with "edit," it doesn't make it the actual file

# to determine the OS
import platform
'''

import sys
from PySide6.QtWidgets import QApplication
from modules.mainwindow import MainWindow
# import default

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow(app) #default
    widget.show()
    sys.exit(app.exec())