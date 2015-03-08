# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Busqueda.ui'
#
# Created: Tue Dec 09 10:23:13 2014
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

class Ui_PanelDeBusqueda(object):
    def setupUi(self, PanelDeBusqueda):
        PanelDeBusqueda.setObjectName(_fromUtf8("PanelDeBusqueda"))
        PanelDeBusqueda.resize(661, 550)
        PanelDeBusqueda.setMinimumSize(QtCore.QSize(661, 550))
        PanelDeBusqueda.setMaximumSize(QtCore.QSize(661, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../10808257_892502220760807_508259266_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PanelDeBusqueda.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(PanelDeBusqueda)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 490, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.TablaGeneral = QtGui.QTableWidget(self.centralwidget)
        self.TablaGeneral.setGeometry(QtCore.QRect(20, 230, 621, 251))
        self.TablaGeneral.setObjectName(_fromUtf8("TablaGeneral"))
        self.TablaGeneral.setColumnCount(0)
        self.TablaGeneral.setRowCount(0)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 621, 191))
        self.groupBox.setMinimumSize(QtCore.QSize(621, 191))
        self.groupBox.setMaximumSize(QtCore.QSize(621, 191))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 170, 221, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 40, 121, 21))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 70, 131, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 100, 111, 17))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 130, 101, 17))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.TxtBNombre = QtGui.QLineEdit(self.groupBox)
        self.TxtBNombre.setEnabled(False)
        self.TxtBNombre.setGeometry(QtCore.QRect(210, 40, 391, 20))
        self.TxtBNombre.setObjectName(_fromUtf8("TxtBNombre"))
        self.TxtBDpto = QtGui.QLineEdit(self.groupBox)
        self.TxtBDpto.setEnabled(False)
        self.TxtBDpto.setGeometry(QtCore.QRect(210, 70, 391, 20))
        self.TxtBDpto.setObjectName(_fromUtf8("TxtBDpto"))
        self.TxtBSub = QtGui.QLineEdit(self.groupBox)
        self.TxtBSub.setEnabled(False)
        self.TxtBSub.setGeometry(QtCore.QRect(210, 100, 391, 20))
        self.TxtBSub.setObjectName(_fromUtf8("TxtBSub"))
        self.TxtBCol = QtGui.QLineEdit(self.groupBox)
        self.TxtBCol.setEnabled(False)
        self.TxtBCol.setGeometry(QtCore.QRect(210, 130, 391, 20))
        self.TxtBCol.setObjectName(_fromUtf8("TxtBCol"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 160, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(260, 170, 191, 17))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 661, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 490, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 500, 161, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        PanelDeBusqueda.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(PanelDeBusqueda)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PanelDeBusqueda.setStatusBar(self.statusbar)

        self.retranslateUi(PanelDeBusqueda)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), PanelDeBusqueda.Volver)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), PanelDeBusqueda.BusquedaEspecifica)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TablaGeneral.clear)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), PanelDeBusqueda.BNombre)
        QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), PanelDeBusqueda.BDepartamento)
        QtCore.QObject.connect(self.radioButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), PanelDeBusqueda.BSubespecie)
        QtCore.QObject.connect(self.radioButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), PanelDeBusqueda.BColector)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtBCol.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtBSub.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtBDpto.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtBNombre.clear)
        QtCore.QObject.connect(self.radioButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), PanelDeBusqueda.VerEstado)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TablaGeneral.clear)
        QtCore.QMetaObject.connectSlotsByName(PanelDeBusqueda)

    def retranslateUi(self, PanelDeBusqueda):
        PanelDeBusqueda.setWindowTitle(_translate("PanelDeBusqueda", "Panel De Busqueda", None))
        self.pushButton.setText(_translate("PanelDeBusqueda", "Volver", None))
        self.groupBox.setTitle(_translate("PanelDeBusqueda", "BUSCAR", None))
        self.radioButton.setText(_translate("PanelDeBusqueda", "Ir a busqueda especifica", None))
        self.radioButton_2.setText(_translate("PanelDeBusqueda", "Nombre", None))
        self.radioButton_3.setText(_translate("PanelDeBusqueda", "Departamento", None))
        self.radioButton_4.setText(_translate("PanelDeBusqueda", "Subespecie", None))
        self.radioButton_5.setText(_translate("PanelDeBusqueda", "Colector", None))
        self.pushButton_2.setText(_translate("PanelDeBusqueda", "Limpiar", None))
        self.radioButton_6.setText(_translate("PanelDeBusqueda", "Consultar Por Estado", None))
        self.label.setText(_translate("PanelDeBusqueda", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#0000ff;\">Busqueda</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("PanelDeBusqueda", "Limpiar", None))
        self.label_4.setText(_translate("PanelDeBusqueda", "Universidad de los Llanos 2014 ®", None))

