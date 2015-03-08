# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AportesUser.ui'
#
# Created: Mon Dec 08 00:48:54 2014
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

class Ui_Aportes(object):
    def setupUi(self, Aportes):
        Aportes.setObjectName(_fromUtf8("Aportes"))
        Aportes.resize(480, 339)
        Aportes.setMinimumSize(QtCore.QSize(480, 339))
        Aportes.setMaximumSize(QtCore.QSize(480, 339))
        self.centralwidget = QtGui.QWidget(Aportes)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 461, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 71, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.TxtPass = QtGui.QLineEdit(self.groupBox)
        self.TxtPass.setGeometry(QtCore.QRect(140, 50, 113, 20))
        self.TxtPass.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtPass.setObjectName(_fromUtf8("TxtPass"))
        self.TxtAportes = QtGui.QPlainTextEdit(self.groupBox)
        self.TxtAportes.setGeometry(QtCore.QRect(140, 80, 301, 111))
        self.TxtAportes.setObjectName(_fromUtf8("TxtAportes"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 200, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 471, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 290, 161, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 290, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Aportes.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Aportes)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Aportes.setStatusBar(self.statusbar)

        self.retranslateUi(Aportes)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Aportes.Volver)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Aportes.Guardar)
        QtCore.QMetaObject.connectSlotsByName(Aportes)

    def retranslateUi(self, Aportes):
        Aportes.setWindowTitle(_translate("Aportes", "Aportes", None))
        self.groupBox.setTitle(_translate("Aportes", "Datos Requeridos", None))
        self.label_2.setText(_translate("Aportes", "Contraseña", None))
        self.label_3.setText(_translate("Aportes", "Aportes", None))
        self.pushButton_2.setText(_translate("Aportes", "Aceptar", None))
        self.label.setText(_translate("Aportes", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#0000ff;\">Aportes</span></p></body></html>", None))
        self.label_4.setText(_translate("Aportes", "Universidad de los Llanos 2014 ®", None))
        self.pushButton.setText(_translate("Aportes", "Volver", None))

