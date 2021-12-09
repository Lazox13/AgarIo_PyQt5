import sys
import os

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QSize
from PyQt5.QtGui import QCursor, QFont, QIcon
from PyQt5.QtWidgets import *


class FenPrincipale(QMainWindow):
    def __init__(self):
        super(FenPrincipale, self).__init__()

        # Taille de la fenêtre principale
        self.resize(680, 400)

        # Suppression du "window tittle" et fond de la fenêtre transparent
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Ajout fond de la fenêtre (QFrame)
        self.fond = QFrame(self)
        self.fond.resize(680, 400)

        # Variables utilisées pour choix joueur via menu
        self.couleur_fond_jeu = (255, 255, 255)
        self.couleur_fond_scores = (230, 230, 230)
        self.couleur_police_scores = (0, 0, 0)
        self.couleur_grille = (150, 150, 150)

        self.fond.setCursor(QCursor(Qt.ArrowCursor))
        self.fond.setStyleSheet(
            "QFrame {\n"
            "	background-color: rgb(56, 58, 89);\n"
            "	color: rgb(220, 220, 220);\n"
            "	border-radius: 20px;\n"
            "}")

        # Ligne Haut
        self.ligne_h = QLabel(self.fond)
        self.ligne_h.setGeometry(QRect(60, 70, 550, 1))
        self.ligne_h.setStyleSheet(
            "QLabel{\n"
            "	background-color: rgb(0, 255, 217);\n"
            "}")

        # Ligne Bas
        self.ligne_b = QLabel(self.fond)
        self.ligne_b.setGeometry(QRect(60, 245, 550, 1))
        self.ligne_b.setStyleSheet(
            "QLabel{\n"
            "	background-color: rgb(0, 255, 217);\n"
            "}")

        # Titre
        self.titre = QLabel(self.fond)
        self.titre.setGeometry(QRect(0, 5, 660, 50))

        self.police_titre = QFont()
        self.police_titre.setFamily("Segoe UI")
        self.police_titre.setPointSize(40)

        self.titre.setFont(self.police_titre)
        self.titre.setStyleSheet("color: rgb(0, 255, 217);")

        self.titre.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.titre.setText("<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\""
                           ">Agar</span><span style=\" font-size:22pt;\">.io</span></p></body></html>")

        # Sous titre
        self.soustitre = QLabel(self.fond)

        self.soustitre.setGeometry(QRect(0, 75, 660, 30))
        self.soustitre.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.police_soustitre = QFont()
        self.police_soustitre.setFamily("Segoe UI")
        self.police_soustitre.setPointSize(13)

        self.soustitre.setFont(self.police_soustitre)
        self.soustitre.setStyleSheet("color: rgb(98, 114, 164)")

        self.soustitre.setText(QCoreApplication.translate("MenuParam", u"<strong>Param\u00e8tres du jeu", None))

        # Credits
        self.credits = QLabel(self.fond)

        self.credits.setGeometry(QRect(10, 370, 640, 20))

        self.police_credits = QFont()
        self.police_credits.setFamily("Segoe UI")
        self.police_credits.setPointSize(10)

        self.credits.setFont(self.police_credits)
        self.credits.setStyleSheet(u"color: rgb(98, 114, 164)")

        self.credits.setText(QCoreApplication.translate("MenuParam", "<strong>Cr\u00e9\u00e9 par</strong>: "
                                                                     "Arnaud MORMONT \u2022 Mat\u00e9o "
                                                                     "ROLLET", None))

        self.credits.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)

        # Paramètre pseudo
        self.pseudo = QLabel(self.fond)
        self.pseudo.setGeometry(QRect(150, 115, 280, 30))

        self.police_pseudo = QFont()
        self.police_pseudo.setFamily("Segoe UI")
        self.police_pseudo.setPointSize(14)

        self.pseudo.setFont(self.police_pseudo)
        self.pseudo.setStyleSheet("color: rgb(98, 114, 164);")

        self.pseudo.setText(QCoreApplication.translate("MenuParam", u"<html><head/><body><p align=\"justify\">"
                                                                    u"<span style=\" font-size:11pt; "
                                                                    u"color:#00ffd9;\">\u2022 </span><span style=\" "
                                                                    u"font-size:11pt;\">Choix du </span><span style=\" "
                                                                    u"font-size:11pt; font-weight:600;\">pseudo</span>"
                                                                    u"<span style=\" font-size:11pt;\">:</span></p>"
                                                                    u"</body></html>", None))

        # Entrée pseudo
        self.entree_pseudo = QLineEdit(self.fond)
        self.entree_pseudo.setGeometry(QRect(310, 115, 180, 28))
        self.police_entree_pseudo = QFont()
        self.police_entree_pseudo.setPointSize(9)
        self.entree_pseudo.setFont(self.police_entree_pseudo)

        self.entree_pseudo.setStyleSheet(
            "QLineEdit{\n"
            "	border-radius:10px;\n"
            "	border:1px solid rgb(0, 238, 202);\n"
            "	background-color: rgb(81, 84, 129);\n"
            "	color: rgb(0, 255, 174);\n"
            "}\n"
            "\n"
            "QLineEdit:hover{\n"
            "	border:3px solid rgb(0, 238, 202);\n"
            "}\n"
            "\n"
            "QLineEdit:focus{\n"
            "	border:3px solid rgb(0, 238, 202);\n"
            "}")

        self.entree_pseudo.setMaxLength(18)
        self.entree_pseudo.setAlignment(Qt.AlignCenter)

        # Paramètre mode difficile
        self.mode_diff = QLabel(self.fond)
        self.mode_diff.setGeometry(QRect(150, 155, 281, 31))

        self.mode_diff.setFont(self.police_pseudo)
        self.mode_diff.setStyleSheet(u"color: rgb(98, 114, 164);")

        self.mode_diff.setText(QCoreApplication.translate("MenuParam", u"<html><head/><body><p align=\"justify\">"
                                                                       u"<span style=\" font-size:11pt; color:#00ffd9;"
                                                                       u"\">\u2022 </span><span style=\" "
                                                                       u"font-size:11pt;"
                                                                       u" color:#6272a4;\">Activer le mode </span>"
                                                                       u"<span style=\" font-size:11pt; "
                                                                       u"font-weight:600;\">difficile</span><span "
                                                                       u"style=\" font-size:11pt;\">:</span></p></body>"
                                                                       u"</html>", None))

        # Variable utilisée pour choix joueur dans menu
        self.nbennemis = 5

        # Bouton mode difficile
        self.chck_diff = QCheckBox(self.fond)
        self.chck_diff.setGeometry(QRect(380, 155, 32, 32))
        self.chck_diff.setCursor(QCursor(Qt.PointingHandCursor))
        self.chck_diff.setStyleSheet(
            "QCheckBox::indicator {\n"
            "	width: 32px;\n"
            "	height: 32px;\n"
            "}\n"
            "\n"
            "QCheckBox::indicator:checked {\n"
            "    image: url(C:/Users/thegh/PycharmProjects/agario_2.0/chk_ok.png);\n"
            "}\n"
            "\n"
            "QCheckBox::indicator:unchecked {\n"
            "    image: url(C:/Users/thegh/PycharmProjects/agario_2.0/chk_nok.png);\n"
            "}")

        # Paramètre mode sombre
        self.mode_sombre = QLabel(self.fond)
        self.mode_sombre.setGeometry(QRect(150, 195, 281, 31))

        self.mode_sombre.setFont(self.police_pseudo)
        self.mode_sombre.setStyleSheet(u"color: rgb(98, 114, 164);")

        self.mode_sombre.setText(QCoreApplication.translate("MenuParam", u"<html><head/><body><p align=\"justify\">"
                                                                         u"<span style=\" font-size:11pt; color:"
                                                                         u"#00ffd9;\">\u2022 </span><span style=\" "
                                                                         u"font-size:11pt; color:#6272a4;\">Activer "
                                                                         u"le mode </span><span style=\" "
                                                                         u"font-size:11pt; font-weight:600; color:"
                                                                         u"#6272a4;\">sombre</span><span style=\" "
                                                                         u"font-size:11pt; color:#6272a4;\">:</span>"
                                                                         u"</p></body></html>", None))

        # Bouton mode sombre
        self.chck_sombre = QCheckBox(self.fond)
        self.chck_sombre.setGeometry(QRect(380, 195, 32, 32))
        self.chck_sombre.setCursor(QCursor(Qt.PointingHandCursor))
        self.chck_sombre.setStyleSheet(
            "QCheckBox::indicator {\n"
            "	width: 32px;\n"
            "	height: 32px;\n"
            "}\n"
            "\n"
            "QCheckBox::indicator:checked {\n"
            "    image: url(C:/Users/thegh/PycharmProjects/agario_2.0/chk_ok.png);\n"
            "}\n"
            "\n"
            "QCheckBox::indicator:unchecked {\n"
            "    image: url(C:/Users/thegh/PycharmProjects/agario_2.0/chk_nok.png);\n"
            "}")

        # Bouton Jouer
        self.bouton_jouer = QPushButton(self.fond)
        self.bouton_jouer.setGeometry(QRect(205, 280, 250, 45))

        self.police_bjouer = QFont()
        self.police_bjouer.setFamily("Segoe UI")
        self.police_bjouer.setPointSize(14)
        self.police_bjouer.setBold(True)
        self.police_bjouer.setWeight(75)

        self.bouton_jouer.setFont(self.police_bjouer)
        self.bouton_jouer.setCursor(QCursor(Qt.ArrowCursor))
        self.bouton_jouer.setText(QCoreApplication.translate("MenuParam", u" Jouer", None))

        self.bouton_jouer.setStyleSheet(
            "QPushButton{\n"
            "	background-color: rgb(98, 114, 164);\n"
            "	border: none;\n"
            "	color: rgb(0, 255, 217);\n"
            "	border-left: 1px solid rgb(126, 148, 212);\n"
            "	border-right: 1px solid rgb(126, 148, 212);\n"
            "	border-bottom: 3px solid rgb(126, 148, 212);\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "	background-color: rgb(117, 137, 197);\n"
            "	color: rgb(187, 255, 221);\n"
            "	border-left: 1px solid rgb(148, 175, 249);\n"
            "	border-right: 1px solid rgb(148, 175, 249);\n"
            "	border-bottom: 3px solid rgb(148, 175, 249);\n"
            "}\n"
            "\n"
            "QPushButton:pressed{\n"
            "	background-color: rgb(152, 179, 255);\n"
            "	color: rgb(187, 255, 221);\n"
            "	border-left: 1px solid rgb(117, 137, 197);\n"
            "	border-right: 1px solid rgb(117, 137, 197);\n"
            "	border-bottom: 3px solid rgb(117, 137, 197);\n"
            "}")

        # Icone du bouton Jouer
        icone_b_jouer = QIcon()
        icone_b_jouer.addFile(u"../../PycharmProjects/agario_2.0/controller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bouton_jouer.setIcon(icone_b_jouer)
        self.bouton_jouer.setIconSize(QSize(32, 32))

        # Bouton Jouer
        self.bouton_jouer.clicked.connect(self.b_jouer_clic)

        # Bouton difficulté
        self.chck_diff.clicked.connect(self.b_diff_clic)

        # Bouton mode sombre (darkmode)
        self.chck_sombre.clicked.connect(self.b_sombre_clic)

    def b_jouer_clic(self):
        # print("\n"
        #       "############################################\n"
        #       "#   ---→ Démarrage par bouton jouer ←---   #\n"
        #       "############################################\n")
        os.system('python Agario.py')
        self.close()
        # print(f"\n[CHOIX] Vous avez choisi le pseudo → {self.entree_pseudo.text()}")

    def b_diff_clic(self):
        if self.chck_diff.isChecked():
            self.nbennemis = 10
            print(f"\n[CHOIX] Mode difficile activé !\n"
                  f"        Nombre d'ennemis → {self.nbennemis}")
        else:
            self.nbennemis = 5
            print(f"\n[CHOIX] Mode difficile désactivé !\n"
                  f"        Nombre d'ennemis → {self.nbennemis}")

    def b_sombre_clic(self):
        if self.chck_sombre.isChecked():
            self.couleur_fond_jeu = (40, 40, 40)
            self.couleur_fond_scores = (25, 25, 25)
            self.couleur_police_scores = (255, 255, 255)
            self.couleur_grille = (100, 100, 100)
            print(f"\n[CHOIX] Mode sombre activé ! \n"
                  f"        Couleur du fond → {self.couleur_fond_jeu}\n"
                  f"        Couleur du fond des scores → {self.couleur_fond_scores}\n"
                  f"        Couleur de la police → {self.couleur_police_scores}\n"
                  f"        Couleur de la grille → {self.couleur_grille}")
        else:
            self.couleur_fond_jeu = (255, 255, 255)
            self.couleur_fond_scores = (230, 230, 230)
            self.couleur_police_scores = (0, 0, 0)
            self.couleur_grille = (150, 150, 150)
            print(f"\n[CHOIX] Mode sombre désactivé ! \n"
                  f"        Couleur du fond → {self.couleur_fond_jeu}\n"
                  f"        Couleur du fond des scores → {self.couleur_fond_scores}\n"
                  f"        Couleur de la police → {self.couleur_police_scores}\n"
                  f"        Couleur de la grille → {self.couleur_grille}")


def run_fen():
    app = QApplication(sys.argv)
    window = FenPrincipale()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_fen()