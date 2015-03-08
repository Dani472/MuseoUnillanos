# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuModificarInsertar.ui'
#
# Created: Sun Dec 07 23:38:55 2014
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

class Ui_MenuModificar(object):
    def setupUi(self, MenuModificar):
        MenuModificar.setObjectName(_fromUtf8("MenuModificar"))
        MenuModificar.resize(310, 325)
        MenuModificar.setMinimumSize(QtCore.QSize(310, 325))
        MenuModificar.setMaximumSize(QtCore.QSize(310, 304))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../10808257_892502220760807_508259266_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MenuModificar.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MenuModificar)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 311, 301))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Fondos/insertar.jpg")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.BVolver = QtGui.QPushButton(self.centralwidget)
        self.BVolver.setGeometry(QtCore.QRect(110, 260, 75, 23))
        self.BVolver.setObjectName(_fromUtf8("BVolver"))
        self.RBIC = QtGui.QRadioButton(self.centralwidget)
        self.RBIC.setEnabled(False)
        self.RBIC.setGeometry(QtCore.QRect(100, 80, 111, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft New Tai Lue"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RBIC.setFont(font)
        self.RBIC.setObjectName(_fromUtf8("RBIC"))
        self.RBHe = QtGui.QRadioButton(self.centralwidget)
        self.RBHe.setEnabled(False)
        self.RBHe.setGeometry(QtCore.QRect(100, 110, 121, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft New Tai Lue"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RBHe.setFont(font)
        self.RBHe.setObjectName(_fromUtf8("RBHe"))
        self.RBOr = QtGui.QRadioButton(self.centralwidget)
        self.RBOr.setGeometry(QtCore.QRect(100, 140, 111, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft New Tai Lue"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RBOr.setFont(font)
        self.RBOr.setObjectName(_fromUtf8("RBOr"))
        self.RBMu = QtGui.QRadioButton(self.centralwidget)
        self.RBMu.setEnabled(False)
        self.RBMu.setGeometry(QtCore.QRect(100, 170, 151, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft New Tai Lue"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RBMu.setFont(font)
        self.RBMu.setObjectName(_fromUtf8("RBMu"))
        self.RBIn = QtGui.QRadioButton(self.centralwidget)
        self.RBIn.setEnabled(False)
        self.RBIn.setGeometry(QtCore.QRect(100, 200, 131, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft New Tai Lue"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RBIn.setFont(font)
        self.RBIn.setObjectName(_fromUtf8("RBIn"))
        self.RBTe = QtGui.QRadioButton(self.centralwidget)
        self.RBTe.setGeometry(QtCore.QRect(100, 230, 121, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft New Tai Lue"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RBTe.setFont(font)
        self.RBTe.setObjectName(_fromUtf8("RBTe"))
        MenuModificar.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MenuModificar)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MenuModificar.setStatusBar(self.statusbar)

        self.retranslateUi(MenuModificar)
        QtCore.QObject.connect(self.BVolver, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuModificar.Volver)
        QtCore.QObject.connect(self.RBIC, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuModificar.Ictiologica)
        QtCore.QObject.connect(self.RBHe, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuModificar.Herpofologica)
        QtCore.QObject.connect(self.RBOr, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuModificar.Ornitologica)
        QtCore.QObject.connect(self.RBMu, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuModificar.Mustozoologica)
        QtCore.QObject.connect(self.RBIn, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuModificar.Invertebrados)
        QtCore.QObject.connect(self.RBTe, QtCore.SIGNAL(_fromUtf8("clicked()")), MenuModificar.Tejidos)
        QtCore.QMetaObject.connectSlotsByName(MenuModificar)

    def retranslateUi(self, MenuModificar):
        MenuModificar.setWindowTitle(_translate("MenuModificar", "Menu Modificar - Insertar  ", None))
        self.BVolver.setText(_translate("MenuModificar", "Volver", None))
        self.RBIC.setText(_translate("MenuModificar", "Ictiológica", None))
        self.RBHe.setText(_translate("MenuModificar", "Herpefológica", None))
        self.RBOr.setText(_translate("MenuModificar", "Ornitológica", None))
        self.RBMu.setText(_translate("MenuModificar", "Mustozoológica", None))
        self.RBIn.setText(_translate("MenuModificar", "Invertebrados", None))
        self.RBTe.setText(_translate("MenuModificar", "Tejidos", None))

