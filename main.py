from tkinter import *
from tkinter import ttk
import pymysql
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
        query = "SELECT * FROM workers"
        try:
            self.cursor.execute(query)
            users = self.cursor.fetchall()
            # for i in users:
            #     print("name", i[0])
            return users
        except Exception as error:
            print(error)
    
    def getUserById(self, id):
        query = "SELECT * FROM workers where id = {}".format(id)
        try:
            self.cursor.execute(query)
            user = self.cursor.fetchone()
            #lblMensaje.config(text = user)
        except Exception as error:
            print(error)
            return 0

    def setUser(self, user):
        print(user)
        try:
            print(type(user))
            print(user["id"]),
            print(user["nameWorker"]),
            print(user["phone"]),
            print(user["designation"]),
            print(user["salary"])
        except Exception as error:
            print("error from print method", error)
            pass
        
        query = "insert into workers values({}, {}, {}, {}, {})".format(
            user["id"],
            user["nameWorker"],
            user["phone"],
            user["designation"],
            5.2
            #float(user["salary"])
        )
        print("query:\n", query)
        try:
            self.cursor.execute(query)
        except Exception as error:
            print("erro from db method", error)

db = Database()
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
    id, name, phone, designation, salary = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

    lbId = Label(frmA , text="Id: ").grid(row= 2, column=2)
    inputId = Entry(frmA, width=10, textvariable=id).grid(row= 2, column=10)

    lbName = Label(frmA , text="Name: ").grid(row= 4, column=2)
    inputName =Entry(frmA, width=90, textvariable=name).grid(row= 4, column=10)

    lbPhone = Label(frmA , text="Phone: ").grid(row= 6, column=2)
    inputPhone =Entry(frmA, width=10, textvariable=phone).grid(row= 6, column=10)

    lbDesignation = Label(frmA , text="Designation: ").grid(row= 8, column=2)
    inputDesignation =Entry(frmA, width=20, textvariable=designation).grid(row= 8, column=10)

    lbSalary = Label(frmA , text="Salary: ").grid(row= 10, column=2)
    inputSalary =Entry(frmA, width=15, textvariable=salary).grid(row= 10, column=10)

    user = {"id": id.get(), "nameWorker": name.get(), "phone": phone.get(), "designation": designation.get(), "salary": salary.get()}
    
    btnGuardar = Button(frmA, text="Save", command = db.setUser(user)).grid(row= 12, column=7)    
    btnCancelar = Button(frmA, text="Cancel", command = frmA.destroy).grid(row= 12, column=10)

    
def buscarTrabajador():
    frmA = Toplevel(vent)
    frmA .geometry("800x600")
    frmA .title("Módulo Buscar trabajador")

    #vent.iconify()  
    lc = Label(frmA , text="Id: ").grid(row= 2, column=2)
    txtClave = Entry(frmA, width=5).grid(row= 2, column=10)
    btnGuardar = Button(frmA, text="Find by id", command=db.getUserById(txtClave)).grid(row= 12, column=7)
    btnCancelar = Button(frmA, text="Cancel", command=frmA.destroy).grid(row= 12, column=10)
    lblMensaje = Label(frmA).grid(row= 13, column=10)

def borrarTrabajador():
    frmA = Toplevel(vent)
    frmA .geometry("800x600")
    frmA .title("Módulo Borrar trabajador")

    #vent.iconify()  
    lc = Label(frmA , text="Id: ").grid(row= 2, column=2)
    txtClave = Entry(frmA, width=5).grid(row= 2, column=10)
    btnGuardar = Button(frmA, text="Find by id", command=guardarDatos).grid(row= 12, column=7)
    btnCancelar = Button(frmA, text="Cancel", command=frmA.destroy).grid(row= 12, column=10)
    btnBorrar = Button(frmA, text="Delete",  command=borrarTrabajador).grid(row= 13, column=10)
    
    
# Crear menu de opciones del dashboard
menubar = Menu(vent)

# Construimos opciones del menu
menuWorker = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Workers", menu=menuWorker)

menuWorker.add_command(label="Add", command=agregarTrabajador)
#menuWorker.add_command(label="Buscar", command=agregarTrabajador)
menuWorker.add_command(label="Search", command=buscarTrabajador)
menuWorker.add_command(label="Delete", command=borrarTrabajador)


# Dibujar el menu para los reportes
menuReport = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Reports", menu=menuReport)

menuReport.add_command(label="Screen list", command="mensaje")
menuReport.add_command(label="PDF", command="mensaje")

# Dibujar el menu para salir de la app
menuAbout = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Who we are?", menu=menuAbout)

menuAbout.add_command(label="Credits", command="mensaje")
menuAbout.add_command(label="Exit", command=salir)

# display the menu
vent.config(menu=menubar)

# mostramos ventana
vent.mainloop()
