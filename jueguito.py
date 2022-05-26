from email import message
import tkinter
from tkinter import messagebox

ventana=tkinter.Tk()
ventana.geometry("360x300")
etiqueta=tkinter.Label(ventana, text=("GUAYABITA"))

etiqueta.pack(fill=tkinter.X)

def jugador1():
    def cyg():
        x=cajatextonombre.get()
        y=cajatextoplata.get()
        jugadores["a"]["nombre"]=x
        jugadores["a"]["plata"]=y
        pl=int(y)
        print(jugadores)
        if (pl >=200):
            j1.withdraw()
        else:
            messagebox.showerror("Error","Su dinero total debe ser mayor a $200")
    
    j1=tkinter.Toplevel()
    j1.geometry("380x300")
    j1.config(background="chocolate")
    tj1=tkinter.Label(j1,text="hola jugador 1")
    tj1.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)
    nombre=tkinter.Label(j1,text="Nombre:")
    nombre.place(relx=0.1,rely=0.4)
    cajatextonombre=tkinter.Entry(j1)
    cajatextonombre.place(relx=0.3,rely=0.4)
    boton=tkinter.Button(j1,text="ok",command=cyg)
    boton.pack(side=tkinter.BOTTOM)
    tj1p=tkinter.Label(j1,text="Ingrese su dinero total")
    tj1p.place(relx=0.1,rely=0.5)
    cajatextoplata=tkinter.Entry(j1)
    cajatextoplata.place(relx=0.5,rely=0.5)
    
    [20:28] ROBERT ARTURO JAIME NIETO
    def jugador2():
def cyg():
        x=cajatextonombre.get()
        y=cajatextoplata.get()
        jugadores["b"]["nombre"]=x
        jugadores["b"]["plata"]=y
        pl=int(y)
        print(jugadores)
if (pl >=200):
            j2.withdraw()
else:
            messagebox.showerror("Error","Su dinero total debe ser mayor a $200")
    j2=tkinter.Toplevel()
    j2.geometry("380x300")
    j2.config(background="peru")
    tj2=tkinter.Label(j2,text="hola jugador 2")
    tj2.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)
    nombre=tkinter.Label(j2,text="Nombre:")
    nombre.place(relx=0.1,rely=0.4)
    cajatextonombre=tkinter.Entry(j2)
    cajatextonombre.place(relx=0.3,rely=0.4)
    boton=tkinter.Button(j2,text="ok",command=cyg)
    boton.pack(side=tkinter.BOTTOM)
    tj2p=tkinter.Label(j2,text="Ingrese su dinero total")
    tj2p.place(relx=0.1,rely=0.5)
    cajatextoplata=tkinter.Entry(j2)
    cajatextoplata.place(relx=0.5,rely=0.5)
​[20:28] ROBERT ARTURO JAIME NIETO
    def jugador3():
def cyg():
        x=cajatextonombre.get()
        y=cajatextoplata.get()
        pl=int(y)
        jugadores["c"]["nombre"]=x
        jugadores["c"]["plata"]=y
        print(jugadores)
if (pl >=200):
            j3.withdraw()
else:
            messagebox.showerror("Error","Su dinero total debe ser mayor a $200")

    j3=tkinter.Toplevel()
    j3.geometry("380x300")
    j3.config(background="gold")
    tj3=tkinter.Label(j3,text="hola jugador 3")
    tj3.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)
    nombre=tkinter.Label(j3,text="Nombre:")
    nombre.place(relx=0.1,rely=0.4)
    cajatextonombre=tkinter.Entry(j3)
    cajatextonombre.place(relx=0.3,rely=0.4)
    boton=tkinter.Button(j3,text="ok",command=cyg)
    boton.pack(side=tkinter.BOTTOM)
    tj3p=tkinter.Label(j3,text="Ingrese su dinero total")
    tj3p.place(relx=0.1,rely=0.5)
    cajatextoplata=tkinter.Entry(j3)
    cajatextoplata.place(relx=0.5,rely=0.5)

#botones inicio y reglas
def reglas():
    
    r=tkinter.Toplevel()
    r.geometry("500x400")
    r.config(background="gold")
    tr=tkinter.Label(r,text="reglas")
    tr.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)
    reg=tkinter.Label(r,text="Regla 1. Todos los jugadores deben poner un minimo inicial de $200 ")
    reg2=tkinter.Label(r,text="Regla2. Al sacar el numero 1 y 6 se deben poner $200")
    reg3=tkinter.Label(r,text="Regla3. El juego acaba cuando dos jugadores se queden con menos de $200")
    reg4=tkinter.Label(r,text="Regla4. Solo se pueden apostar los siguientes valores:$100 $200 y $500")
    reg.pack(fill=tkinter.X,padx=5,ipadx=5,ipady=5)
    reg2.pack(fill=tkinter.X,padx=5,ipadx=5,ipady=5)
    reg3.pack(fill=tkinter.X,padx=5,ipadx=5,ipady=5)
    reg4.pack(fill=tkinter.X,padx=5,ipadx=5,ipady=5)
    boton=tkinter.Button(r,text="ok",command=r.destroy)
    boton.pack(side=tkinter.BOTTOM)

bregla=tkinter.Button(ventana,command=reglas,text="reglas",bg="blue",fg="white")
bregla.place(relx=0.6,rely=0.7)
#Boton juego 

def inicio():
    ventana.withdraw()
    ini=tkinter.Toplevel()
    ini.geometry("380x300")
    ini.config(background="light cyan")
    tini=tkinter.Label(ini,text="aqui va el juego",bg="light cyan")
    tini.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)
    

bini=tkinter.Button(ventana,command=inicio,text="Jugar",bg="green",fg="white")
bini.place(relx=0.3,rely=0.7)


jugadores={
    "a":{
        "nombre":"",
        "plata":"",
        "apuesta":"",
    },
    "b":{
        "nombre":"",
        "plata":"",
        "apuesta":"",
    },
    "c":{
        "nombre":"",
        "plata":"",
        "apuesta":"",
    },
}
