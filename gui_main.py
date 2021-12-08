# ==================================================================================================================== #
# --→ Code écrit par Arnaud MORMONT.                                                                                   #
# --→ Objectif de ce fichier: Ouvrir le jeu agar.io codé en cours avec une interface graphique                         #
# --→ Ce fichier appartient au projet du cours d'informatique qui a lieu dans le cadre de la licence professionnelle   #
#     RAVI. Ce projet est codé en binôme par Arnaud MORMONT et Matéo ROLLET.                                           #
# --→ L'interface graphique a été designée grâce au logiciel QtDesigner de PyQt5.                                      #
# ==================================================================================================================== #

import os
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

# -------→ import du MenuParamètres
from gui_Parametres import Ui_MenuParam
# # -------→ import du MenuPrincipal
# import gui_Parametres
# import gui_main
from ui_chargement import Ui_Chargement

# Déclaration compteur pour chargement
compteur = 0


# FENÊTRE MENU PRINCIPAL / CHOIX PARAMÈTRES
########################################################################################################################
class MenuParam(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MenuParam()
        self.ui.setupUi(self)

        self.nbennemis = 5

        # ACTIONS BOUTONS MENU PRINCIPAL
        ###########################################################################
        # Bouton Jouer
        self.ui.bouton_jouer_param.clicked.connect(self.b_jouer_clic)

        # Bouton difficulté
        self.ui.ch_diff.clicked.connect(self.b_diff_clic)

        # Bouton mode sombre (darkmode)
        self.ui.ch_sombre.clicked.connect(self.b_sombre_clic)

        # Retirer la barre de titre de la fenêtre
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def b_jouer_clic(self):
        self.close()
        # print(self.ui.ledit_choixpseudo.text()) → récup pseudo
        print("\n"
              "############################################\n"
              "#   ---→ Démarrage par bouton jouer ←---   #\n"
              "############################################\n")
        os.system('python Agario.py')

    def b_diff_clic(self):
        if self.ui.ch_diff.isChecked():
            print("diff activée")
            self.nbennemis = 10
        else:
            print("diff désactivée")
            self.nbennemis = 5

    def b_sombre_clic(self):
        if self.ui.ch_sombre.isChecked():
            print("darkmode activé")

        else:
            print("darkmode désactivé")


# FENÊTRE CHARGEMENT
########################################################################################################################

class Chargement(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Chargement()
        self.ui.setupUi(self)

        # -------→ Retirer la barre de titre de la fenêtre
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # -------→ DÉBUT Qtimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # -------→ Qtimer en ms
        self.timer.start(35)

        # Afficher la fenêtre
        self.show()

    # FONCTION CHARGEMENT
    ####################################################################################################################
    def progress(self):
        # CHARGEMENT ET OUVERTURE MENU PRINCIPAL
        ################################################################################################################
        global compteur
        # VALEUR DE LA BARRE DE CHARGEMENT
        self.ui.progressBar.setValue(compteur)

        # FERMER LE CHARGEMENT ET OUVRIR LE MENU PRINCIPAL
        if compteur > 100:
            # Arrêter le timer
            self.timer.stop()

            # Ouvrir menu principal
            self.main = MenuParam()
            self.main.show()

            # Fermer la fenêtre de chargement
            self.close()

        # Augmenter la valeur du compteur → animation chargement
        compteur = compteur + 1


# BOUCLE APP
########################################################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Chargement()
    sys.exit(app.exec_())
