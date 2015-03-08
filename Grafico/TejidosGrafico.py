# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tejidos.ui'
#
# Created: Wed Dec 03 15:41:01 2014
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

class Ui_Tejidos(object):
    def setupUi(self, Tejidos):
        Tejidos.setObjectName(_fromUtf8("Tejidos"))
        Tejidos.resize(390, 313)
        Tejidos.setMinimumSize(QtCore.QSize(390, 313))
        Tejidos.setMaximumSize(QtCore.QSize(390, 313))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../10808257_892502220760807_508259266_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Tejidos.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Tejidos)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 391, 301))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("High Tower Text"))
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Fondos/TEJIDOS.jpg")))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.TxtNombre = QtGui.QLineEdit(self.centralwidget)
        self.TxtNombre.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.TxtNombre.setObjectName(_fromUtf8("TxtNombre"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 150, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 190, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 220, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(170, 140, 101, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.TxtDescripcion = QtGui.QTextEdit(self.centralwidget)
        self.TxtDescripcion.setGeometry(QtCore.QRect(170, 180, 201, 71))
        self.TxtDescripcion.setObjectName(_fromUtf8("TxtDescripcion"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 70, 21, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 260, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Tejidos.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Tejidos)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Tejidos.setStatusBar(self.statusbar)

        self.retranslateUi(Tejidos)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtNombre.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtDescripcion.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_2.click)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Tejidos.Guardar)
        QtCore.QMetaObject.connectSlotsByName(Tejidos)

    def retranslateUi(self, Tejidos):
        Tejidos.setWindowTitle(_translate("Tejidos", "Tejidos", None))
        self.pushButton_2.setText(_translate("Tejidos", "Limpiar", None))
        self.label.setText(_translate("Tejidos", "Nombre", None))
        self.radioButton.setText(_translate("Tejidos", "Tejido", None))
        self.radioButton_2.setText(_translate("Tejidos", "Carcaza", None))
        self.radioButton_3.setText(_translate("Tejidos", "ADN", None))
        self.comboBox.setItemText(0, _translate("Tejidos", "Seleccionar", None))
        self.comboBox.setItemText(1, _translate("Tejidos", "Músculo Pectoral", None))
        self.comboBox.setItemText(2, _translate("Tejidos", "Higado", None))
        self.comboBox.setItemText(3, _translate("Tejidos", "Corazón", None))
        self.label_2.setText(_translate("Tejidos", "MYR", None))
        self.pushButton.setText(_translate("Tejidos", "Guardar", None))

