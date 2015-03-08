# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VerAportes.ui'
#
# Created: Mon Dec 08 09:39:10 2014
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

class Ui_AportesUser(object):
    def setupUi(self, AportesUser):
        AportesUser.setObjectName(_fromUtf8("AportesUser"))
        AportesUser.resize(357, 242)
        AportesUser.setMinimumSize(QtCore.QSize(357, 242))
        AportesUser.setMaximumSize(QtCore.QSize(357, 242))
        self.centralwidget = QtGui.QWidget(AportesUser)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 331, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 211, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 141, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 90, 131, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 341, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 190, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        AportesUser.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(AportesUser)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AportesUser.setStatusBar(self.statusbar)

        self.retranslateUi(AportesUser)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AportesUser.Volver)
        QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), AportesUser.Sql)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), AportesUser.Excel)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AportesUser.Txt)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), AportesUser.AbrirCarpeta)
        QtCore.QMetaObject.connectSlotsByName(AportesUser)

    def retranslateUi(self, AportesUser):
        AportesUser.setWindowTitle(_translate("AportesUser", "Ver Aportes", None))
        self.pushButton.setText(_translate("AportesUser", "Volver", None))
        self.groupBox.setTitle(_translate("AportesUser", "Exportar", None))
        self.radioButton.setText(_translate("AportesUser", "Archivo de texto plano", None))
        self.radioButton_2.setText(_translate("AportesUser", "Archivo Excel", None))
        self.radioButton_3.setText(_translate("AportesUser", "Archivo SQL", None))
        self.label.setText(_translate("AportesUser", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">Aportes</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("AportesUser", "Ver Carpeta ", None))

