'''
Main window for the program
'''

# This Python file uses the following encoding: utf-8

import os.path

from PySide6.QtWidgets import QMainWindow, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form_6_6 import Ui_MainWindow
from editgcode import EditGcode
from portselection import PortSelection
import webbrowser

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()

        self.gedit = None
        self.loadedGcode = None
        self.sel_port = None

        self.setupUi(self)
        self.app = app

        self.actionSave.triggered.connect(self.save)
        self.actionSave_As.triggered.connect(self.saveAs)
        self.actionLoad.triggered.connect(self.load)
        self.actionReset.triggered.connect(self.reset)
        self.actionPorts.triggered.connect(self.ports)
        self.actionGCode.triggered.connect(self.gcode)
        self.actionCode.triggered.connect(self.code)
        self.actionDocumentation.triggered.connect(self.documentation)

        self.disablemotors.released.connect(self.dismotors)
        self.autohome.released.connect(self.findhome)

        self.sel_well.toggled.connect(self.well_selection)
        self.sel_row.toggled.connect(self.row_selection)
        self.sel_all.toggled.connect(self.all_selection)

        # time
        self.run.released.connect(self.go)
        self.stop.released.connect(self.stop_running)

        # self.progress_bar

        self.x_home.released.connect(self.x_homed)
        self.y_home.released.connect(self.y_homed)
        self.z_home.released.connect(self.z_homed)

        self.commit.released.connect(self.send)

        self.x_set.released.connect(self.x_home_set)
        self.y_set.released.connect(self.y_home_set)
        self.z_set.released.connect(self.z_home_set)

        self.speed_set.released.connect(self.set_speed)

        self.load_gcode.released.connect(self.loadGcode)
        self.edit_gcode.released.connect(self.editGcode)


    #### Menubar functions

    # 
    def save(self):
        print("boys")

    # Takes the current state of everything and saves it to a file
    def saveAs(self):
        print("Finally")
    
    #
    def load(self):
        print("l")

    #
    def reset(self):
        print("r")

    #
    def ports(self):
        if self.sel_port is None:
            self.sel_port = PortSelection()
        self.sel_port.show()
    
    #
    def gcode(self):
        print("g")
    
    #
    def code(self):
        print("c")

    #
    def documentation(self):
        webbrowser.open("")



    #### Left hand side

    #
    def dismotors(self):
        print("m")

    #
    def findhome(self):
        print("f")

    #
    def well_selection(self):
        print("w")

    # a place for well_edit
    def get_well(self):
        return self.well_edit.text()
    
    # sending the well edit value

    # 
    def row_selection(self):
        print("r")

    # a place for row_edit
    def get_row(self):
        return self.row_edit.text()
    
    # sending the row edit value

    # 
    def all_selection(self):
        print("a")


    # a place for the time estimation
    def time_est(self):
        print("how")

    # 
    def go(self):
        print("g")

    #
    def stop_running(self):
        print("s")



    #### Center

    # a place for the progress bar
    def setup_progress(self):
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)

    #
    def set_time(self,current_time,max_time):
        self.progress_bar.setValue(100*current_time/max_time)

    #
    def run_bar(self):
        print("something")



    #### Right hand side

    # Tells the Arduino to return to the home position for x
    def x_homed(self):
        print("x")
    
    # Tells the Arduino to return to the home position for y
    def y_homed(self):
        print("y")

    # Tells the Arduino to return to the home position for z
    def z_homed(self):
        print("z")

    # a place to read the x
    def get_x(self):
        return self.x_input.text()
    
    # send the x

    # a place to read the y
    def get_y(self):
        return self.y_input.text()
    
    # send the y

    # a place to read the z
    def get_z(self):
        return self.z_input.text()
    
    # send the z

    # sends position changes to the Arduino
    def send(self):
        print("sent")

    # 
    def x_home_set(self):
        print("x")

    # 
    def y_home_set(self):
        print("Y")

    # 
    def z_home_set(self):
        print("Z")

    # a place to read the x
    def get_x_speed(self):
        return self.x_speed.text()
    
    # send the x

    # a place to read the y
    def get_y_speed(self):
        return self.y_speed.text()
    
    # send the y

    # a place to read the z
    def get_z_speed(self):
        return self.z_speed.text()
    
    # send the z

    # 
    def set_speed(self):
        print("s")

    #
    def editGcode(self):
        if self.gedit is None:
            self.gedit = EditGcode(self.loadedGcode)
        self.gedit.show()

    # 
    def loadGcode(self):
        fileName,_ = QFileDialog.getOpenFileName(self, "Open File",
                                                      "/home",
                                                      "Text (*.txt);;All files(*.*)")
        self.loadedGcode = os.path.join(os.path.dirname(os.path.abspath(fileName)),fileName)
