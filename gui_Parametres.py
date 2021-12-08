# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuAgarIo_parametresypkSPd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import platform
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MenuParam(object):
    def setupUi(self, MenuParam):
        if not MenuParam.objectName():
            MenuParam.setObjectName(u"MenuParam")
        MenuParam.resize(680, 400)
        MenuParam.setLocale(QLocale(QLocale.French, QLocale.France))
        self.centralwidget = QWidget(MenuParam)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_titre = QLabel(self.dropShadowFrame)
        self.label_titre.setObjectName(u"label_titre")
        self.label_titre.setGeometry(QRect(0, 5, 661, 51))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_titre.setFont(font)
        self.label_titre.setStyleSheet(u"color: rgb(0, 255, 217);")
        self.label_titre.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_pseudo = QLabel(self.dropShadowFrame)
        self.label_pseudo.setObjectName(u"label_pseudo")
        self.label_pseudo.setGeometry(QRect(150, 115, 281, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_pseudo.setFont(font1)
        self.label_pseudo.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_pseudo.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_soustitre = QLabel(self.dropShadowFrame)
        self.label_soustitre.setObjectName(u"label_soustitre")
        self.label_soustitre.setGeometry(QRect(0, 75, 661, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(13)
        self.label_soustitre.setFont(font2)
        self.label_soustitre.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_soustitre.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(10, 350, 641, 21))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.Ligne_param = QLabel(self.dropShadowFrame)
        self.Ligne_param.setObjectName(u"Ligne_param")
        self.Ligne_param.setGeometry(QRect(60, 70, 550, 1))
        self.Ligne_param.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(0, 255, 217);\n"
"}")
        self.label_pseudo_2 = QLabel(self.dropShadowFrame)
        self.label_pseudo_2.setObjectName(u"label_pseudo_2")
        self.label_pseudo_2.setGeometry(QRect(150, 155, 281, 31))
        self.label_pseudo_2.setFont(font1)
        self.label_pseudo_2.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_pseudo_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_pseudo_3 = QLabel(self.dropShadowFrame)
        self.label_pseudo_3.setObjectName(u"label_pseudo_3")
        self.label_pseudo_3.setGeometry(QRect(150, 195, 281, 31))
        self.label_pseudo_3.setFont(font1)
        self.label_pseudo_3.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_pseudo_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.Ligne_param_3 = QLabel(self.dropShadowFrame)
        self.Ligne_param_3.setObjectName(u"Ligne_param_3")
        self.Ligne_param_3.setGeometry(QRect(60, 245, 550, 1))
        self.Ligne_param_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(0, 255, 217);\n"
"}")
        self.bouton_jouer_param = QPushButton(self.dropShadowFrame)
        self.bouton_jouer_param.setObjectName(u"bouton_jouer_param")
        self.bouton_jouer_param.setGeometry(QRect(205, 280, 250, 45))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.bouton_jouer_param.setFont(font4)
        self.bouton_jouer_param.setCursor(QCursor(Qt.ArrowCursor))
        self.bouton_jouer_param.setMouseTracking(False)
        self.bouton_jouer_param.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"../../PycharmProjects/agario_2.0/controller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bouton_jouer_param.setIcon(icon)
        self.bouton_jouer_param.setIconSize(QSize(32, 32))
        self.ledit_choixpseudo = QLineEdit(self.dropShadowFrame)
        self.ledit_choixpseudo.setObjectName(u"ledit_choixpseudo")
        self.ledit_choixpseudo.setGeometry(QRect(310, 115, 180, 28))
        font5 = QFont()
        font5.setPointSize(9)
        self.ledit_choixpseudo.setFont(font5)
        self.ledit_choixpseudo.setStyleSheet(u"QLineEdit{\n"
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
        self.ledit_choixpseudo.setMaxLength(18)
        self.ledit_choixpseudo.setAlignment(Qt.AlignCenter)
        self.ch_diff = QCheckBox(self.dropShadowFrame)
        self.ch_diff.setObjectName(u"ch_diff")
        self.ch_diff.setGeometry(QRect(380, 155, 32, 32))
        self.ch_diff.setCursor(QCursor(Qt.PointingHandCursor))
        self.ch_diff.setStyleSheet(u"QCheckBox::indicator {\n"
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
        self.ch_sombre = QCheckBox(self.dropShadowFrame)
        self.ch_sombre.setObjectName(u"ch_sombre")
        self.ch_sombre.setGeometry(QRect(380, 195, 32, 32))
        self.ch_sombre.setCursor(QCursor(Qt.PointingHandCursor))
        self.ch_sombre.setStyleSheet(u"QCheckBox::indicator {\n"
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
        self.label_pseudo.raise_()
        self.label_credits.raise_()
        self.label_titre.raise_()
        self.label_soustitre.raise_()
        self.Ligne_param.raise_()
        self.label_pseudo_2.raise_()
        self.label_pseudo_3.raise_()
        self.Ligne_param_3.raise_()
        self.bouton_jouer_param.raise_()
        self.ledit_choixpseudo.raise_()
        self.ch_diff.raise_()
        self.ch_sombre.raise_()

        self.verticalLayout.addWidget(self.dropShadowFrame)

        MenuParam.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuParam)

        QMetaObject.connectSlotsByName(MenuParam)
    # setupUi

    def retranslateUi(self, MenuParam):
        MenuParam.setWindowTitle(QCoreApplication.translate("MenuParam", u"MainWindow", None))
        self.label_titre.setText(QCoreApplication.translate("MenuParam", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Agar</span><span style=\" font-size:22pt;\">.io</span></p></body></html>", None))
        self.label_pseudo.setText(QCoreApplication.translate("MenuParam", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; color:#00ffd9;\">\u2022 </span><span style=\" font-size:11pt;\">Choix du </span><span style=\" font-size:11pt; font-weight:600;\">pseudo</span><span style=\" font-size:11pt;\">:</span></p></body></html>", None))
        self.label_soustitre.setText(QCoreApplication.translate("MenuParam", u"<strong>Param\u00e8tres du jeu", None))
        self.label_credits.setText(QCoreApplication.translate("MenuParam", u"<strong>Cr\u00e9\u00e9 par</strong>: Arnaud MORMONT \u2022 Mat\u00e9o ROLLET", None))
        self.Ligne_param.setText("")
        self.label_pseudo_2.setText(QCoreApplication.translate("MenuParam", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; color:#00ffd9;\">\u2022 </span><span style=\" font-size:11pt; color:#6272a4;\">Activer le mode </span><span style=\" font-size:11pt; font-weight:600;\">difficile</span><span style=\" font-size:11pt;\">:</span></p></body></html>", None))
        self.label_pseudo_3.setText(QCoreApplication.translate("MenuParam", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; color:#00ffd9;\">\u2022 </span><span style=\" font-size:11pt; color:#6272a4;\">Activer le mode </span><span style=\" font-size:11pt; font-weight:600; color:#6272a4;\">sombre</span><span style=\" font-size:11pt; color:#6272a4;\">:</span></p></body></html>", None))
        self.Ligne_param_3.setText(QCoreApplication.translate("MenuParam", u"Cliquez sur le bouton jouer", None))
        self.bouton_jouer_param.setText(QCoreApplication.translate("MenuParam", u" Jouer", None))
        self.ledit_choixpseudo.setPlaceholderText(QCoreApplication.translate("MenuParam", u"Entrez votre pseudo", None))
        self.ch_diff.setText("")
        self.ch_sombre.setText("")
    # retranslateUi
