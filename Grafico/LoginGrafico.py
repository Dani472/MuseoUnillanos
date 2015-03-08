# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created: Fri Dec 05 17:06:04 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.setWindowModality(QtCore.Qt.NonModal)
        Login.resize(463, 326)
        Login.setMinimumSize(QtCore.QSize(463, 326))
        Login.setMaximumSize(QtCore.QSize(463, 326))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../10808257_892502220760807_508259266_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        Login.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(Login)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 471, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("High Tower Text"))
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Fondos/10818706_904791449531884_726653690_n.jpg")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.BCreditos = QtGui.QPushButton(self.centralwidget)
        self.BCreditos.setGeometry(QtCore.QRect(10, 280, 75, 23))
        self.BCreditos.setObjectName(_fromUtf8("BCreditos"))
        self.TxtUsuario = QtGui.QLineEdit(self.centralwidget)
        self.TxtUsuario.setGeometry(QtCore.QRect(250, 120, 113, 20))
        self.TxtUsuario.setObjectName(_fromUtf8("TxtUsuario"))
        self.TxtClave = QtGui.QLineEdit(self.centralwidget)
        self.TxtClave.setGeometry(QtCore.QRect(250, 160, 113, 20))
        self.TxtClave.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtClave.setObjectName(_fromUtf8("TxtClave"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 230, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 230, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Login)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QObject.connect(self.BCreditos, QtCore.SIGNAL(_fromUtf8("clicked()")), Login.Credito)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Login.Ingreso)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtClave.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtClave.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtUsuario.clear)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Ingresar", None))
        self.BCreditos.setText(_translate("Login", "Creditos", None))
        self.pushButton.setText(_translate("Login", "Limpiar", None))
        self.pushButton_2.setText(_translate("Login", "Ingresar", None))

