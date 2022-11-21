from tkinter import *
from tkinter import ttk
import pymysql
import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv()

# Creamos ventana
vent = Tk()
# Agregar atributos
vent.geometry("800x600")
vent.title("CRUD Base de Datos")

global frmA

def dbTrabajadores():
    def __init__(self):
        self.conection = pymysql.connect(
            host = "localhost",
            user = "port",
            password = ""
        ) 

#database connection

class Database():
    def __init__(self):
        self.connection = pymysql.connect(
            host = os.getenv("HOST"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            db = os.getenv("DB_NAME"),
            ssl_verify_identity= True,
            ssl = {
                "ca": "/etc/ssl/cert.pem"
            }
        )
        self.cursor = self.connection.cursor()

    def getAllusers(self):
        query = "select * from workers"
        try:
            self.cursor.execute(query)
            users = self.cursor.fetchall()
            for i in users:
                print("name", i[0])
        except Exception as e:
            pass


db = Database()
db.getAllusers()
#Función para Salir de la App

def salir():
    print("*** Fin del sistema")
    vent.destroy()

def guardarDatos():
    print("")
 
def cancelar():
    print("")

"""Método para Agregar Trabajadores a la base de Datos"""
    
def AgregarFrm():

    frmA = Toplevel(vent)
    frmA .geometry("800x600")
    frmA .title("Módulo Agregar Datos")

    #vent.iconify()  
    lc = Label(frmA , text="Clave: ").grid(row= 2, column=2)
    txtClave = Entry(frmA, width=5).grid(row= 2, column=10)
    ln = Label(frmA , text="Nombre: ").grid(row= 4, column=2)
    txtNombre =Entry(frmA, width=30).grid(row= 4, column=10)
    ls= Label(frmA , text="Sueldo: ").grid(row= 6, column=2)
    txtSueldo=Entry(frmA, width=12).grid(row= 6, column=10)
    btnGuardar = Button(frmA, text="Guardar Datos", command=guardarDatos).grid(row= 12, column=7)
    btnCancelar = Button(frmA, text="Cancelar", command=frmA.destroy).grid(row= 12, column=10)
    

""" Método para buscar trabajadores """

def agregarTrabajador():

    frmA = Toplevel(vent)
    frmA .geometry("800x600")
    frmA .title("Módulo Agregar Datos")

    #vent.iconify()  
    lc = Label(frmA , text="Clave: ").grid(row= 2, column=2)
    txtClave = Entry(frmA, width=5).grid(row= 2, column=10)
    ln = Label(frmA , text="Nombre: ").grid(row= 4, column=2)
    txtNombre =Entry(frmA, width=30).grid(row= 4, column=10)
    ls= Label(frmA , text="Sueldo: ").grid(row= 6, column=2)
    txtSueldo=Entry(frmA, width=12).grid(row= 6, column=10)
    btnGuardar = Button(frmA, text="Guardar Datos", command=guardarDatos).grid(row= 12, column=7)
    btnCancelar = Button(frmA, text="Cancelar", command=frmA.destroy).grid(row= 12, column=10)
    
def buscarTrabajador():

    frmA = Toplevel(vent)
    frmA .geometry("800x600")
    frmA .title("Módulo Buscar trabajador")

    #vent.iconify()  
    lc = Label(frmA , text="Clave: ").grid(row= 2, column=2)
    txtClave = Entry(frmA, width=5).grid(row= 2, column=10)
    btnGuardar = Button(frmA, text="Buscar por clave", command=guardarDatos).grid(row= 12, column=7)
    btnCancelar = Button(frmA, text="Cancelar", command=frmA.destroy).grid(row= 12, column=10)

def borrarTrabajador():
    frmA = Toplevel(vent)
    frmA .geometry("800x600")
    frmA .title("Módulo Borrar trabajador")

    #vent.iconify()  
    lc = Label(frmA , text="Clave: ").grid(row= 2, column=2)
    txtClave = Entry(frmA, width=5).grid(row= 2, column=10)
    btnGuardar = Button(frmA, text="Buscar por clave", command=guardarDatos).grid(row= 12, column=7)
    btnCancelar = Button(frmA, text="Cancelar", command=frmA.destroy).grid(row= 12, column=10)
    btnBorrar = Button(frmA, text="Borrar",  command=borrarTrabajador).grid(row= 13, column=10)
    
    
# Crear menu de opciones del dashboard
menubar = Menu(vent)

# Construimos opciones del menu
menutrab = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Trabajadores", menu=menutrab)

menutrab.add_command(label="Agregar", command=AgregarFrm)
#menutrab.add_command(label="Buscar", command=agregarTrabajador)
menutrab.add_command(label="Buscar", command=buscarTrabajador)
menutrab.add_command(label="Borrar", command=borrarTrabajador)


# Dibujar el menu para los reportes
menurep = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Reportes", menu=menurep)
menurep.add_command(label="Pantalla", command="mensaje")
menurep.add_command(label="PDF", command="mensaje")

# Dibujar el menu para salir de la app
menusalir = Menu(menubar, tearoff=0)
menubar.add_cascade(label="¿Quienes somos?", menu=menusalir)

menusalir.add_command(label="Créditos", command="mensaje")
menusalir.add_command(label="Salir", command=salir)

# display the menu
vent.config(menu=menubar)
# mostramos ventana
vent.mainloop()
