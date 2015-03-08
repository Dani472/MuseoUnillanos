# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EliminarUser.ui'
#
# Created: Tue Dec 09 09:18:06 2014
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

class Ui_EliminarUser(object):
    def setupUi(self, EliminarUser):
        EliminarUser.setObjectName(_fromUtf8("EliminarUser"))
        EliminarUser.resize(365, 209)
        EliminarUser.setMinimumSize(QtCore.QSize(365, 209))
        EliminarUser.setMaximumSize(QtCore.QSize(365, 209))
        self.centralwidget = QtGui.QWidget(EliminarUser)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 381, 201))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Fondos/Eliminar-usuario.jpg")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.BConfirmar = QtGui.QPushButton(self.centralwidget)
        self.BConfirmar.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.BConfirmar.setObjectName(_fromUtf8("BConfirmar"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 150, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.TxtUserEliminar = QtGui.QLineEdit(self.centralwidget)
        self.TxtUserEliminar.setGeometry(QtCore.QRect(220, 90, 113, 20))
        self.TxtUserEliminar.setObjectName(_fromUtf8("TxtUserEliminar"))
        self.TxtPassadmin = QtGui.QLineEdit(self.centralwidget)
        self.TxtPassadmin.setGeometry(QtCore.QRect(230, 120, 113, 20))
        self.TxtPassadmin.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtPassadmin.setObjectName(_fromUtf8("TxtPassadmin"))
        EliminarUser.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(EliminarUser)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EliminarUser.setStatusBar(self.statusbar)

        self.retranslateUi(EliminarUser)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), EliminarUser.Volver)
        QtCore.QObject.connect(self.BConfirmar, QtCore.SIGNAL(_fromUtf8("clicked()")), EliminarUser.Confirmar)
        QtCore.QObject.connect(self.BConfirmar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtPassadmin.clear)
        QtCore.QObject.connect(self.BConfirmar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtUserEliminar.clear)
        QtCore.QMetaObject.connectSlotsByName(EliminarUser)

    def retranslateUi(self, EliminarUser):
        EliminarUser.setWindowTitle(_translate("EliminarUser", "Eliminar", None))
        self.BConfirmar.setText(_translate("EliminarUser", "Confirmar", None))
        self.pushButton.setText(_translate("EliminarUser", "Volver", None))

