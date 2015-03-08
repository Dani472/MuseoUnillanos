# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CambioPass.ui'
#
# Created: Sat Dec 06 21:40:43 2014
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

class Ui_CambioPass(object):
    def setupUi(self, CambioPass):
        CambioPass.setObjectName(_fromUtf8("CambioPass"))
        CambioPass.resize(361, 233)
        CambioPass.setMinimumSize(QtCore.QSize(361, 233))
        CambioPass.setMaximumSize(QtCore.QSize(361, 233))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../10808257_892502220760807_508259266_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CambioPass.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(CambioPass)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 381, 231))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Fondos/contraseña.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.TxtantiguaPass = QtGui.QLineEdit(self.centralwidget)
        self.TxtantiguaPass.setGeometry(QtCore.QRect(200, 60, 113, 20))
        self.TxtantiguaPass.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtantiguaPass.setObjectName(_fromUtf8("TxtantiguaPass"))
        self.TxtRepetirPass = QtGui.QLineEdit(self.centralwidget)
        self.TxtRepetirPass.setGeometry(QtCore.QRect(200, 120, 113, 20))
        self.TxtRepetirPass.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtRepetirPass.setObjectName(_fromUtf8("TxtRepetirPass"))
        self.TxtNuevaPass = QtGui.QLineEdit(self.centralwidget)
        self.TxtNuevaPass.setGeometry(QtCore.QRect(200, 90, 113, 20))
        self.TxtNuevaPass.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtNuevaPass.setObjectName(_fromUtf8("TxtNuevaPass"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 160, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 160, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        CambioPass.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(CambioPass)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CambioPass.setStatusBar(self.statusbar)

        self.retranslateUi(CambioPass)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtantiguaPass.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), CambioPass.Volver)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), CambioPass.CambioDePass)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtRepetirPass.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtNuevaPass.clear)
        QtCore.QMetaObject.connectSlotsByName(CambioPass)

    def retranslateUi(self, CambioPass):
        CambioPass.setWindowTitle(_translate("CambioPass", "Cambio De Contraseña", None))
        self.pushButton.setText(_translate("CambioPass", "Volver", None))
        self.pushButton_2.setText(_translate("CambioPass", "Confirmar", None))
        self.pushButton_3.setText(_translate("CambioPass", "Limpiar", None))

