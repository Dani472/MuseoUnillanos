# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificarIngresar.ui'
#
# Created: Sun Nov 30 14:34:29 2014
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

class Ui_IngresarGeneral(object):
    def setupUi(self, IngresarGeneral):
        IngresarGeneral.setObjectName(_fromUtf8("IngresarGeneral"))
        IngresarGeneral.resize(960, 474)
        IngresarGeneral.setMinimumSize(QtCore.QSize(960, 474))
        IngresarGeneral.setMaximumSize(QtCore.QSize(960, 474))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../a.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        IngresarGeneral.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(IngresarGeneral)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 961, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("High Tower Text"))
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 281, 371))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.TxtColeccion = QtGui.QLineEdit(self.groupBox)
        self.TxtColeccion.setGeometry(QtCore.QRect(150, 50, 113, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setItalic(False)
        self.TxtColeccion.setFont(font)
        self.TxtColeccion.setObjectName(_fromUtf8("TxtColeccion"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.TxtClase = QtGui.QLineEdit(self.groupBox)
        self.TxtClase.setGeometry(QtCore.QRect(150, 90, 113, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setItalic(False)
        self.TxtClase.setFont(font)
        self.TxtClase.setObjectName(_fromUtf8("TxtClase"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.TxtOrden = QtGui.QLineEdit(self.groupBox)
        self.TxtOrden.setGeometry(QtCore.QRect(150, 130, 113, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setItalic(False)
        self.TxtOrden.setFont(font)
        self.TxtOrden.setObjectName(_fromUtf8("TxtOrden"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.TxtFamilia = QtGui.QLineEdit(self.groupBox)
        self.TxtFamilia.setGeometry(QtCore.QRect(150, 170, 113, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setItalic(False)
        self.TxtFamilia.setFont(font)
        self.TxtFamilia.setObjectName(_fromUtf8("TxtFamilia"))
        self.TxtEspecie = QtGui.QLineEdit(self.groupBox)
        self.TxtEspecie.setGeometry(QtCore.QRect(150, 250, 113, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setItalic(False)
        self.TxtEspecie.setFont(font)
        self.TxtEspecie.setObjectName(_fromUtf8("TxtEspecie"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 111, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.TxtGenero = QtGui.QLineEdit(self.groupBox)
        self.TxtGenero.setGeometry(QtCore.QRect(150, 210, 113, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setItalic(False)
        self.TxtGenero.setFont(font)
        self.TxtGenero.setObjectName(_fromUtf8("TxtGenero"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.TxtSubespecie = QtGui.QLineEdit(self.groupBox)
        self.TxtSubespecie.setGeometry(QtCore.QRect(150, 290, 113, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setItalic(False)
        self.TxtSubespecie.setFont(font)
        self.TxtSubespecie.setObjectName(_fromUtf8("TxtSubespecie"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 290, 111, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 340, 81, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(11)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 420, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 420, 75, 23))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 40, 321, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 340, 81, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(11)
        font.setItalic(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.TxtNombre = QtGui.QLineEdit(self.groupBox_2)
        self.TxtNombre.setGeometry(QtCore.QRect(180, 40, 131, 20))
        self.TxtNombre.setObjectName(_fromUtf8("TxtNombre"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 81, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.TxtPeso = QtGui.QLineEdit(self.groupBox_2)
        self.TxtPeso.setGeometry(QtCore.QRect(180, 70, 131, 20))
        self.TxtPeso.setObjectName(_fromUtf8("TxtPeso"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 110, 46, 13))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(178, 100, 131, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(20, 140, 141, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.TxtFecha = QtGui.QLineEdit(self.groupBox_2)
        self.TxtFecha.setGeometry(QtCore.QRect(180, 140, 131, 20))
        self.TxtFecha.setWhatsThis(_fromUtf8(""))
        self.TxtFecha.setObjectName(_fromUtf8("TxtFecha"))
        self.TxtEstado = QtGui.QLineEdit(self.groupBox_2)
        self.TxtEstado.setGeometry(QtCore.QRect(180, 170, 131, 20))
        self.TxtEstado.setObjectName(_fromUtf8("TxtEstado"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(20, 170, 141, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.TxtMetodo = QtGui.QLineEdit(self.groupBox_2)
        self.TxtMetodo.setGeometry(QtCore.QRect(180, 200, 131, 20))
        self.TxtMetodo.setObjectName(_fromUtf8("TxtMetodo"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(20, 200, 151, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(20, 240, 151, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(20, 290, 151, 21))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.TxtHabitat = QtGui.QPlainTextEdit(self.groupBox_2)
        self.TxtHabitat.setGeometry(QtCore.QRect(180, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Serif"))
        font.setPointSize(9)
        font.setItalic(False)
        self.TxtHabitat.setFont(font)
        self.TxtHabitat.setObjectName(_fromUtf8("TxtHabitat"))
        self.Txtanotaciones = QtGui.QPlainTextEdit(self.groupBox_2)
        self.Txtanotaciones.setGeometry(QtCore.QRect(180, 290, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Serif"))
        font.setPointSize(9)
        font.setItalic(False)
        self.Txtanotaciones.setFont(font)
        self.Txtanotaciones.setObjectName(_fromUtf8("Txtanotaciones"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(630, 130, 321, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(30, 40, 46, 13))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(30, 70, 111, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(30, 100, 101, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(30, 130, 101, 21))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(30, 160, 101, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(30, 220, 101, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 250, 81, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(11)
        font.setItalic(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_23 = QtGui.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(30, 190, 121, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.TxtVereda = QtGui.QLineEdit(self.groupBox_3)
        self.TxtVereda.setGeometry(QtCore.QRect(190, 220, 113, 20))
        self.TxtVereda.setObjectName(_fromUtf8("TxtVereda"))
        self.TxtAltitud = QtGui.QLineEdit(self.groupBox_3)
        self.TxtAltitud.setGeometry(QtCore.QRect(190, 190, 113, 20))
        self.TxtAltitud.setObjectName(_fromUtf8("TxtAltitud"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 40, 121, 22))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_3.setEnabled(False)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 70, 121, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_4.setEnabled(False)
        self.comboBox_4.setGeometry(QtCore.QRect(190, 100, 121, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.TxtLongitudGrados = QtGui.QLineEdit(self.groupBox_3)
        self.TxtLongitudGrados.setGeometry(QtCore.QRect(190, 130, 21, 20))
        self.TxtLongitudGrados.setObjectName(_fromUtf8("TxtLongitudGrados"))
        self.TxtLongitudMinutos = QtGui.QLineEdit(self.groupBox_3)
        self.TxtLongitudMinutos.setGeometry(QtCore.QRect(230, 130, 21, 20))
        self.TxtLongitudMinutos.setObjectName(_fromUtf8("TxtLongitudMinutos"))
        self.TxtLongitudSegundos = QtGui.QLineEdit(self.groupBox_3)
        self.TxtLongitudSegundos.setGeometry(QtCore.QRect(270, 130, 21, 20))
        self.TxtLongitudSegundos.setObjectName(_fromUtf8("TxtLongitudSegundos"))
        self.TxtLatitudMinutos = QtGui.QLineEdit(self.groupBox_3)
        self.TxtLatitudMinutos.setGeometry(QtCore.QRect(230, 160, 21, 20))
        self.TxtLatitudMinutos.setObjectName(_fromUtf8("TxtLatitudMinutos"))
        self.TxtLatitudSegundos = QtGui.QLineEdit(self.groupBox_3)
        self.TxtLatitudSegundos.setGeometry(QtCore.QRect(270, 160, 21, 20))
        self.TxtLatitudSegundos.setObjectName(_fromUtf8("TxtLatitudSegundos"))
        self.TxtLatitudGrados = QtGui.QLineEdit(self.groupBox_3)
        self.TxtLatitudGrados.setGeometry(QtCore.QRect(190, 160, 21, 20))
        self.TxtLatitudGrados.setObjectName(_fromUtf8("TxtLatitudGrados"))
        self.label_24 = QtGui.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(250, 130, 16, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(250, 160, 16, 16))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(290, 130, 16, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.groupBox_3)
        self.label_27.setGeometry(QtCore.QRect(290, 160, 16, 16))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.groupBox_3)
        self.label_28.setGeometry(QtCore.QRect(210, 130, 16, 16))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(210, 160, 16, 16))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 420, 75, 23))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(630, 39, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.TxtRutaImagen = QtGui.QLineEdit(self.groupBox_4)
        self.TxtRutaImagen.setGeometry(QtCore.QRect(170, 40, 141, 20))
        self.TxtRutaImagen.setObjectName(_fromUtf8("TxtRutaImagen"))
        self.label_30 = QtGui.QLabel(self.groupBox_4)
        self.label_30.setGeometry(QtCore.QRect(20, 40, 141, 21))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        IngresarGeneral.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(IngresarGeneral)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        IngresarGeneral.setStatusBar(self.statusbar)

        self.retranslateUi(IngresarGeneral)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtSubespecie.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtEspecie.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtGenero.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtFamilia.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtOrden.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtClase.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtColeccion.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), IngresarGeneral.Guardar)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), IngresarGeneral.Volver)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Txtanotaciones.clear)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtHabitat.clear)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtMetodo.clear)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtEstado.clear)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtFecha.clear)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtPeso.clear)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtNombre.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pushButton_4.setDisabled)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtVereda.clear)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtAltitud.clear)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtLatitudGrados.clear)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtLatitudMinutos.clear)
        QtCore.QObject.connect(self.groupBox_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtLatitudSegundos.clear)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtLongitudSegundos.clear)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtLongitudMinutos.clear)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtLongitudGrados.clear)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), IngresarGeneral.Continuar)
        QtCore.QObject.connect(self.comboBox_3, QtCore.SIGNAL(_fromUtf8("activated(QString)")), IngresarGeneral.LlenarMunicipio)
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("activated(QString)")), IngresarGeneral.LlenarDpto)
        QtCore.QObject.connect(self.comboBox_4, QtCore.SIGNAL(_fromUtf8("activated(QString)")), IngresarGeneral.Municipio)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_7.click)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_5.click)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_2.click)
        QtCore.QMetaObject.connectSlotsByName(IngresarGeneral)
        IngresarGeneral.setTabOrder(self.TxtColeccion, self.TxtClase)
        IngresarGeneral.setTabOrder(self.TxtClase, self.TxtOrden)
        IngresarGeneral.setTabOrder(self.TxtOrden, self.TxtFamilia)
        IngresarGeneral.setTabOrder(self.TxtFamilia, self.TxtGenero)
        IngresarGeneral.setTabOrder(self.TxtGenero, self.TxtEspecie)
        IngresarGeneral.setTabOrder(self.TxtEspecie, self.TxtSubespecie)
        IngresarGeneral.setTabOrder(self.TxtSubespecie, self.pushButton_2)
        IngresarGeneral.setTabOrder(self.pushButton_2, self.TxtNombre)
        IngresarGeneral.setTabOrder(self.TxtNombre, self.TxtPeso)
        IngresarGeneral.setTabOrder(self.TxtPeso, self.comboBox)
        IngresarGeneral.setTabOrder(self.comboBox, self.TxtFecha)
        IngresarGeneral.setTabOrder(self.TxtFecha, self.TxtEstado)
        IngresarGeneral.setTabOrder(self.TxtEstado, self.TxtMetodo)
        IngresarGeneral.setTabOrder(self.TxtMetodo, self.TxtHabitat)
        IngresarGeneral.setTabOrder(self.TxtHabitat, self.Txtanotaciones)
        IngresarGeneral.setTabOrder(self.Txtanotaciones, self.pushButton_5)
        IngresarGeneral.setTabOrder(self.pushButton_5, self.TxtRutaImagen)
        IngresarGeneral.setTabOrder(self.TxtRutaImagen, self.comboBox_2)
        IngresarGeneral.setTabOrder(self.comboBox_2, self.comboBox_3)
        IngresarGeneral.setTabOrder(self.comboBox_3, self.comboBox_4)
        IngresarGeneral.setTabOrder(self.comboBox_4, self.TxtLongitudGrados)
        IngresarGeneral.setTabOrder(self.TxtLongitudGrados, self.TxtLongitudMinutos)
        IngresarGeneral.setTabOrder(self.TxtLongitudMinutos, self.TxtLongitudSegundos)
        IngresarGeneral.setTabOrder(self.TxtLongitudSegundos, self.TxtLatitudGrados)
        IngresarGeneral.setTabOrder(self.TxtLatitudGrados, self.TxtLatitudMinutos)
        IngresarGeneral.setTabOrder(self.TxtLatitudMinutos, self.TxtLatitudSegundos)
        IngresarGeneral.setTabOrder(self.TxtLatitudSegundos, self.TxtAltitud)
        IngresarGeneral.setTabOrder(self.TxtAltitud, self.TxtVereda)
        IngresarGeneral.setTabOrder(self.TxtVereda, self.pushButton_7)
        IngresarGeneral.setTabOrder(self.pushButton_7, self.pushButton_3)
        IngresarGeneral.setTabOrder(self.pushButton_3, self.pushButton_4)
        IngresarGeneral.setTabOrder(self.pushButton_4, self.pushButton)

    def retranslateUi(self, IngresarGeneral):
        IngresarGeneral.setWindowTitle(_translate("IngresarGeneral", "Modificar - Ingresar", None))
        self.label_5.setText(_translate("IngresarGeneral", "<html><head/><body><p><span style=\" color:#ff0000;\">Museo Natural Universidad de los Llanos</span></p></body></html>", None))
        self.groupBox.setTitle(_translate("IngresarGeneral", "Generalidades", None))
        self.label.setText(_translate("IngresarGeneral", "Colección", None))
        self.label_2.setText(_translate("IngresarGeneral", "Clase", None))
        self.label_3.setText(_translate("IngresarGeneral", "Orden", None))
        self.label_4.setText(_translate("IngresarGeneral", "Especie", None))
        self.label_6.setText(_translate("IngresarGeneral", "Familia", None))
        self.label_7.setText(_translate("IngresarGeneral", "Genero", None))
        self.label_8.setText(_translate("IngresarGeneral", "Subespecie", None))
        self.pushButton_2.setText(_translate("IngresarGeneral", "Limpiar", None))
        self.pushButton.setText(_translate("IngresarGeneral", "Volver", None))
        self.pushButton_3.setText(_translate("IngresarGeneral", "Guardar", None))
        self.groupBox_2.setTitle(_translate("IngresarGeneral", "Generalidades", None))
        self.pushButton_5.setText(_translate("IngresarGeneral", "Limpiar", None))
        self.label_9.setText(_translate("IngresarGeneral", "Nombre", None))
        self.label_10.setText(_translate("IngresarGeneral", "Peso (g)", None))
        self.label_11.setText(_translate("IngresarGeneral", "Sexo", None))
        self.comboBox.setItemText(0, _translate("IngresarGeneral", "Indeterminado", None))
        self.comboBox.setItemText(1, _translate("IngresarGeneral", "Macho", None))
        self.comboBox.setItemText(2, _translate("IngresarGeneral", "Hembra", None))
        self.label_12.setText(_translate("IngresarGeneral", "Fecha de coleccion", None))
        self.label_13.setText(_translate("IngresarGeneral", "Estado actual", None))
        self.label_14.setText(_translate("IngresarGeneral", "Metodo de coleccion", None))
        self.label_15.setText(_translate("IngresarGeneral", "Habitat", None))
        self.label_16.setText(_translate("IngresarGeneral", "anotaciones", None))
        self.groupBox_3.setTitle(_translate("IngresarGeneral", "Localizacion", None))
        self.label_17.setText(_translate("IngresarGeneral", "Pais", None))
        self.label_18.setText(_translate("IngresarGeneral", "Departamento", None))
        self.label_19.setText(_translate("IngresarGeneral", "Municipio", None))
        self.label_20.setText(_translate("IngresarGeneral", "Longitud", None))
        self.label_21.setText(_translate("IngresarGeneral", "Latitud", None))
        self.label_22.setText(_translate("IngresarGeneral", "Vereda", None))
        self.pushButton_7.setText(_translate("IngresarGeneral", "Limpiar", None))
        self.label_23.setText(_translate("IngresarGeneral", "Altitud (Metros)", None))
        self.label_24.setText(_translate("IngresarGeneral", "\'", None))
        self.label_25.setText(_translate("IngresarGeneral", "\'", None))
        self.label_26.setText(_translate("IngresarGeneral", "\'\'", None))
        self.label_27.setText(_translate("IngresarGeneral", "\'\'", None))
        self.label_28.setText(_translate("IngresarGeneral", "°", None))
        self.label_29.setText(_translate("IngresarGeneral", "°", None))
        self.pushButton_4.setText(_translate("IngresarGeneral", "Continuar", None))
        self.groupBox_4.setTitle(_translate("IngresarGeneral", "Imagen", None))
        self.label_30.setText(_translate("IngresarGeneral", "Ruta de la imagen", None))
