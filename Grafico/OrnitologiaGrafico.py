# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ornitologia.ui'
#
# Created: Fri Dec 05 17:47:57 2014
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

class Ui_Ornitologia(object):
    def setupUi(self, Ornitologia):
        Ornitologia.setObjectName(_fromUtf8("Ornitologia"))
        Ornitologia.resize(646, 440)
        Ornitologia.setMinimumSize(QtCore.QSize(646, 440))
        Ornitologia.setMaximumSize(QtCore.QSize(646, 440))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../10808257_892502220760807_508259266_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ornitologia.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Ornitologia)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(-10, -10, 651, 431))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("High Tower Text"))
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Fondos/10836275_904791479531881_93460058_n.jpg")))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 390, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 611, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.TxtEdad = QtGui.QLineEdit(self.groupBox)
        self.TxtEdad.setGeometry(QtCore.QRect(140, 40, 113, 20))
        self.TxtEdad.setObjectName(_fromUtf8("TxtEdad"))
        self.TxtEnvergadura = QtGui.QLineEdit(self.groupBox)
        self.TxtEnvergadura.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.TxtEnvergadura.setObjectName(_fromUtf8("TxtEnvergadura"))
        self.TxtGrasa = QtGui.QLineEdit(self.groupBox)
        self.TxtGrasa.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.TxtGrasa.setObjectName(_fromUtf8("TxtGrasa"))
        self.TxtMuda = QtGui.QTextEdit(self.groupBox)
        self.TxtMuda.setGeometry(QtCore.QRect(140, 210, 111, 71))
        self.TxtMuda.setTabStopWidth(20)
        self.TxtMuda.setObjectName(_fromUtf8("TxtMuda"))
        self.TxtContenidoEstomacal = QtGui.QTextEdit(self.groupBox)
        self.TxtContenidoEstomacal.setGeometry(QtCore.QRect(450, 30, 141, 51))
        self.TxtContenidoEstomacal.setObjectName(_fromUtf8("TxtContenidoEstomacal"))
        self.TxtPartesBlandas = QtGui.QTextEdit(self.groupBox)
        self.TxtPartesBlandas.setGeometry(QtCore.QRect(450, 100, 141, 51))
        self.TxtPartesBlandas.setObjectName(_fromUtf8("TxtPartesBlandas"))
        self.TxtReproduccion = QtGui.QTextEdit(self.groupBox)
        self.TxtReproduccion.setGeometry(QtCore.QRect(450, 170, 141, 51))
        self.TxtReproduccion.setObjectName(_fromUtf8("TxtReproduccion"))
        self.TxtOscificacion = QtGui.QLineEdit(self.groupBox)
        self.TxtOscificacion.setGeometry(QtCore.QRect(140, 160, 113, 20))
        self.TxtOscificacion.setObjectName(_fromUtf8("TxtOscificacion"))
        self.TxtGonodas = QtGui.QTextEdit(self.groupBox)
        self.TxtGonodas.setGeometry(QtCore.QRect(450, 240, 141, 51))
        self.TxtGonodas.setObjectName(_fromUtf8("TxtGonodas"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 390, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        Ornitologia.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Ornitologia)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Ornitologia.setStatusBar(self.statusbar)

        self.retranslateUi(Ornitologia)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Ornitologia.Guardar)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_2.click)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtReproduccion.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtPartesBlandas.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtGrasa.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtEdad.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtEnvergadura.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtMuda.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtContenidoEstomacal.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtGonodas.clear)
        QtCore.QMetaObject.connectSlotsByName(Ornitologia)

    def retranslateUi(self, Ornitologia):
        Ornitologia.setWindowTitle(_translate("Ornitologia", "Ornitologia", None))
        self.pushButton.setText(_translate("Ornitologia", "Guardar", None))
        self.pushButton_2.setText(_translate("Ornitologia", "Limpiar", None))

