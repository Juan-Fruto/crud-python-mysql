"""
Nombre: dashboard.py
Objetivo: construye la ventana principal de la aplicación de base de datos.
Autor: alumnos de SO
Fecha: 07/10/2022
"""

from tkinter import *
from tkinter import ttk
import pymysql

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


"""
Función para Salir de la App
"""
def salir():
    print("*** Fin del sistema")
    vent.destroy()

    
def guardarDatos():
    print("")
 

def cancelar():
    print("")

"""
Método para Agregar Trabajadores a la base de Datos

"""    
def AgregarFrm():
    # invocar formulario
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
    
# def cancelar():
#     frmA.destroy()
  

"""
Método para buscar trabajadores
"""
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
menutrab.add_command(label="Agregar", command=AgregarFrm)
#menutrab.add_command(label="Buscar", command=agregarTrabajador)
menutrab.add_command(label="Buscar", command=buscarTrabajador)
menutrab.add_command(label="Borrar", command=borrarTrabajador)
menubar.add_cascade(label="Trabajadores", menu=menutrab)

# Dibujar el menu para los reportes
menurep = Menu(menubar, tearoff=0)
menurep.add_command(label="Pantalla", command="mensaje")
menurep.add_command(label="PDF", command="mensaje")
menubar.add_cascade(label="Reportes", menu=menurep)

# Dibujar el menu para salir de la app
menusalir = Menu(menubar, tearoff=0)
menusalir.add_command(label="Créditos", command="mensaje")
menusalir.add_command(label="Salir", command=salir)
menubar.add_cascade(label="¿Quienes somos?", menu=menusalir)

# display the menu
vent.config(menu=menubar)
# mostramos ventana
vent.mainloop()
