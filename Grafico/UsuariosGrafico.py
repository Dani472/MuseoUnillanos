# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Usuarios.ui'
#
# Created: Sat Nov 29 12:37:01 2014
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

class Ui_Usuarios(object):
    def setupUi(self, Usuarios):
        Usuarios.setObjectName(_fromUtf8("Usuarios"))
        Usuarios.resize(590, 410)
        Usuarios.setMinimumSize(QtCore.QSize(590, 410))
        Usuarios.setMaximumSize(QtCore.QSize(590, 410))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../10808257_892502220760807_508259266_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Usuarios.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Usuarios)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 360, 161, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 571, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("High Tower Text"))
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 360, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 271, 251))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(220, 300, 261, 311))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 30, 271, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 271, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 121, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 131, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 140, 121, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 220, 141, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.TxtNombreUser = QtGui.QLineEdit(self.frame)
        self.TxtNombreUser.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.TxtNombreUser.setObjectName(_fromUtf8("TxtNombreUser"))
        self.TxtPassNueva = QtGui.QLineEdit(self.frame)
        self.TxtPassNueva.setGeometry(QtCore.QRect(150, 140, 113, 20))
        self.TxtPassNueva.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtPassNueva.setObjectName(_fromUtf8("TxtPassNueva"))
        self.TxtRepetirPass = QtGui.QLineEdit(self.frame)
        self.TxtRepetirPass.setGeometry(QtCore.QRect(150, 180, 113, 20))
        self.TxtRepetirPass.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtRepetirPass.setObjectName(_fromUtf8("TxtRepetirPass"))
        self.TxtPassadmin = QtGui.QLineEdit(self.frame)
        self.TxtPassadmin.setGeometry(QtCore.QRect(150, 220, 113, 20))
        self.TxtPassadmin.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtPassadmin.setObjectName(_fromUtf8("TxtPassadmin"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(290, 40, 281, 251))
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(220, 300, 261, 311))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(0, 30, 281, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_10 = QtGui.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 100, 121, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 130, 121, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 160, 131, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(10, 190, 121, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(10, 220, 131, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.TxtUserNew = QtGui.QLineEdit(self.frame_3)
        self.TxtUserNew.setGeometry(QtCore.QRect(160, 100, 113, 20))
        self.TxtUserNew.setObjectName(_fromUtf8("TxtUserNew"))
        self.TxtPassNew = QtGui.QLineEdit(self.frame_3)
        self.TxtPassNew.setGeometry(QtCore.QRect(160, 130, 113, 20))
        self.TxtPassNew.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtPassNew.setObjectName(_fromUtf8("TxtPassNew"))
        self.TxtRepetirNew = QtGui.QLineEdit(self.frame_3)
        self.TxtRepetirNew.setGeometry(QtCore.QRect(160, 160, 113, 20))
        self.TxtRepetirNew.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtRepetirNew.setObjectName(_fromUtf8("TxtRepetirNew"))
        self.TxtTipoUser = QtGui.QLineEdit(self.frame_3)
        self.TxtTipoUser.setGeometry(QtCore.QRect(160, 190, 113, 20))
        self.TxtTipoUser.setObjectName(_fromUtf8("TxtTipoUser"))
        self.TxtPassadmin_2 = QtGui.QLineEdit(self.frame_3)
        self.TxtPassadmin_2.setGeometry(QtCore.QRect(160, 220, 113, 20))
        self.TxtPassadmin_2.setEchoMode(QtGui.QLineEdit.Password)
        self.TxtPassadmin_2.setObjectName(_fromUtf8("TxtPassadmin_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 360, 91, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 320, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.BLimpiarCambio = QtGui.QPushButton(self.centralwidget)
        self.BLimpiarCambio.setGeometry(QtCore.QRect(120, 320, 75, 23))
        self.BLimpiarCambio.setObjectName(_fromUtf8("BLimpiarCambio"))
        self.BLimpiarNew = QtGui.QPushButton(self.centralwidget)
        self.BLimpiarNew.setGeometry(QtCore.QRect(410, 320, 75, 23))
        self.BLimpiarNew.setObjectName(_fromUtf8("BLimpiarNew"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 320, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        Usuarios.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Usuarios)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Usuarios.setStatusBar(self.statusbar)

        self.retranslateUi(Usuarios)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Usuarios.EliminarUser)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Usuarios.Volver)
        QtCore.QObject.connect(self.BLimpiarNew, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtUserNew.clear)
        QtCore.QObject.connect(self.BLimpiarNew, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtRepetirNew.clear)
        QtCore.QObject.connect(self.BLimpiarNew, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtPassNew.clear)
        QtCore.QObject.connect(self.BLimpiarNew, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtPassadmin_2.clear)
        QtCore.QObject.connect(self.BLimpiarCambio, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtNombreUser.clear)
        QtCore.QObject.connect(self.BLimpiarCambio, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtPassadmin.clear)
        QtCore.QObject.connect(self.BLimpiarCambio, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtRepetirPass.clear)
        QtCore.QObject.connect(self.BLimpiarCambio, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TxtPassNueva.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Usuarios.ConfirmarCambio)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Usuarios.ConfirmarNuevo)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.BLimpiarNew.click)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.BLimpiarCambio.click)
        QtCore.QMetaObject.connectSlotsByName(Usuarios)
        Usuarios.setTabOrder(self.TxtNombreUser, self.TxtPassNueva)
        Usuarios.setTabOrder(self.TxtPassNueva, self.TxtRepetirPass)
        Usuarios.setTabOrder(self.TxtRepetirPass, self.TxtPassadmin)
        Usuarios.setTabOrder(self.TxtPassadmin, self.BLimpiarCambio)
        Usuarios.setTabOrder(self.BLimpiarCambio, self.TxtUserNew)
        Usuarios.setTabOrder(self.TxtUserNew, self.TxtPassNew)
        Usuarios.setTabOrder(self.TxtPassNew, self.TxtRepetirNew)
        Usuarios.setTabOrder(self.TxtRepetirNew, self.TxtTipoUser)
        Usuarios.setTabOrder(self.TxtTipoUser, self.TxtPassadmin_2)
        Usuarios.setTabOrder(self.TxtPassadmin_2, self.BLimpiarNew)
        Usuarios.setTabOrder(self.BLimpiarNew, self.pushButton)

    def retranslateUi(self, Usuarios):
        Usuarios.setWindowTitle(_translate("Usuarios", "Panel de Usuarios", None))
        self.label_4.setText(_translate("Usuarios", "Universidad de los Llanos 2014 ®", None))
        self.label_3.setText(_translate("Usuarios", "<html><head/><body><p align=\"center\"><span style=\" color:#5500ff;\">Control de Usuarios</span></p></body></html>", None))
        self.pushButton.setText(_translate("Usuarios", "Volver", None))
        self.label.setText(_translate("Usuarios", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Cambiar Contraseña</span></p></body></html>", None))
        self.label_2.setText(_translate("Usuarios", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Cambiar Contraseña</span></p></body></html>", None))
        self.label_6.setText(_translate("Usuarios", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nombre de usuario</span></p></body></html>", None))
        self.label_7.setText(_translate("Usuarios", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Repetir Contraseña</span></p></body></html>", None))
        self.label_8.setText(_translate("Usuarios", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Contraseña nueva</span></p></body></html>", None))
        self.label_9.setText(_translate("Usuarios", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Contraseña de admin</span></p></body></html>", None))
        self.label_5.setText(_translate("Usuarios", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Nuevo Usuario</span></p></body></html>", None))
        self.label_10.setText(_translate("Usuarios", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nombre de usuario</span></p></body></html>", None))
        self.label_11.setText(_translate("Usuarios", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Contraseña</span></p></body></html>", None))
        self.label_12.setText(_translate("Usuarios", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Repetir Contraseña</span></p></body></html>", None))
        self.label_13.setText(_translate("Usuarios", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo Usuario</span></p></body></html>", None))
        self.label_14.setText(_translate("Usuarios", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Contraseña admin</span></p></body></html>", None))
        self.TxtTipoUser.setText(_translate("Usuarios", "INVITADO", None))
        self.pushButton_2.setText(_translate("Usuarios", "Borrar Usuario", None))
        self.pushButton_3.setText(_translate("Usuarios", "Confirmar", None))
        self.BLimpiarCambio.setText(_translate("Usuarios", "Limpiar", None))
        self.BLimpiarNew.setText(_translate("Usuarios", "Limpiar", None))
        self.pushButton_4.setText(_translate("Usuarios", "Confirmar", None))
