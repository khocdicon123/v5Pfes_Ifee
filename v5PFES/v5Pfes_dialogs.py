from qgis.core import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from owslib.wfs import WebFeatureService

import sys
import os.path

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/module")

from update_chrung import *
from add_field_struc import *
from update_vungchitra import *
from update_dtuong_chtra import *
from update_xakk import *
from update_hesoK import *
from update_tinhchitra import *

# ------------------------------------------------------------------------------
#    dialog - base class for hcmgis dialogs containing utility functions
# ------------------------------------------------------------------------------
class _dialog(QtWidgets.QDialog):
    def __init__(self, iface):
        QtWidgets.QDialog.__init__(self)
        self.iface = iface

class update_chrung_name_dialog(_dialog, Ui_update_chrung):
    def __init__(self, iface):		
        _dialog.__init__(self, iface)	
        self.setupUi(self)
        project = QgsProject.instance()
        home_path = project.homePath()
        if not home_path:
            home_path = os.path.expanduser('~')

class add_field_struc_dialog(_dialog, Ui_add_field_struc):
    def __init__(self, iface):		
        _dialog.__init__(self, iface)	
        self.setupUi(self)
        project = QgsProject.instance()
        home_path = project.homePath()
        if not home_path:
            home_path = os.path.expanduser('~')
        
        
        

class update_vungchitra_dialog(_dialog, Ui_update_vungchitra):
    def __init__(self, iface):		
        _dialog.__init__(self, iface)	
        self.setupUi(self)
        project = QgsProject.instance()
        home_path = project.homePath()
        if not home_path:
            home_path = os.path.expanduser('~')

class update_dtuong_chtra_dialog(_dialog, Ui_update_dtuong_chtra):
    def __init__(self, iface):		
        _dialog.__init__(self, iface)	
        self.setupUi(self)
        project = QgsProject.instance()
        home_path = project.homePath()
        if not home_path:
            home_path = os.path.expanduser('~')

class update_xakk_dialog(_dialog, Ui_update_xakk):
    def __init__(self, iface):		
        _dialog.__init__(self, iface)	
        self.setupUi(self)
        project = QgsProject.instance()
        home_path = project.homePath()
        if not home_path:
            home_path = os.path.expanduser('~')

class update_hesoK_dialog(_dialog, Ui_update_hesoK):
    def __init__(self, iface):		
        _dialog.__init__(self, iface)	
        self.setupUi(self)
        project = QgsProject.instance()
        home_path = project.homePath()
        if not home_path:
            home_path = os.path.expanduser('~')

class update_tinhchitra_dialog(_dialog, Ui_update_tinhchitra):
    def __init__(self, iface):		
        _dialog.__init__(self, iface)	
        self.setupUi(self)
        project = QgsProject.instance()
        home_path = project.homePath()
        if not home_path:
            home_path = os.path.expanduser('~')



        