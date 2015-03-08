# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VerEstado.ui'
#
# Created: Tue Dec 09 10:23:23 2014
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

class Ui_ViewEstado(object):
    def setupUi(self, ViewEstado):
        ViewEstado.setObjectName(_fromUtf8("ViewEstado"))
        ViewEstado.resize(474, 451)
        ViewEstado.setMinimumSize(QtCore.QSize(474, 451))
        ViewEstado.setMaximumSize(QtCore.QSize(474, 451))
        self.centralwidget = QtGui.QWidget(ViewEstado)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 400, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.TablaGeneral = QtGui.QTableWidget(self.centralwidget)
        self.TablaGeneral.setGeometry(QtCore.QRect(20, 170, 431, 221))
        self.TablaGeneral.setObjectName(_fromUtf8("TablaGeneral"))
        self.TablaGeneral.setColumnCount(0)
        self.TablaGeneral.setRowCount(0)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 431, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 131, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 141, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.TxtCodigo = QtGui.QLineEdit(self.groupBox)
        self.TxtCodigo.setGeometry(QtCore.QRect(290, 50, 113, 20))
        self.TxtCodigo.setObjectName(_fromUtf8("TxtCodigo"))
        self.BoxEstado = QtGui.QComboBox(self.groupBox)
        self.BoxEstado.setGeometry(QtCore.QRect(240, 80, 121, 22))
        self.BoxEstado.setObjectName(_fromUtf8("BoxEstado"))
        self.BoxEstado.addItem(_fromUtf8(""))
        self.BoxEstado.addItem(_fromUtf8(""))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(190, 50, 82, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 401, 20))
        self.label.setObjectName(_fromUtf8("label"))
        ViewEstado.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ViewEstado)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ViewEstado.setStatusBar(self.statusbar)

        self.retranslateUi(ViewEstado)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ViewEstado.Disponible)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), ViewEstado.NoDisponible)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ViewEstado.Volver)
        QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), ViewEstado.CambiarEstado)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TablaGeneral.clear)
        QtCore.QMetaObject.connectSlotsByName(ViewEstado)

    def retranslateUi(self, ViewEstado):
        ViewEstado.setWindowTitle(_translate("ViewEstado", "Consultar Por Estado", None))
        self.pushButton.setText(_translate("ViewEstado", "Volver", None))
        self.groupBox.setTitle(_translate("ViewEstado", "Estado del animal", None))
        self.radioButton.setText(_translate("ViewEstado", "Disponible ", None))
        self.radioButton_2.setText(_translate("ViewEstado", "No Disponible", None))
        self.label_2.setText(_translate("ViewEstado", "Cambiar estado", None))
        self.BoxEstado.setItemText(0, _translate("ViewEstado", "Disponible", None))
        self.BoxEstado.setItemText(1, _translate("ViewEstado", "no Disponible", None))
        self.radioButton_3.setText(_translate("ViewEstado", "Codigo", None))
        self.label.setText(_translate("ViewEstado", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">Consulta</span></p></body></html>", None))

