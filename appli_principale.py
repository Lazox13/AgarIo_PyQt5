import os
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

# -------→ import du MenuParamètres
from gui_Parametres import Ui_MenuParam


class ApplicationPrincipale:
    def __init__(self):
        self.ui = Ui_MenuParam()
        self.ui.setupUi(self)
