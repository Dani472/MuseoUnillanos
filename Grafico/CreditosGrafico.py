# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Creditos.ui'
#
# Created: Wed Dec 03 14:57:29 2014
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

class Ui_Creditos(object):
    def setupUi(self, Creditos):
        Creditos.setObjectName(_fromUtf8("Creditos"))
        Creditos.setWindowModality(QtCore.Qt.NonModal)
        Creditos.resize(383, 361)
        Creditos.setMinimumSize(QtCore.QSize(383, 340))
        Creditos.setMaximumSize(QtCore.QSize(383, 361))
        Creditos.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        Creditos.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/danielfernando/.designer/10808257_892502220760807_508259266_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Creditos.setWindowIcon(icon)
        Creditos.setAccessibleName(_fromUtf8(""))
        Creditos.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(Creditos)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 391, 341))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setTextFormat(QtCore.Qt.LogText)
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Fondos/creditos.jpg")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Bvolver = QtGui.QPushButton(self.centralwidget)
        self.Bvolver.setGeometry(QtCore.QRect(280, 260, 75, 23))
        self.Bvolver.setObjectName(_fromUtf8("Bvolver"))
        Creditos.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Creditos)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Creditos.setStatusBar(self.statusbar)

        self.retranslateUi(Creditos)
        QtCore.QObject.connect(self.Bvolver, QtCore.SIGNAL(_fromUtf8("clicked()")), Creditos.Volver)
        QtCore.QMetaObject.connectSlotsByName(Creditos)

    def retranslateUi(self, Creditos):
        Creditos.setWindowTitle(_translate("Creditos", "Creditos", None))
        self.Bvolver.setText(_translate("Creditos", "Volver", None))

