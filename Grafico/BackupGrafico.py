# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Backup.ui'
#
# Created: Fri Dec 05 17:14:50 2014
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

class Ui_Backup(object):
    def setupUi(self, Backup):
        Backup.setObjectName(_fromUtf8("Backup"))
        Backup.resize(350, 324)
        Backup.setMinimumSize(QtCore.QSize(350, 324))
        Backup.setMaximumSize(QtCore.QSize(350, 324))
        self.centralwidget = QtGui.QWidget(Backup)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 301))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Fondos/974460_904791486198547_282416342_n.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 210, 81, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.TxtPassCopia = QtGui.QLineEdit(self.centralwidget)
        self.TxtPassCopia.setGeometry(QtCore.QRect(200, 130, 113, 20))
        self.TxtPassCopia.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtPassCopia.setObjectName(_fromUtf8("TxtPassCopia"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 80, 111, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Backup.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Backup)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Backup.setStatusBar(self.statusbar)

        self.retranslateUi(Backup)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Backup.RealizarBackup)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Backup.Volver)
        QtCore.QMetaObject.connectSlotsByName(Backup)

    def retranslateUi(self, Backup):
        Backup.setWindowTitle(_translate("Backup", "Copias de seguridad", None))
        self.pushButton_2.setText(_translate("Backup", "Realizar Copia", None))
        self.comboBox.setItemText(0, _translate("Backup", "Todos los datos", None))
        self.comboBox.setItemText(1, _translate("Backup", "Usuarios", None))
        self.comboBox.setItemText(2, _translate("Backup", "Departamentos", None))
        self.comboBox.setItemText(3, _translate("Backup", "Municipios", None))
        self.comboBox.setItemText(4, _translate("Backup", "Animales Colectados", None))
        self.comboBox.setItemText(5, _translate("Backup", "Ornitologia", None))
        self.comboBox.setItemText(6, _translate("Backup", "Tejidos", None))
        self.comboBox.setItemText(7, _translate("Backup", "Localizacion", None))
        self.pushButton.setText(_translate("Backup", "Volver", None))

