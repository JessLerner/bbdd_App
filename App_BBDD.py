from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
cuadro=Frame(root,width=1200,height=600)
cuadro.pack()
conexion=sqlite3.connect("Usuarios")
cursor=conexion.cursor()

def advertencia(elError):
	messagebox.showwarning("Atencion",elError)
def informacion(detalle):
	messagebox.showinfo("BBDD",detalle)
def salir():
	cerrar=messagebox.askokcancel("Salir","¿Desea salir de la aplicacion?")
	if cerrar==True:
		conexion.close()
		root.destroy()
	
def conectar():
	
	try:
		cursor.execute('''
		CREATE TABLE REGISTROS(
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		NOMBRE VARCHAR(30),
		PASSWORD VARCHAR(30),
		APELLIDO VARCHAR(30),
		DIRECCION VARCHAR(30),
		COMENTARIOS VARCHAR(100))
		''')
	except:
		advertencia("La Base ya existe")

def leer():
	
	cursor.execute("SELECT * FROM REGISTROS WHERE ID="+ campoID.get()) 
	usuario=cursor.fetchall()

	for usuarios in usuario:
		campoID.set(usuarios[0])
		campoNombre.set(usuarios[1])
		campoPass.set(usuarios[2])
		campoApellido.set(usuarios[3])
		campoDireccion.set(usuarios[4])
		cuadroComentario.insert(1.0,usuarios[5])
	conexion.commit()
def actualizar():
	 
	datos=(cuadroNombre.get(), cuadroPass.get(), cuadroApellido.get(), cuadroDireccion.get(), cuadroComentario.get(1.0,END))
	cursor.execute("UPDATE REGISTROS SET NOMBRE=?,PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=? WHERE ID="+ campoID.get(),(datos))
	conexion.commit()
	informacion("Registro actualizado con exito")

def insertar():
	
	datos=(cuadroNombre.get(),
	cuadroPass.get(),
	cuadroApellido.get(),
	cuadroDireccion.get(),
	cuadroComentario.get(1.0,END))

	cursor.execute("INSERT INTO REGISTROS VALUES (NULL,?,?,?,?,?)",datos)
	conexion.commit()
	informacion("Registro ingresado con exito")
def eliminar():
	cursor.execute("DELETE FROM REGISTROS WHERE ID="+ campoID.get())
	conexion.commit()
	informacion("Registro eliminado con exito")
def limpiar():
	campoID.set("")
	campoNombre.set("")
	campoPass.set("")
	campoApellido.set("")
	campoDireccion.set("")
	cuadroComentario.delete(1.0, END)

#-----------------------MENUES------------------------#

barramenu=Menu(root)
root.config(menu=barramenu)

archivoMenu=Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="BBDD",menu=archivoMenu)
archivoMenu.add_command(label="Conectar",command=lambda:conectar())
archivoMenu.add_command(label="Cerrar",command=lambda:salir())

archivoBorrar=Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Borrar",menu=archivoBorrar)
archivoBorrar.add_command(label="Borrar Campos",command=lambda:limpiar())

archivoCRUD=Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="CRUD",menu=archivoCRUD)
archivoCRUD.add_command(label="Crear",command=lambda:insertar())
archivoCRUD.add_command(label="Leer",command=lambda:leer())
archivoCRUD.add_command(label="Actualizar",command=lambda:actualizar())
archivoCRUD.add_command(label="Eliminar registro",command=lambda:eliminar())

archivoAyuda=Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Ayuda",menu=archivoAyuda)
archivoAyuda.add_command(label="Licencia",command=lambda:informacion("Producto bajo licencia"))
archivoAyuda.add_command(label="Acerca de...",command=lambda:informacion("Autor Jesica Lerner \n Version 1.2022 \n Todos los derechos reservados"))

#----------------------CAMPOS--------------------------------#

campoID=StringVar()
campoNombre=StringVar()
campoPass=StringVar()
campoApellido=StringVar()
campoDireccion=StringVar()
	


etiquetaID=Label(cuadro,text="ID")
etiquetaID.grid(row=0,column=0,padx=5,pady=5)
cuadroID=Entry(cuadro,textvariable=campoID)
cuadroID.grid(row=0,column=1,padx=5,pady=5)

etiquetaNombre=Label(cuadro,text="Nombre")
etiquetaNombre.grid(row=1,column=0,padx=5,pady=5)
cuadroNombre=Entry(cuadro,textvariable=campoNombre)
cuadroNombre.grid(row=1,column=1,padx=5,pady=5)

etiquetaPass=Label(cuadro,text="Password")
etiquetaPass.grid(row=2,column=0,padx=5,pady=5)
cuadroPass=Entry(cuadro,textvariable=campoPass)
cuadroPass.grid(row=2,column=1,padx=5,pady=5)
cuadroPass.config(show="*")

etiquetaApellido=Label(cuadro,text="Apellido")
etiquetaApellido.grid(row=3,column=0,padx=5,pady=5)
cuadroApellido=Entry(cuadro,textvariable=campoApellido)
cuadroApellido.grid(row=3,column=1,padx=5,pady=5)

etiquetaDireccion=Label(cuadro,text="Direccion")
etiquetaDireccion.grid(row=4,column=0,padx=5,pady=5)
cuadroDireccion=Entry(cuadro,textvariable=campoDireccion)
cuadroDireccion.grid(row=4,column=1,padx=5,pady=5)

etiquetaComentario=Label(cuadro,text="Comentarios")
etiquetaComentario.grid(row=5,column=0,padx=5,pady=5)
cuadroComentario=Text(cuadro)
cuadroComentario.grid(row=5,column=1,padx=5,pady=5)
cuadroComentario.config(width=15,height=5)

barra=Scrollbar(cuadro,command=cuadroComentario.yview)
barra.grid(row=5,column=2,sticky="nsew")
cuadroComentario.config(yscrollcommand=barra.set)

#-------------------BOTONES----------------------#

FrameBotones=Frame(root,width=200,height=100)
FrameBotones.pack()
botonCreate=Button(FrameBotones,text="Create",command=lambda:insertar())
botonCreate.grid(row=0,column=0,padx=10,pady=10)
botonRead=Button(FrameBotones,text="Read",command=lambda:leer())
botonRead.grid(row=0,column=1,padx=10,pady=10)
botonUpdate=Button(FrameBotones,text="Update",command=lambda:actualizar())
botonUpdate.grid(row=0,column=2,padx=10,pady=10)
botonDelete=Button(FrameBotones,text="Delete",command=lambda:eliminar())
botonDelete.grid(row=0,column=3,padx=10,pady=10)


root.mainloop()