# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuAdministrador.ui'
#
# Created: Tue Dec 09 08:00:43 2014
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

class Ui_Menuadmin(object):
    def setupUi(self, Menuadmin):
        Menuadmin.setObjectName(_fromUtf8("Menuadmin"))
        Menuadmin.resize(323, 400)
        Menuadmin.setMinimumSize(QtCore.QSize(323, 400))
        Menuadmin.setMaximumSize(QtCore.QSize(323, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../10808257_892502220760807_508259266_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Menuadmin.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Menuadmin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, -20, 441, 421))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("High Tower Text"))
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Fondos/10841299_904791456198550_2128780366_n.jpg")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.BSalir = QtGui.QPushButton(self.centralwidget)
        self.BSalir.setGeometry(QtCore.QRect(120, 330, 75, 23))
        self.BSalir.setObjectName(_fromUtf8("BSalir"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 90, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 130, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.BcambioPassadmin = QtGui.QPushButton(self.centralwidget)
        self.BcambioPassadmin.setGeometry(QtCore.QRect(120, 250, 75, 23))
        self.BcambioPassadmin.setObjectName(_fromUtf8("BcambioPassadmin"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 210, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 290, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        Menuadmin.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Menuadmin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Menuadmin.setStatusBar(self.statusbar)

        self.retranslateUi(Menuadmin)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Menuadmin.Busqueda)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Menuadmin.Modificar)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Menuadmin.Usuarios)
        QtCore.QObject.connect(self.BSalir, QtCore.SIGNAL(_fromUtf8("clicked()")), Menuadmin.Salir)
        QtCore.QObject.connect(self.BcambioPassadmin, QtCore.SIGNAL(_fromUtf8("clicked()")), Menuadmin.CambioPassadmin)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Menuadmin.CopiaSeguridad)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), Menuadmin.VerAportes)
        QtCore.QMetaObject.connectSlotsByName(Menuadmin)
        Menuadmin.setTabOrder(self.pushButton, self.pushButton_2)
        Menuadmin.setTabOrder(self.pushButton_2, self.pushButton_3)
        Menuadmin.setTabOrder(self.pushButton_3, self.BSalir)

    def retranslateUi(self, Menuadmin):
        Menuadmin.setWindowTitle(_translate("Menuadmin", "Menu", None))
        self.BSalir.setText(_translate("Menuadmin", "Salir", None))
        self.pushButton.setText(_translate("Menuadmin", "Busqueda", None))
        self.pushButton_2.setText(_translate("Menuadmin", "Insertar", None))
        self.pushButton_3.setText(_translate("Menuadmin", "Usuarios", None))
        self.BcambioPassadmin.setText(_translate("Menuadmin", "Cambian Pass", None))
        self.pushButton_4.setText(_translate("Menuadmin", "Backup", None))
        self.pushButton_5.setText(_translate("Menuadmin", "Ver Aportes", None))

