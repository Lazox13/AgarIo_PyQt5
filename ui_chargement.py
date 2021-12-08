# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chargementwMHqaj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Chargement(object):
    def setupUi(self, Chargement):
        if not Chargement.objectName():
            Chargement.setObjectName(u"Chargement")
        Chargement.resize(680, 400)
        Chargement.setLocale(QLocale(QLocale.French, QLocale.France))
        self.centralwidget = QWidget(Chargement)
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
        self.label_titre.setGeometry(QRect(0, 30, 661, 111))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(50)
        self.label_titre.setFont(font)
        self.label_titre.setStyleSheet(u"color: rgb(0, 255, 217);")
        self.label_titre.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_soustitre = QLabel(self.dropShadowFrame)
        self.label_soustitre.setObjectName(u"label_soustitre")
        self.label_soustitre.setGeometry(QRect(0, 140, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_soustitre.setFont(font1)
        self.label_soustitre.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_soustitre.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 260, 541, 23))
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
        font2.setPointSize(10)
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.label_soustitre_2 = QLabel(self.dropShadowFrame)
        self.label_soustitre_2.setObjectName(u"label_soustitre_2")
        self.label_soustitre_2.setGeometry(QRect(0, 290, 661, 31))
        self.label_soustitre_2.setFont(font1)
        self.label_soustitre_2.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_soustitre_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_soustitre.raise_()
        self.progressBar.raise_()
        self.label_credits.raise_()
        self.label_titre.raise_()
        self.label_soustitre_2.raise_()

        self.verticalLayout.addWidget(self.dropShadowFrame)

        Chargement.setCentralWidget(self.centralwidget)

        self.retranslateUi(Chargement)

        QMetaObject.connectSlotsByName(Chargement)
    # setupUi

    def retranslateUi(self, Chargement):
        Chargement.setWindowTitle(QCoreApplication.translate("Chargement", u"MainWindow", None))
        self.label_titre.setText(QCoreApplication.translate("Chargement", u"<strong>Agar</strong>.io", None))
        self.label_soustitre.setText(QCoreApplication.translate("Chargement", u"<strong>RAVI</strong> - Projet informatique", None))
        self.label_credits.setText(QCoreApplication.translate("Chargement", u"<strong>Cr\u00e9\u00e9 par</strong>: Arnaud MORMONT \u2022 Mat\u00e9o ROLLET", None))
        self.label_soustitre_2.setText(QCoreApplication.translate("Chargement", u"<html><head/><body><p><span style=\" font-size:11pt;\">chargement...</span></p></body></html>", None))
    # retranslateUi

