# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuInvitado.ui'
#
# Created: Wed Dec 03 14:32:16 2014
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

class Ui_MenuInvitado(object):
    def setupUi(self, MenuInvitado):
        MenuInvitado.setObjectName(_fromUtf8("MenuInvitado"))
        MenuInvitado.resize(323, 323)
        MenuInvitado.setMinimumSize(QtCore.QSize(323, 323))
        MenuInvitado.setMaximumSize(QtCore.QSize(323, 323))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../10808257_892502220760807_508259266_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MenuInvitado.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MenuInvitado)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 441, 311))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("High Tower Text"))
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Fondos/menu.jpg")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.BSalir = QtGui.QPushButton(self.centralwidget)
        self.BSalir.setGeometry(QtCore.QRect(120, 230, 75, 23))
        self.BSalir.setObjectName(_fromUtf8("BSalir"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 110, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.BCambioPassInvitado = QtGui.QPushButton(self.centralwidget)
        self.BCambioPassInvitado.setGeometry(QtCore.QRect(120, 190, 75, 23))
        self.BCambioPassInvitado.setObjectName(_fromUtf8("BCambioPassInvitado"))
        MenuInvitado.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MenuInvitado)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MenuInvitado.setStatusBar(self.statusbar)

        self.retranslateUi(MenuInvitado)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuInvitado.Busqueda)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuInvitado.aportes)
        QtCore.QObject.connect(self.BSalir, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuInvitado.Salir)
        QtCore.QObject.connect(self.BCambioPassInvitado, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuInvitado.CambioPassInvitado)
        QtCore.QMetaObject.connectSlotsByName(MenuInvitado)
        MenuInvitado.setTabOrder(self.pushButton, self.pushButton_3)
        MenuInvitado.setTabOrder(self.pushButton_3, self.BSalir)

    def retranslateUi(self, MenuInvitado):
        MenuInvitado.setWindowTitle(_translate("MenuInvitado", "Menu", None))
        self.BSalir.setText(_translate("MenuInvitado", "Salir", None))
        self.pushButton.setText(_translate("MenuInvitado", "Busqueda", None))
        self.pushButton_3.setText(_translate("MenuInvitado", "Aportes", None))
        self.BCambioPassInvitado.setText(_translate("MenuInvitado", "Cambiar Pass", None))

