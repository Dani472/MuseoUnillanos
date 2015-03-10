# -*- coding: UTF-8 -*-
#Museo Natural de Historia Universidad de los Llanos
#Ingenieria de Sistemas 2014
#Implementar la conexcion y peticiones en una clase independiente



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
  
from PyQt4.QtGui import *
import sys
import MySQLdb 
import os
import time
sys.path.append('..') 
from Grafico.VerEstadoGrafico import Ui_ViewEstado
from Grafico.VerAportesGrafico import Ui_AportesUser
from Grafico.AportesGrafico import Ui_Aportes
from Grafico.BusquedaPersonalizadaGrafico import Ui_BusquedaPersonalizada
from Grafico.BackupGrafico import Ui_Backup
from Grafico.BusquedaGrafico import Ui_PanelDeBusqueda
from Grafico.TejidosGrafico import Ui_Tejidos
from Grafico.OrnitologiaGrafico import Ui_Ornitologia
from Grafico.ModificarIngresarGrafico import Ui_IngresarGeneral
from Grafico.MenuModificarInsertarGrafico import Ui_MenuModificar
from Grafico.EliminarUserGrafico import Ui_EliminarUser
from Grafico.UsuariosGrafico import Ui_Usuarios
from Grafico.CambioPassGrafico import Ui_CambioPass
from Grafico.MenuInvitadoGrafico import Ui_MenuInvitado
from Grafico.MenuAdministradorGrafico import Ui_Menuadmin
from Grafico.CreditosGrafico import Ui_Creditos
from Grafico.LoginGrafico import Ui_Login
      
class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
   
    def Ingreso(self):    
    	self.usuario = self.ui.TxtUsuario.text()
        self.clave = self.ui.TxtClave.text()
        host="localhost"
        userdb="Visualizar"
        passdb=""
        bdausar="mhnu"
        In="' or '1'='1' -- '"
        if self.usuario=="" or self.clave=="":
			QMessageBox.information(self,"Error","Usuario o clave vacios")
        if self.usuario==In or self.clave==In:
			QMessageBox.information(self,"Error","Codigo no permitido (Inyeccion SQL)")	
        Conuser="select * from usuarios where nomb_usuar='%s';"%self.usuario
        db=MySQLdb.connect(host,userdb,passdb,bdausar)
        curso=db.cursor()
        curso.execute(Conuser)
        InfoUser=curso.fetchone()
        db.close()
        try:
			self.ValidarUsuario(InfoUser[1],InfoUser[2],InfoUser[3])
        except:
			print""      
                
    def ValidarUsuario(self,user,passw,tipo):
		if user==self.usuario and passw==self.clave:
			if tipo=="ADMINISTRADOR":
				QMessageBox.information(self,"Mensaje","Bienvenid@ %s"%user,"Aceptar")
				self.ui.TxtUsuario.clear()
				self.ui.TxtClave.clear()
				Menuadmon.show()
				Log.close()
			if tipo=="INVITADO":
				QMessageBox.information(self,"Mensaje","Bienvenid@ %s"%user,"Aceptar")
				MenuInv.show()
				Log.close()
			if user==None:
				QMessageBox.information(self,"Error","Este usuario no existe")	
		else:
			QMessageBox.information(self,"Error","Usuario o clave incorrectos")	  		
			
		
    def Credito(self):
     	Cre.show()
     	Log.close()
    
    def TipoUsuario(self):
		print "Estructura"
     	   	     	
class Creditos (QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_Creditos()
		self.ui.setupUi(self)
		
			
	def Volver(self):
		Log.show()
		Cre.close()
		
class MenuInvitado(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_MenuInvitado()
		self.ui.setupUi(self)
	
	def Busqueda(self):
		Buscar.SaberQueMenuInvoco(2)
		Buscar.show()
		MenuInv.close()
	
	def aportes(self):
		Apor.show()
		MenuInv.close()
	
	def CambioPassInvitado(self):
		CambioP.show()
		MenuInv.close()
	
	def Salir(self):
		Log.show()
		MenuInv.close()

class Menuadmin(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_Menuadmin()
		self.ui.setupUi(self)
	
	def Busqueda (self):
		Buscar.SaberQueMenuInvoco(1)
		Buscar.show()
		Menuadmon.close()
	
	def Modificar(self):
		actualizar.show()
		Menuadmon.close()
	
	def Usuarios(self):
		Users.show()
		Menuadmon.close()
	
	def CambioPassadmin(self):
		CambioP.show()
		Menuadmon.close()
	
	def CopiaSeguridad(self):
		Copia.show()
		Menuadmon.close()
	
	def VerAportes(self):
		VAportes.show()
		Menuadmon.close()				
	
	def Salir(self):
		Log.show()
		Menuadmon.close()
		
class CambioPassword(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_CambioPass()
		self.ui.setupUi(self)
	
	
	def CambioDePass(self):
		Claveantigua = self.ui.TxtantiguaPass.text()
		NuevaClave = self.ui.TxtNuevaPass.text()
		RepetirNuevaClave = self.ui.TxtRepetirPass.text()
		cambio="update usuarios set clave='%s' where clave='%s';"%(NuevaClave,Claveantigua)
		if Claveantigua=="" or NuevaClave=="" or RepetirNuevaClave=="":
			QMessageBox.information(self,"Error","Campos vacios")
		else:
			if RepetirNuevaClave == NuevaClave:
				host="localhost"
				userdb="DM"
				passdb=""
				bdausar="mhnu"
				db=MySQLdb.connect(host,userdb,passdb,bdausar)
				curso=db.cursor()
				curso.execute(cambio)
				resultado=curso.fetchone()
				db.commit()
				db.close()
				QMessageBox.information(self,"Mensaje","Clave modificada con exito")
				Log.show()
				CambioP.close()
			else:
				QMessageBox.information(self,"Error","La clave no concuerdan")
				db.rollback()
				db.close()
		self.ui.TxtantiguaPass.clear()
		self.ui.TxtNuevaPass.clear()
		self.ui.TxtRepetirPass.clear()
				
			
	def Volver(self):
		Log.show()
		CambioP.close()

class ControlUsers(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_Usuarios()
		self.ui.setupUi(self)
		
	def EliminarUser(self):
		DeleteUser.show()
		Users.close()
		
	def ObtenerDatos(self):
		self.Passadmin = self.ui.TxtPassadmin.text()
		self.NombreUser = self.ui.TxtNombreUser.text()
		self.PassNueva = self.ui.TxtPassNueva.text()
		self.RepetirPass = self.ui.TxtRepetirPass.text()
		print"a", self.Passadmin
	
	def ConfirmarCambio(self):
		Users.ObtenerDatos()
		host="localhost"
		userdb="DM"
		passdb=""
		bdausar="mhnu"
		con="select * from usuarios where clave='%s';" % self.Passadmin
		cambio="update usuarios set clave='%s' where nomb_usuar='%s';"%(self.PassNueva,self.NombreUser)
		db=MySQLdb.connect(host,userdb,passdb,bdausar)
		curso=db.cursor()
		curso.execute(con)
		InfoUser=curso.fetchone()
		tipo=InfoUser[3]
		if tipo=="ADMINISTRADOR":
			if self.PassNueva==self.RepetirPass:
				db=MySQLdb.connect(host,userdb,passdb,bdausar)
				curso=db.cursor()
				curso.execute(cambio)
				InfoUser1=curso.fetchone()
				db.commit()
				db.close()
				QMessageBox.information(self,"Mensaje","Clave del usuario cambiada con exito")
				Menuadmon.show()
				Users.close()
			else:
				QMessageBox.information(self,"Error","Las claves no conciden")
				db.rollback()
				db.close()
		db.close()
		

	def ConfirmarNuevo(self):
		NewUser = self.ui.TxtUserNew.text()
		NewPass = self.ui.TxtPassNew.text()
		RepetirPass = self.ui.TxtRepetirNew.text()
		TipoUser = self.ui.TxtTipoUser.text() # Guardarlo en mayuscula con upper TipoUser.upper()
		Passadmon = self.ui.TxtPassadmin_2.text()
		tipo=str(TipoUser)
		tipo=tipo.upper()
		host="localhost"
		userdb="DM"
		passdb=""
		bdausar="mhnu"
		inserccion="insert into usuarios (nomb_usuar,clave,tipo_us) values ('%s','%s','%s');"%(NewUser,NewPass,tipo)
		if NewUser=="" or NewPass=="" or RepetirPass=="" or Passadmon=="":
			QMessageBox.information(self,"Error","Por favor llene todos los campos")
		else:
			comprobaradmin="select * from usuarios where clave='%s';"% Passadmon
			db=MySQLdb.connect(host,userdb,passdb,bdausar)
			curso=db.cursor()
			curso.execute(comprobaradmin)
			InfoUser=curso.fetchone()
			if InfoUser[3]=="ADMINISTRADOR":
				db=MySQLdb.connect(host,userdb,passdb,bdausar)
				curso=db.cursor()
				curso.execute(inserccion)
				InfoUser=curso.fetchone()
				db.commit()
				db.close()
				QMessageBox.information(self,"Mensaje","Usuario creado exitosamente")
				Menuadmon.show()
				Users.close()
			else:
				QMessageBox.information(self,"Error","Contraseña de administrador no valida")
			
	def Volver(self):
		Menuadmon.show()
		Users.close()
			
class EliminarUsuario(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_EliminarUser()
		self.ui.setupUi(self)
	
	def Confirmar(self):
		UserEliminar = self.ui.TxtUserEliminar.text()
		Passadministrador = self.ui.TxtPassadmin.text()
		if UserEliminar=="" or Passadministrador=="":
			QMessageBox.information(self,"Error","Campos vacios")
		else:
			DeleteUser.Eliminar(UserEliminar,Passadministrador)			
			
	def Eliminar(self,user,passw):
		host="localhost"
		userdb="DM"
		passdb=""
		bdausar="mhnu"
		con="select * from usuarios where clave='%s';" % passw
		delete="delete from usuarios where nomb_usuar='%s';"% user
		db=MySQLdb.connect(host,userdb,passdb,bdausar)
		curso=db.cursor()
		curso.execute(con)
		InfoUser=curso.fetchone()
		permisos=InfoUser[3]
		if permisos=="ADMINISTRADOR":
			db=MySQLdb.connect(host,userdb,passdb,bdausar)
			curso=db.cursor()
			curso.execute(delete)
			resultado=curso.fetchone()
			db.commit()
			db.close()
			QMessageBox.information(self,"Mensaje","Usuario eliminado con exito")
		else:
			QMessageBox.information(self,"Error","No se pudo eliminar el usuario")
			db.rollback()
			db.close()	
		db.close()
		CambioP.close()
		Menuadmon.show()
	
	def Volver(self):
		DeleteUser.close()
		Users.show()
		
class ModificarInfo(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_MenuModificar()
		self.ui.setupUi(self)
		
	def Ictiologica(self):
		Ingresar.show()
		Ingresar.CualContinua(1)
		actualizar.close()
		
	def Herpofologica(self):
		Ingresar.show()
		Ingresar.CualContinua(2)
		actualizar.close()
	
	def Ornitologica(self):
		Ingresar.show()
		Ingresar.CualContinua(3)
		actualizar.close()
	
	def Mustozoologica(self):
		Ingresar.show()
		Ingresar.CualContinua(4)
		actualizar.close()
		
	def Invertebrados(self):
		Ingresar.show()
		Ingresar.CualContinua(5)
		actualizar.close()
	
	def Tejidos(self):
		Ingresar.show()
		Ingresar.CualContinua(6)
		actualizar.close()
	
	def Volver(self):
		Menuadmon.show()
		actualizar.close()
		
class IngresarDatos(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_IngresarGeneral()
		self.ui.setupUi(self)		
		self.ui.comboBox_2.addItem("Seleccionar")
		self.ui.comboBox_2.addItem("Colombia")

	def CualContinua(self,especie):
		self.Esp=especie
	
	def LimpiarTodito(self):
		self.ui.TxtColeccion.clear()
		self.ui.TxtClase.clear()
		self.ui.TxtOrden.clear()
		self.ui.TxtFamilia.clear()
		self.ui.TxtGenero.clear()
		self.ui.TxtEspecie.clear()
		self.ui.TxtSubespecie.clear()
		
		self.ui.TxtNombre.clear()
		self.ui.TxtPeso.clear()
		self.ui.TxtFecha.clear()
		self.ui.TxtEstado.clear()
		self.ui.TxtMetodo.clear()
		self.ui.TxtHabitat.clear()
		self.ui.Txtanotaciones.clear() 
		self.ui.comboBox.clear()
		
		self.ui.TxtRutaImagen.clear()
		
		self.ui.TxtAltitud.clear()
		self.ui.TxtVereda.clear()
		self.ui.TxtLongitudGrados.clear()
		self.ui.TxtLongitudMinutos.clear()
		self.ui.TxtLongitudSegundos.clear()
		self.ui.TxtLatitudGrados.clear()
		self.ui.TxtLatitudMinutos.clear()
		self.ui.TxtLatitudSegundos.clear()
		
	def Guardar(self):
		Coleccion = str(self.ui.TxtColeccion.text())
		Clase = str(self.ui.TxtClase.text())
		Orden = str(self.ui.TxtOrden.text())
		Familia = str(self.ui.TxtFamilia.text())
		Genero = str(self.ui.TxtGenero.text())
		Especie = str(self.ui.TxtEspecie.text())
		Subespecie = str(self.ui.TxtSubespecie.text())
		
		Nombre = str(self.ui.TxtNombre.text())
		Peso = float(self.ui.TxtPeso.text())
		Fecha = int(self.ui.TxtFecha.text())
		Estado = str(self.ui.TxtEstado.text())
		Metodo = str(self.ui.TxtMetodo.text())
		Habitat =str(self.ui.TxtHabitat.toPlainText())
		Anotaciones = str(self.ui.Txtanotaciones.toPlainText()) 
		Sexo=str(self.ui.comboBox.currentText())
		
		RutaImagen = self.ui.TxtRutaImagen.text()
		
		TxtAltitud = float(self.ui.TxtAltitud.text())
		Vereda =str(self.ui.TxtVereda.text())
		LongitudGrados = int(self.ui.TxtLongitudGrados.text())
		LongitudMinutos = int(self.ui.TxtLongitudMinutos.text())
		LongitudSegundos = float(self.ui.TxtLongitudSegundos.text())
		LatitudGrados = int(self.ui.TxtLatitudGrados.text())
		LatitudMinutos = int(self.ui.TxtLatitudMinutos.text())
		LatitudSegundos = float(self.ui.TxtLatitudSegundos.text())
		
		try:
			Mun_selec=self.ui.comboBox_4.currentText()
			enviar="select cod_mun  from municipio where nomb_mun='%s'"% Mun_selec
			Cod_mun=Ingresar.Consulta(enviar)
			InserLocalizacion="insert into localizacion  (lat_grad,lat_min,lat_seg,lon_grad,lon_min,lon_seg,altitud,vereda,cod_mun) values (%s,%s,%s,%s,%s,%s,%s,'%s',%s);"% (LatitudGrados,LongitudMinutos,LatitudSegundos,LongitudGrados,LongitudMinutos,LongitudSegundos,TxtAltitud,Vereda,Cod_mun[0])
			Ingresar.InserBD(InserLocalizacion)
			Col="select cod_col from coleccion where nomb_cientifico='%s';"% Coleccion
			Subes="select cod_sub from subespecie where nomb_sub='%s';"% Subespecie
			Locali="select cod_loc from localizacion where altitud=%s and lat_grad=%s;"% (TxtAltitud , LatitudGrados)
			Code="Select count(*) from animal_colectado;"
			Coleccion1=Ingresar.Consulta(Col)
			Subespecie1=Ingresar.Consulta(Subes)
			Localizacion1=Ingresar.Consulta(Locali)
			Codigo=Ingresar.Consulta(Code)
			NomCien=Genero+Especie+Subespecie
			InserDatosEspecimen="insert into animal_colectado values (%s,%s,%s,%s,'%s','%s',%s,'%s',%s,'%s','%s','%s');"%(Codigo[0]+1,Coleccion1[0],Subespecie1[0],Localizacion1[0],Estado,Metodo,Fecha,Nombre,Peso,Habitat,Anotaciones,Sexo[0].upper())
			print InserDatosEspecimen
			Ingresar.InserBD(InserDatosEspecimen)
			#aves.SaberAnimal(Codigo[0]+2)
			QMessageBox.information(self,"Mensaje","Especimen guardado con exito")
			Ingresar.LimpiarTodito()
		except:			
			QMessageBox.information(self,"Error","No se puede guardar especimen")
			
	def LlenarDpto(self):
		db=MySQLdb.connect("localhost","root","10267","mhnu")
		curso=db.cursor()
		curso.execute("select nomb_dept from departamento;")
		InforUb=curso.fetchall()
		self.ui.comboBox_3.addItem(_fromUtf8("Seleccionar"))
		for departamento in InforUb:
			dpto=_fromUtf8(str(departamento))
			dep=dpto.replace("(","").replace(")","").replace("'","").replace(",","")
			self.ui.comboBox_3.addItem(_fromUtf8(dep))
		self.ui.comboBox_3.setEnabled(True)
	
	def LlenarMunicipio(self):
		self.ui.comboBox_4.clear()
		self.ui.comboBox_4.setEnabled(True)
		marcado=self.ui.comboBox_3.currentText()
		consultica="select municipio.nomb_mun from departamento, municipio where departamento.cod_dept=municipio.cod_dept and departamento.nomb_dept='%s';"% marcado
		db=MySQLdb.connect("localhost","root","10267","mhnu")
		curso=db.cursor()
		curso.execute(consultica)
		InfoUser=curso.fetchall()
		for departamento in InfoUser:
			muni=_fromUtf8(str(departamento))
			mun=_fromUtf8(muni.replace("(","").replace(")","").replace("'","").replace(",",""))
			self.ui.comboBox_4.addItem((_fromUtf8(str(mun))))
		
	def Municipio(self):
		print""
		
	def InserBD(self,insertar):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(insertar)
			InfoUser=curso.fetchone()
			db.commit()
		except:
			db.rollback()
	
	def Consulta(self,consulta):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(consulta)
			InfoUser=curso.fetchone()
			db.commit()
			db.close()
			return InfoUser
		except:
			db.close()
			return "Vacio"
				
	def Volver(self):
		Menuadmon.show()
		Ingresar.close()
		
	def Continuar(self):
		if self.Esp==1:
			#Ictologica
			Ingresar.close()
		if self.Esp==2:
			#Herpectologica
			Ingresar.close()
		if self.Esp==3:
			#Ornitologica
			aves.show()
			Ingresar.close()
		if self.Esp==4:
			#Mustozoologica
			Ingresar.close()
		if self.Esp==5:
			#Invertebrados
			Ingresar.close()			
		if self.Esp==6:
			#Tejidos
			Tej.show()		
			Ingresar.close()		
		else:
			print""
					
class Ornitologia(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_Ornitologia()
		self.ui.setupUi(self)
		
	def Guardar(self):
		Edad = self.ui.TxtEdad.text()
		Envergadura =self.ui.TxtEnvergadura.text()
		Grasa = self.ui.TxtGrasa.text()
		Muda = str(self.ui.TxtMuda.toPlainText())
		ContenidoEstomacal =str(self.ui.TxtContenidoEstomacal.toPlainText())
		PartesBlandas = str(self.ui.TxtPartesBlandas.toPlainText())
		Reproduccion = str(self.ui.TxtReproduccion.toPlainText())
		Gonodas = str(self.ui.TxtGonodas.toPlainText())
		Oscificacion = self.ui.TxtEdad.text()
		SacarCode="Select count(*) from ornitologia;"
		CodeAni="Select count(*) animal_colectado;"
		CodOrn=aves.Consulta(SacarCode)
		CodAni=aves.Consulta(CodeAni)		
		try:
			Ornitologia="insert into ornitologia values (%s,%s,%s,%s,'%s',%s,'%s','%s','%s','%s',%s);"%(CodAni[0]+1,CodOrn[0]+1,Edad,Envergadura,Reproduccion,Grasa,ContenidoEstomacal,Muda,PartesBlandas,Gonodas,Oscificacion)
			aves.InserBD(Ornitologia)
			QMessageBox.information(self,"Mensaje","Especimen guardado con exito")
			aves.close()
			Menuadmon.show()
		except:
			QMessageBox.information(self,"Error","No se pudo guardar la informacion,Intentelo de nuevo")

		
	def InserBD(self,insertar):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(insertar)
			InfoUser=curso.fetchone()
			db.commit()
			db.close()
		except:
			db.rollback()
			db.close()
	
	def Consulta(self,consulta):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(consulta)
			InfoUser=curso.fetchone()
			db.commit()
			db.close()
			return InfoUser
		except:
			db.close()
			return "Vacio"			
				
class Tejidos(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_Tejidos()
		self.ui.setupUi(self)
		
	def Guardar(self):
		Tipo=str(self.ui.comboBox.currentText())
		Nombre = str(self.ui.TxtNombre.text())
		Descripcion = str(self.ui.TxtDescripcion.toPlainText())
		CodA=Tej.Consulta("select count(*) from animal_colectado;")
		CodTe=Tej.Consulta("select count(*) from tejidos;")
		#RadioButton1.Checked = True
		
		if Nombre=="" or Tipo=="":
			QMessageBox.information(self,"Error","Campos vacios")
		else:
			try:
				insert="insert into tejidos values(%s,%s,'%s','%s','%s');"%(CodA[0]+1,CodTe[0]+1,Nombre,Tipo,Descripcion)
				print insert
				Tej.InserBD(insert)
				QMessageBox.information(self,"Mensaje","Especimen guardado con exito")
				Menuadmon.show()
				Tej.close()
			except:
				QMessageBox.information(self,"Error","no se pudo registrar el especimen")
			
	
	def InserBD(self,insertar):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(insertar)
			InfoUser=curso.fetchone()
			db.commit()
			db.close()
		except:
			print"No se pudo insertar"
			db.rollback()
			db.close()
	
	def Consulta(self,consulta):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(consulta)
			InfoUser=curso.fetchone()
			db.commit()
			db.close()
			return InfoUser
		except:
			db.close()
			return "Vacio"
						
class Busqueda(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_PanelDeBusqueda()
		self.ui.setupUi(self)
		self.ui.TxtBDpto.setEnabled(True)
		self.ui.TxtBNombre.setEnabled(True)
		self.ui.TxtBCol.setEnabled(True)
		self.ui.TxtBSub.setEnabled(True)
		self.opc1=0
		self.opc2=0
		self.opc3=0
		self.opc4=0		        
	
	def BNombre(self):
		Nom=self.ui.TxtBNombre.text()
		Enviar="select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado as estado ,	s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector from ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , subespecie as s natural join especies as e where orn.cod_ani=(select cod_ani from animal_colectado where nomb_ani='%s') and a.cod_col = col.cod_col and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = d.cod_dept	and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp;" % Nom
		Envio="select count(*) from ornitologia where cod_ani=(select cod_ani from animal_colectado where nomb_ani='%s');"%Nom
		SaberFilas=Buscar.Consulta(Envio)
		Par=int(SaberFilas[0])
		
		db=MySQLdb.connect("localhost","root","10267","mhnu")
		curso=db.cursor()
		curso.execute(Enviar)
		InfoUser=curso.fetchall()
		db.commit()
		db.close()
		
		self.ui.TablaGeneral.setRowCount(Par)
		self.ui.TablaGeneral.setColumnCount(9)
				
		item = QTableWidgetItem("Codigo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
		item = QTableWidgetItem("Nombre")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
		item = QTableWidgetItem("Departamento")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
		item = QTableWidgetItem("Estado")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
		item = QTableWidgetItem("Subespecie")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 4, item )
		item = QTableWidgetItem("Especie")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 5, item )
		item = QTableWidgetItem("Sexo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 6, item )
		item = QTableWidgetItem("Edad")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 7, item )
		item = QTableWidgetItem("Colector")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 8, item )
		for i in range(Par):
			for j in range(9):
				item = QTableWidgetItem(InfoUser[i][j])
				self.ui.TablaGeneral.setItem(i,j, item)
	
	def BDepartamento(self):
		Dpto=self.ui.TxtBDpto.text()
		Enviar="select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado,s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector  from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , subespecie as s natural join especies as e where  a.cod_col = col.cod_col	and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = (select cod_dept from departamento where nomb_dept = '%s')	and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;"% Dpto
		Envio="select count(orn.cod_orn) as cantidad from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , subespecie as s natural join especies as e where  a.cod_col = col.cod_col and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = (select cod_dept from departamento where nomb_dept = '%s') and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;"%Dpto
		SaberFilas=Buscar.Consulta(Envio)
			
		db=MySQLdb.connect("localhost","root","10267","mhnu")
		curso=db.cursor()
		curso.execute(Enviar)
		InfoUser=curso.fetchall()
		db.commit()
		db.close()
					
		Par=int(SaberFilas[0])
		self.ui.TablaGeneral.setRowCount(Par)
		self.ui.TablaGeneral.setColumnCount(9)
						
		item = QTableWidgetItem("Codigo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
		item = QTableWidgetItem("Nombre")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
		item = QTableWidgetItem("Departamento")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
		item = QTableWidgetItem("Estado")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
		item = QTableWidgetItem("Subespecie")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 4, item )
		item = QTableWidgetItem("Especie")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 5, item )
		item = QTableWidgetItem("Sexo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 6, item )
		item = QTableWidgetItem("Edad")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 7, item )
		item = QTableWidgetItem("Colector")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 8, item )
		for i in range(Par):
			for j in range(9):
				item = QTableWidgetItem(InfoUser[i][j])
				self.ui.TablaGeneral.setItem(i,j, item)
	
	def BSubespecie(self):
		Sub=self.ui.TxtBSub.text()
		Enviar="select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado,s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , subespecie as s natural join especies as e where  a.cod_col = col.cod_col and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and a.cod_sub = (select cod_sub from subespecie where nomb_sub = '%s')	and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;"%Sub
		Envio="select count(cod_ani) from animal_colectado where cod_sub=(select cod_sub from subespecie where nomb_sub='%s');"%Sub
		SaberFilas=Buscar.Consulta(Envio)
		Par=int(SaberFilas[0])
		
		db=MySQLdb.connect("localhost","root","10267","mhnu")
		curso=db.cursor()
		curso.execute(Enviar)
		InfoUser=curso.fetchall()
		db.commit()
		db.close()
		
		self.ui.TablaGeneral.setRowCount(Par)
		self.ui.TablaGeneral.setColumnCount(9)
				
		item = QTableWidgetItem("Codigo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
		item = QTableWidgetItem("Nombre")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
		item = QTableWidgetItem("Departamento")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
		item = QTableWidgetItem("Estado")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
		item = QTableWidgetItem("Subespecie")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 4, item )
		item = QTableWidgetItem("Especie")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 5, item )
		item = QTableWidgetItem("Sexo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 6, item )
		item = QTableWidgetItem("Edad")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 7, item )
		item = QTableWidgetItem("Colector")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 8, item )
		for i in range(Par):
			for j in range(9):
				item = QTableWidgetItem(InfoUser[i][j])
				self.ui.TablaGeneral.setItem(i,j, item)
		
	def BColector(self):
		Col=self.ui.TxtBCol.text()
		Enviar="select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado,s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector  from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , 	subespecie as s natural join especies as e where  a.cod_col = col.cod_col and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and a.cod_col = (select cod_col from colectores where nomb_col = '%s') and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;"%Col
		Envio="select count(cod_ani) from animal_colectado where cod_col=(select cod_col  from colectores where nomb_col='%s');"%Col
		SaberFilas=Buscar.Consulta(Envio)
		Par=int(SaberFilas[0])
		
		db=MySQLdb.connect("localhost","root","10267","mhnu")
		curso=db.cursor()
		curso.execute(Enviar)
		InfoUser=curso.fetchall()
		db.commit()
		db.close()
		
		self.ui.TablaGeneral.setRowCount(Par)
		self.ui.TablaGeneral.setColumnCount(9)
				
		item = QTableWidgetItem("Codigo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
		item = QTableWidgetItem("Nombre")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
		item = QTableWidgetItem("Departamento")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
		item = QTableWidgetItem("Estado")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
		item = QTableWidgetItem("Subespecie")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 4, item )
		item = QTableWidgetItem("Especie")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 5, item )
		item = QTableWidgetItem("Sexo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 6, item )
		item = QTableWidgetItem("Edad")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 7, item )
		item = QTableWidgetItem("Colector")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 8, item )
		for i in range(Par):
			for j in range(9):
				item = QTableWidgetItem(InfoUser[i][j])
				self.ui.TablaGeneral.setItem(i,j, item)
		
	def  Buscar(self):
		Nom=self.ui.TxtBNombre.text()
		Dpto=self.ui.TxtBDpto.text()
		Sub=self.ui.TxtBSub.text()
		Col=self.ui.TxtBCol.text()
		if self.opc1==0 and self.opc2==0 and self.opc3==0 and self.opc4==0:
			QMessageBox.information(self,"Error","Seleccione una opcion")
		else:
			####
			if self.opc1==1 and Nom=="":
				QMessageBox.information(self,"Error","Campo vacio")
			else:				
				Enviar="select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado as estado ,	s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector from ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , subespecie as s natural join especies as e where orn.cod_ani=(select cod_ani from animal_colectado where nomb_ani='%s') and a.cod_col = col.cod_col and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = d.cod_dept	and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp;" % Nom
				AddTabla=Buscar.ConsultaTodo(Enviar)
				Envio="select count(*) from ornitologia where cod_ani=(select cod_ani from animal_colectado where nomb_ani='%s');"%Nom
				#SaberFilas=Buscar.Consulta(Envio)
				#Par=int(SaberFilas[0])
				self.ui.TablaGeneral.setRowCount(Par)
				self.ui.TablaGeneral.setColumnCount(9)
				
				item = QTableWidgetItem("Codigo")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
				item = QTableWidgetItem("Nombre")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
				item = QTableWidgetItem("Departamento")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
				item = QTableWidgetItem("Estado")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
				item = QTableWidgetItem("Subespecie")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 4, item )
				item = QTableWidgetItem("Especie")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 5, item )
				item = QTableWidgetItem("Sexo")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 6, item )
				item = QTableWidgetItem("Edad")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 7, item )
				item = QTableWidgetItem("Colector")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 8, item )
					
			####
			if self.opc2==1 and Dpto=="":
				QMessageBox.information(self,"Error","Campo vacio")
			else:
				Enviar="select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado,s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector  from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , subespecie as s natural join especies as e where  a.cod_col = col.cod_col	and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = (select cod_dept from departamento where nomb_dept = '%s')	and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;"% Dpto
				#AddTabla=Buscar.ConsultaTodo(Enviar)
				Envio="select count(orn.cod_orn) as cantidad from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , subespecie as s natural join especies as e where  a.cod_col = col.cod_col and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = (select cod_dept from departamento where nomb_dept = '%s') and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;"%Dpto
				SaberFilas=Buscar.Consulta(Envio)
				
				db=MySQLdb.connect("localhost","root","10267","mhnu")
				curso=db.cursor()
				curso.execute(Enviar)
				InfoUser=curso.fetchall()
				db.commit()
				db.close()
					
				Par=int(SaberFilas[0])
				self.ui.TablaGeneral.setRowCount(Par)
				self.ui.TablaGeneral.setColumnCount(9)
						
				item = QTableWidgetItem("Codigo")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
				item = QTableWidgetItem("Nombre")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
				item = QTableWidgetItem("Departamento")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
				item = QTableWidgetItem("Estado")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
				item = QTableWidgetItem("Subespecie")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 4, item )
				item = QTableWidgetItem("Especie")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 5, item )
				item = QTableWidgetItem("Sexo")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 6, item )
				item = QTableWidgetItem("Edad")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 7, item )
				item = QTableWidgetItem("Colector")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 8, item )
				for i in range(Par):
					for j in range(7):
						item = QTableWidgetItem(InfoUser[i][j])
						self.ui.TablaGeneral.setItem(i,j, item)
						
			####	
			if self.opc3==1 and Sub=="":
				QMessageBox.information(self,"Error","Campo vacio")
			else:
				Enviar="select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado,s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , subespecie as s natural join especies as e where  a.cod_col = col.cod_col and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and a.cod_sub = (select cod_sub from subespecie where nomb_sub = '%s')	and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;"%Sub
				AddTabla=Buscar.ConsultaTodo(Enviar)
				Envio="select count(cod_ani) from animal_colectado where cod_sub=(select cod_sub from subespecie where nomb_sub='%s');"%Sub
				SaberFilas=Buscar.Consulta(Envio)
				Par=int(SaberFilas[0])
				self.ui.TablaGeneral.setRowCount(Par)
				self.ui.TablaGeneral.setColumnCount(9)
								
				item = QTableWidgetItem("Codigo")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
				item = QTableWidgetItem("Nombre")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
				item = QTableWidgetItem("Departamento")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
				item = QTableWidgetItem("Estado")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
				item = QTableWidgetItem("Subespecie")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 4, item )
				item = QTableWidgetItem("Especie")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 5, item )
				item = QTableWidgetItem("Sexo")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 6, item )
				item = QTableWidgetItem("Edad")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 7, item )
				item = QTableWidgetItem("Colector")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 8, item )
				for i in range(Par):
					for j in range(7):
						item = QTableWidgetItem(AddTabla[i][j])
						self.ui.TablaGeneral.setItem(i,j, item)
			####	
			if self.opc4==1 and Col=="":
				QMessageBox.information(self,"Error","Campo vacio")
			else:
				Enviar="select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado,s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector  from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , 	subespecie as s natural join especies as e where  a.cod_col = col.cod_col and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and a.cod_col = (select cod_col from colectores where nomb_col = '%s') and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;"%Col
				AddTabla=Buscar.ConsultaTodo(Enviar)
				Envio="select count(cod_ani) from animal_colectado where cod_col=(select cod_col  from colectores where nomb_col='%s');"%Col
				SaberFilas=Buscar.Consulta(Envio)
				Par=int(SaberFilas[0])
				
				self.ui.TablaGeneral.setRowCount(Par)
				self.ui.TablaGeneral.setColumnCount(9)
				item = QTableWidgetItem("Codigo")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
				item = QTableWidgetItem("Nombre")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
				item = QTableWidgetItem("Departamento")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
				item = QTableWidgetItem("Estado")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
				item = QTableWidgetItem("Subespecie")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 4, item )
				item = QTableWidgetItem("Especie")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 5, item )
				item = QTableWidgetItem("Sexo")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 6, item )
				item = QTableWidgetItem("Edad")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 7, item )
				item = QTableWidgetItem("Colector")
				self.ui.TablaGeneral.setHorizontalHeaderItem( 8, item )
				for i in range(Par):
					for j in range(7):
						item = QTableWidgetItem(AddTabla[i][j])
						self.ui.TablaGeneral.setItem(i,j, item)
							
	def Llenar(self,Par,AddTabla):
		print""
		self.ui.TablaGeneral.setRowCount(Par)
		self.ui.TablaGeneral.setColumnCount(9)
				
		item = QTableWidgetItem("Codigo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
		item = QTableWidgetItem("Nombre")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
		item = QTableWidgetItem("Departamento")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
		item = QTableWidgetItem("Estado")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
		item = QTableWidgetItem("Subespecie")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 4, item )
		item = QTableWidgetItem("Especie")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 5, item )
		item = QTableWidgetItem("Sexo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 6, item )
		item = QTableWidgetItem("Edad")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 7, item )
		item = QTableWidgetItem("Colector")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 8, item )

		for i in range(Par):
			for j in range(9):
				item = QTableWidgetItem(AddTabla[i][j])
				self.ui.TablaGeneral.setItem(i,j, item)	
	
	def BusquedaEspecifica(self):
		Buscar.close()
		BusPer.show()
	
	def VerEstado(self):
		Buscar.close()
		Est.show()
			
	def Consulta(self,consulta):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(consulta)
			InfoUser=curso.fetchone()
			db.commit()
			db.close()
			return InfoUser
		except:
			db.close()
			return "Vacio"
			
	def ConsultaTodo(self,consulta):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(consulta)
			InfoUser=curso.fetchall()
			db.commit()
			db.close()
			return InfoUser
		except:
			db.close()
			return "Vacio"
        			
	def Volver(self):
		if self.Me==1:
			Menuadmon.show()
		if self.Me==2:
			MenuInv.show()
		self.ui.TxtBNombre.clear()
		self.ui.TxtBDpto.clear()
		self.ui.TxtBSub.clear()
		self.ui.TxtBCol.clear()
		Buscar.close()
	
	def SaberQueMenuInvoco(self,Lugar):
		self.Me=Lugar

class Backup(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_Backup()
		self.ui.setupUi(self)
	
	def RealizarBackup(self):
		fecha=time.strftime("%d%m%y")
		hora=time.strftime("%H%M%S")
		FechaHora=fecha+"-"+hora+"-"+"CopiaDeSeguridad.sql"
		FH=str(FechaHora)
		Password = self.ui.TxtPassCopia.text()
		Respaldo = self.ui.comboBox.currentText()
		VerificarPass="select tipo_us from usuarios where clave='%s'"% Password
		CopiaBD="mysqldump --user=root --password=10267 mhnu --tables %s  >D:\ProyectoBD\Principal\Backup\%s"% (Respaldo,FH)
		CopiaBDALL="mysqldump --user=root --password=10267 mhnu >D:\ProyectoBD\Principal\Backup\%s"%FH
		Tipouser=Copia.Consulta(VerificarPass)
		print Tipouser
		if Tipouser[0].upper() =="ADMINISTRADOR":
			Password = self.ui.TxtPassCopia.clear()
			if Respaldo=="Todos los datos":
				os.system(CopiaBDALL)
				QMessageBox.information(self,"Mensaje","Copia de seguridad realizada con exito")
			else:
				if Respaldo=="Usuarios":
					CopiaBD="mysqldump --user=root --password=10267 mhnu --tables usuarios > %s "% FH
					os.system(CopiaBD)
					QMessageBox.information(self,"Mensaje","Copia de seguridad realizada con exito")
				if Respaldo=="Departamentos":
					CopiaBD="mysqldump --user=root --password=10267 mhnu --tables departamento > %s "% FH
					os.system(CopiaBD)
					QMessageBox.information(self,"Mensaje","Copia de seguridad realizada con exito")
				if Respaldo=="Municipios":
					CopiaBD="mysqldump --user=root --password=10267 mhnu --tables municipio > %s "% FH
					os.system(CopiaBD)
					QMessageBox.information(self,"Mensaje","Copia de seguridad realizada con exito")
				if Respaldo=="Animales Colectados":
					CopiaBD="mysqldump --user=root --password=10267 mhnu --tables animal_colectado > %s "% FH
					os.system(CopiaBD)
					QMessageBox.information(self,"Mensaje","Copia de seguridad realizada con exito")
				if Respaldo=="Ornitologia":
					CopiaBD="mysqldump --user=root --password=10267 mhnu --tables ornitologia > %s "% FH
					os.system(CopiaBD)
					QMessageBox.information(self,"Mensaje","Copia de seguridad realizada con exito")
				if Respaldo=="Tejidos":
					CopiaBD="mysqldump --user=root --password=10267 mhnu --tables tejidos > %s "% FH
					os.system(CopiaBD)
					QMessageBox.information(self,"Mensaje","Copia de seguridad realizada con exito")
				if Respaldo=="Localizacion":
					CopiaBD="mysqldump --user=root --password=10267 mhnu --tables localizacion > %s "% FH
					os.system(CopiaBD)
					QMessageBox.information(self,"Mensaje","Copia de seguridad realizada con exito")
		else:
			if Tipouser[0].upper()=="INVITADO":
				QMessageBox.information(self,"Error","Ud no posee permisos para realizar esta accion")
				self.ui.TxtPassCopia.clear()
			if Tipouser[0].upper()=="VACIO":
				QMessageBox.information(self,"Error","Contraseña Incorrecta")
				self.ui.TxtPassCopia.clear()
			
			
	def Consulta(self,consulta):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(consulta)
			InfoUser=curso.fetchone()
			db.commit()
			return InfoUser
		except:
			return "VACIO"
	
	def Volver(self):
		self.ui.TxtPassCopia.clear()
		Menuadmon.show()
		Copia.close()

class BusquedaPersonalizada(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_BusquedaPersonalizada()
		self.ui.setupUi(self)
		
	def Buscar(self):
		if self.Uno==1:
			Code = self.ui.TxtCodeAnimal.text()
			TraerInfo="select concat('MHNU-O - ',orn.cod_orn) as codigo, a.nomb_ani, concat (s.nomb_sub ,'-',e.nomb_esp,'-', g.nomb_gen,'-', f.nomb_fam,'-', o.nomb_ord ,'-', c.nomb_cla ,'-', co.nomb_cientifico) as taxonomia, concat (l.lat_grad,'-',l.lat_min,'-',l.lat_seg) as latitud,concat (l.lon_grad,'-',l.lon_min,'-',l.lon_seg) as longitud, concat (l.vereda,'-', m.nomb_mun,'-',d.nomb_dept,'-',p.nomb_pais) as localizacion,	a.estado as estado, a.metodo as metodo, a.fecha as fecha_ingreso, a.sexo as sexo, a.peso as peso, a.habitat as habitat, a.anotaciones as anotaciones, orn.edad as edad, orn.envergadura as envergadura, orn.inf_repro as informacion_reproductiva , orn.grasa as grasa, orn.cont_est as contenido_estomacal, orn.muda as muda, orn.part_blan as partes_blandas, orn.gonadas as gonadas , orn.oscificacion as osficicacion from ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d natural join pais as p, colectores as col,	subespecie as s natural join especies as e natural join genero as g natural join familia as f natural join orden as o natural join clase as c natural join coleccion as co where	a.cod_col = col.cod_col	and  orn.cod_orn='%s'and a.cod_sub = s.cod_sub;"% Code
			Mostrar=BusPer.Consulta(TraerInfo)
			self.ui.L1.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[0])), None))
			self.ui.L2.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[1])), None))
			self.ui.L3.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[2])), None))
			self.ui.L4.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[3])), None))
			self.ui.L5.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[4])), None))
			self.ui.L6.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[5])), None))
			self.ui.L7.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[6])), None))
			self.ui.L8.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[7])), None))
			self.ui.L9.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[8])), None))
			self.ui.L10.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[9])), None))
			self.ui.L11.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[10])), None))
			self.ui.L12.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[11])), None))
			self.ui.L13.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[12])), None))
			self.ui.L14.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[13])), None))
			self.ui.L15.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[14])), None))
			self.ui.L16.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[15])), None))
			self.ui.L17.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[16])), None))
			self.ui.L18.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[17])), None))
			self.ui.L19.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[18])), None))
			self.ui.L20.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[19])), None))
			self.ui.L21.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[20])), None))
			self.ui.L22.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[21])), None))
		if self.Dos==1:
			Nom = self.ui.TxtnomAnimal.text()
			Env = self.ui.TxtEnvergadura.text()
			TraerInfo="select concat('MHNU-O - ',orn.cod_orn) as codigo, a.nomb_ani, concat (s.nomb_sub ,'-',e.nomb_esp,'-', g.nomb_gen,'-', f.nomb_fam,'-', o.nomb_ord ,'-', c.nomb_cla ,'-', co.nomb_cientifico) as taxonomia, concat (l.lat_grad,'-',l.lat_min,'-',l.lat_seg) as latitud,concat (l.lon_grad,'-',l.lon_min,'-',l.lon_seg) as longitud, concat (l.vereda,'-', m.nomb_mun,'-',d.nomb_dept,'-',p.nomb_pais) as localizacion,	a.estado as estado, a.metodo as metodo, a.fecha as fecha_ingreso, a.sexo as sexo, a.peso as peso, a.habitat as habitat, a.anotaciones as anotaciones, orn.edad as edad, orn.envergadura as envergadura, orn.inf_repro as informacion_reproductiva , orn.grasa as grasa, orn.cont_est as contenido_estomacal, orn.muda as muda, orn.part_blan as partes_blandas, orn.gonadas as gonadas , orn.oscificacion as osficicacion from ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d natural join pais as p, colectores as col,	subespecie as s natural join especies as e natural join genero as g natural join familia as f natural join orden as o natural join clase as c natural join coleccion as co where	a.cod_col = col.cod_col	and  	a.nomb_ani ='%s'	and     orn.envergadura='%s'	and a.cod_sub = s.cod_sub;"% (Nom,Env)
			Mostrar=BusPer.Consulta(TraerInfo)
			self.ui.L1.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[0])), None))
			self.ui.L2.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[1])), None))
			self.ui.L3.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[2])), None))
			self.ui.L4.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[3])), None))
			self.ui.L5.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[4])), None))
			self.ui.L6.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[5])), None))
			self.ui.L7.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[6])), None))
			self.ui.L8.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[7])), None))
			self.ui.L9.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[8])), None))
			self.ui.L10.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[9])), None))
			self.ui.L11.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[10])), None))
			self.ui.L12.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[11])), None))
			self.ui.L13.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[12])), None))
			self.ui.L14.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[13])), None))
			self.ui.L15.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[14])), None))
			self.ui.L16.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[15])), None))
			self.ui.L17.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[16])), None))
			self.ui.L18.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[17])), None))
			self.ui.L19.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[18])), None))
			self.ui.L20.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[19])), None))
			self.ui.L21.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[20])), None))
			self.ui.L22.setText(_translate("BusquedaPersonalizada",_fromUtf8(str(Mostrar[21])), None))
		
	def HabilitarUno(self):
		self.ui.TxtCodeAnimal.setEnabled(True)
		self.ui.BotonBusqueda.setEnabled(True)
		self.ui.TxtnomAnimal.setEnabled(False)
		self.ui.TxtEnvergadura.setEnabled(False)
		self.ui.TxtnomAnimal.clear()
		Mostrar=0
		self.Uno=1
		self.Dos=0
		
	def HabilitarVarios(self):
		self.ui.TxtCodeAnimal.setEnabled(False)
		self.ui.TxtnomAnimal.setEnabled(True)
		self.ui.BotonBusqueda.setEnabled(True)
		self.ui.TxtEnvergadura.setEnabled(True)
		self.ui.TxtCodeAnimal.clear()
		self.ui.TxtEnvergadura.clear()
		Mostrar=0
		self.Uno=0
		self.Dos=1
	
	def Consulta(self,consulta):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(consulta)
			InfoUser=curso.fetchone()
			db.commit()
			return InfoUser
		except:
			return "Vacio"
		
	def Volver(self):
		self.ui.TxtnomAnimal.clear()
		self.ui.TxtEnvergadura.clear()
		self.ui.TxtCodeAnimal.clear()
		self.ui.L1.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L2.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L3.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L4.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L5.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L6.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L7.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L8.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L9.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L10.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L11.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L12.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L13.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L14.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L15.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L16.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L17.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L18.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L19.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L20.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L21.setText(_translate("BusquedaPersonalizada","-----", None))
		self.ui.L22.setText(_translate("BusquedaPersonalizada","-----", None))
		BusPer.close()
		Buscar.show()

class Aportes(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_Aportes()
		self.ui.setupUi(self)
	
	def Guardar(self):
		Pass = str(self.ui.TxtPass.text())
		Apor = self.ui.TxtAportes.toPlainText()
		con="select * from usuarios where clave='%s';"%Pass
		Inse="insert into aportes (apor,otro) values ('%s','4');" % Apor
		print Inse
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(con)
			self.InfoUser=curso.fetchone()
			db.commit()
			db.close()
		except:
			db.close()
		if self.InfoUser[3]=="INVITADO":
			try:
				db=MySQLdb.connect("localhost","root","10267","mhnu")
				curso=db.cursor()
				curso.execute(Inse)
				InfoUser=curso.fetchone()
				db.commit()
				QMessageBox.information(self,"Mensaje","Aporte enviado con exito")
			except:
				db.rollback()
				print "Error"
		else:
			QMessageBox.information(self,"Error","Clave Incorrecta")
		
	def Volver(self):
		MenuInv.show()
		Apor.close() 

class VVAportes(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_AportesUser()
		self.ui.setupUi(self)
	
	def AbrirCarpeta(self):
		os.system("start D:\ProyectoBD\Principal\AportesUsers")
		
	def Txt(self):
		fecha=time.strftime("%d%m%y")
		hora=time.strftime("%H%M%S")
		FechaHora=fecha+"-"+hora+"-"+"Aportes"
		FH=str(FechaHora)
		VAportes.Consulta("Select codigo, apor from aportes;")
		ruta="SELECT * INTO OUTFILE 'D:/ProyectoBD/Principal/AportesUsers/%s.txt' FIELDS TERMINATED BY ',' FROM aportes;"% FH
		VAportes.Consulta(ruta)
		QMessageBox.information(self,"Mensaje","Archivo Exportado Con Exito")
	
	def Sql(self):
		fecha=time.strftime("%d%m%y")
		hora=time.strftime("%H%M%S")
		FechaHora=fecha+"-"+hora+"-"+"Aportes"
		FH=str(FechaHora)
		VAportes.Consulta("Select codigo, apor from aportes;")
		ruta="SELECT * INTO OUTFILE 'D:/ProyectoBD/Principal/AportesUsers/%s.sql' FIELDS TERMINATED BY ',' FROM aportes;"%FH
		VAportes.Consulta(ruta)
		QMessageBox.information(self,"Mensaje","Archivo Exportado Con Exito")

	
	def Excel(self):
		fecha=time.strftime("%d%m%y")
		hora=time.strftime("%H%M%S")
		FechaHora=fecha+"-"+hora+"-"+"Aportes"
		FH=str(FechaHora)
		VAportes.Consulta("Select codigo, apor from aportes;")
		ruta="SELECT * INTO OUTFILE 'D:/ProyectoBD/Principal/AportesUsers/%s.csv' FIELDS TERMINATED BY ',' FROM aportes;"%FH
		VAportes.Consulta(ruta)
		QMessageBox.information(self,"Mensaje","Archivo Exportado Con Exito")
	
	def Consulta(self,consulta):
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			curso.execute(consulta)
			InfoUser=curso.fetchone()
			db.commit()
			db.close()
			return InfoUser
		except:
			db.close()
			return "Vacio"
	
	def Volver(self):
		Menuadmon.show()
		VAportes.close()
		
class VerEstadoAnimal(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self,None)
		self.ui = Ui_ViewEstado()
		self.ui.setupUi(self)
	
	def Disponible(self):
		Enviar="select 	concat('MHNU-T - ',tej.cod_teji) as codigo, a.nomb_ani, a.estado as estado, a.sexo as sexo from  tejidos as tej natural join animal_colectado as a where 	a.estado='Disponible';"
		Envio="select count(*) from animal_colectado where estado='Disponible'"
		SaberFilas=Buscar.Consulta(Envio)
		Par=int(SaberFilas[0])
		Enviar1="select 	concat('MHNU-O - ',orn.cod_orn) as codigo, a.nomb_ani, a.estado as estado, a.sexo as sexo from 	ornitologia as orn natural join animal_colectado as a where 	a.estado='Disponible';"
		db=MySQLdb.connect("localhost","root","10267","mhnu")
		curso=db.cursor()
		curso.execute(Enviar)
		InfoUser=curso.fetchall()
		db.commit()
		db.close()
		
		db=MySQLdb.connect("localhost","root","10267","mhnu")
		curso=db.cursor()
		curso.execute(Enviar1)
		InfoUser1=curso.fetchall()
		db.commit()
		db.close()
		
		InfoUser=InfoUser+InfoUser1
		self.ui.TablaGeneral.setRowCount(Par)
		self.ui.TablaGeneral.setColumnCount(4)
				
		item = QTableWidgetItem("Codigo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
		item = QTableWidgetItem("Nombre")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
		item = QTableWidgetItem("Estado")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
		item = QTableWidgetItem("Sexo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
		for i in range(Par):
			for j in range(4):
				item = QTableWidgetItem(InfoUser[i][j])
				self.ui.TablaGeneral.setItem(i,j, item)
	
	
	def NoDisponible(self):
		Enviar="select 	concat('MHNU-T - ',tej.cod_teji) as codigo, a.nomb_ani, a.estado as estado, a.sexo as sexo from  tejidos as tej natural join animal_colectado as a where 	a.estado='no Disponible';"
		Envio="select count(*) from animal_colectado where estado='no Disponible';"
		SaberFilas=Buscar.Consulta(Envio)
		Par=int(SaberFilas[0])
		Enviar1="select 	concat('MHNU-O - ',orn.cod_orn) as codigo, a.nomb_ani, a.estado as estado, a.sexo as sexo from 	ornitologia as orn natural join animal_colectado as a where 	a.estado='no Disponible';"
		db=MySQLdb.connect("localhost","root","10267","mhnu")
		curso=db.cursor()
		curso.execute(Enviar)
		InfoUser=curso.fetchall()
		db.commit()
		db.close()
		
		db=MySQLdb.connect("localhost","root","10267","mhnu")
		curso=db.cursor()
		curso.execute(Enviar1)
		InfoUser1=curso.fetchall()
		db.commit()
		db.close()
		
		InfoUser=InfoUser+InfoUser1
		self.ui.TablaGeneral.setRowCount(Par)
		self.ui.TablaGeneral.setColumnCount(4)
				
		item = QTableWidgetItem("Codigo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 0, item )
		item = QTableWidgetItem("Nombre")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 1, item )
		item = QTableWidgetItem("Estado")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 2, item )
		item = QTableWidgetItem("Sexo")
		self.ui.TablaGeneral.setHorizontalHeaderItem( 3, item )
		for i in range(Par):
			for j in range(4):
				item = QTableWidgetItem(InfoUser[i][j])
				self.ui.TablaGeneral.setItem(i,j, item)
				
	def CambiarEstado(self):
		Estadito=str(self.ui.BoxEstado.currentText())
		Codecito = str(self.ui.TxtCodigo.text())
		print Codecito
		print Estadito
		modificar="update animal_colectado set estado='%s'where cod_ani =%s;"%(Estadito,Codecito)
		try:
			db=MySQLdb.connect("localhost","root","10267","mhnu")
			curso=db.cursor()
			modificar
			curso.execute(modificar)
			InfoUser=curso.fetchone()
			db.commit()
			QMessageBox.information(self,"Mensaje","Actualizado con extio")
		except:
			db.rollback()
	
	
	def Volver(self):
		self.ui.TxtCodigo.clear()
		Estadito=self.ui.BoxEstado.clear()
		Est.close()
		Buscar.show()

if __name__=="__main__":
	Museo = QApplication(sys.argv)
	QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
	QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())
	Buscar=Busqueda()
	Tej=Tejidos()
	aves=Ornitologia()
	Ingresar=IngresarDatos()
	actualizar= ModificarInfo()	
	DeleteUser=EliminarUsuario()
	Users=ControlUsers()
	Cre = Creditos()
	CambioP=CambioPassword()
	Menuadmon=Menuadmin()
	MenuInv=MenuInvitado()
	Copia=Backup()
	BusPer=BusquedaPersonalizada()
	Apor=Aportes()
	VAportes=VVAportes()
	Est=VerEstadoAnimal()
	Log = Login()
	Log.show()
	sys.exit(Museo.exec_())


# cd Desktop\Proyecto Bases de Datos\Principal\Proyectos en Pyqt
#pyuic4 CambioPass.ui -o CambioPassGrafico.py
#pyuic4 Creditos.ui -o CreditosGrafico.py
#pyuic4 EliminarUser.ui -o EliminarUserGrafico.py
#pyuic4 Login.ui -o LoginGrafico.py
#pyuic4 MenuAdministrador.ui -o MenuAdministradorGrafico.py
#pyuic4 MenuInvitado.ui -o MenuInvitadoGrafico.py
#pyuic4 MenuModificarInsertar.ui -o MenuModificarInsertarGrafico.py
#pyuic4 Usuarios.ui -o UsuariosGrafico.py
#Pyuic4 Ornitologia.ui -o OrnitologiaGrafico.py
#Pyuic4 Busqueda.ui -o BusquedaGrafico.py
#Pyuic4 VerEstado.ui -o VerEstadoGrafico.py
#Pyuic4 BusquedaPersonalizada.ui -o BusquedaPersonalizadaGrafico.py
#Pyuic4 Backup.ui -o BackupGrafico.py
#Pyuic4 AportesUser.ui -o AportesGrafico.py
#Pyuic4 VerAportes.ui -o VerAportesGrafico.py
