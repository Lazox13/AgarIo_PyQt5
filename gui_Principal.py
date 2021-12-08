# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuAgarIoFzhStE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MenuPrincipal(object):
    def setupUi(self, MenuPrincipal):
        if not MenuPrincipal.objectName():
            MenuPrincipal.setObjectName(u"MenuPrincipal")
        MenuPrincipal.resize(680, 400)
        #MenuPrincipal.setLocale(QLocale(QLocale.French, QLocale.France))
        self.centralwidget = QWidget(MenuPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_titre = QLabel(self.dropShadowFrame)
        self.label_titre.setObjectName(u"label_titre")
        self.label_titre.setGeometry(QRect(0, 10, 661, 91))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_titre.setFont(font)
        self.label_titre.setStyleSheet(u"color: rgb(0, 255, 217);")
        self.label_titre.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_soustitre = QLabel(self.dropShadowFrame)
        self.label_soustitre.setObjectName(u"label_soustitre")
        self.label_soustitre.setGeometry(QRect(0, 100, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_soustitre.setFont(font1)
        self.label_soustitre.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_soustitre.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 310, 541, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.54, x2:1, y2:0.545273, stop:0 rgba(0, 255, 217, 255), stop:1 rgba(0, 153, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(10, 350, 641, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(True)
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.bouton_jouer = QPushButton(self.dropShadowFrame)
        self.bouton_jouer.setObjectName(u"bouton_jouer")
        self.bouton_jouer.setGeometry(QRect(205, 165, 250, 45))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.bouton_jouer.setFont(font3)
        self.bouton_jouer.setCursor(QCursor(Qt.ArrowCursor))
        self.bouton_jouer.setMouseTracking(False)
        self.bouton_jouer.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u"controller2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bouton_jouer.setIcon(icon)
        self.bouton_jouer.setIconSize(QSize(32, 32))
        self.bouton_jouer_2 = QPushButton(self.dropShadowFrame)
        self.bouton_jouer_2.setObjectName(u"bouton_jouer_2")
        self.bouton_jouer_2.setGeometry(QRect(205, 230, 250, 45))
        self.bouton_jouer_2.setFont(font3)
        self.bouton_jouer_2.setCursor(QCursor(Qt.ArrowCursor))
        self.bouton_jouer_2.setMouseTracking(False)
        self.bouton_jouer_2.setStyleSheet(u"QPushButton{\n"
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
        icon1 = QIcon()
        icon1.addFile(u"settings2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bouton_jouer_2.setIcon(icon1)
        self.bouton_jouer_2.setIconSize(QSize(32, 32))
        self.label_soustitre.raise_()
        self.progressBar.raise_()
        self.label_credits.raise_()
        self.label_titre.raise_()
        self.bouton_jouer.raise_()
        self.bouton_jouer_2.raise_()

        self.verticalLayout.addWidget(self.dropShadowFrame)

        MenuPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuPrincipal)

        QMetaObject.connectSlotsByName(MenuPrincipal)
    # setupUi

    def retranslateUi(self, MenuPrincipal):
        MenuPrincipal.setWindowTitle(QCoreApplication.translate("MenuPrincipal", u"MainWindow", None))
        self.label_titre.setText(QCoreApplication.translate("MenuPrincipal", u"<strong>Agar</strong>.io", None))
        self.label_soustitre.setText(QCoreApplication.translate("MenuPrincipal", u"<strong>RAVI</strong> - Projet informatique", None))
        self.label_credits.setText(QCoreApplication.translate("MenuPrincipal", u"<strong>Cr\u00e9\u00e9 par</strong>: Arnaud MORMONT \u2022 Mat\u00e9o ROLLET", None))
        self.bouton_jouer.setText(QCoreApplication.translate("MenuPrincipal", u" Jouer", None))
        self.bouton_jouer_2.setText(QCoreApplication.translate("MenuPrincipal", u" R\u00e9glages", None))
    # retranslateUi

