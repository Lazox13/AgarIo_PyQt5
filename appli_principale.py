import os
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

# -------→ import du MenuPrincipal
from gui_main import Chargement
from FenPrincipale import FenPrincipale

# from Classe_AgarIo import AgarIo


class AgarIo:
    def __init__(self):
        self.menu_principal = FenPrincipale()
        self.menu_principal.show()
        # self.jeu = Agario()


# Boucle appli
if __name__ == "__main__":
    app = QApplication(sys.argv)
    agario = FenPrincipale()
    sys.exit(app.exec_())
