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
#botones apuestas
        def apuesta_j1():
            apj1=tkinter.Toplevel()
            apj1.geometry("300x100")
            apj1.config(background="gold")

            tapj1=tkinter.Label(apj1,text="apuesta jugador 1 💰💰💰")
            tapj1.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)

            tapj2=tkinter.Label(apj1,text="Cuanto desea apostar? :")
            tapj2.place(relx=0.1,rely=0.4)

            cajatex=tkinter.Entry(apj1)
            cajatex.place(relx=0.57,rely=0.4)

            a=jugadores["a"]["plata"]
            deb=tkinter.Label(apj1,text=f"Le queda {a} pesos")
            deb.place(relx=0.25,rely=0.8)

            def apostar():
                apj1.destroy()

            cerrar=tkinter.Button(apj1,text="¡Apostar!",command=apostar)
            cerrar.place(relx=0.8,rely=0.8)

        j1_apuesta=tkinter.Button(ini,text="apuesta jugador 1",command=apuesta_j1)
        j2_apuesta=tkinter.Button(ini,text="apuesta jugador 2",)
        j3_apuesta=tkinter.Button(ini,text="apuesta jugador 3",)

        j1_apuesta.place(relx=0.1,rely=0.7)
        j2_apuesta.place(relx=0.45,rely=0.7)
        j3_apuesta.place(relx=0.8,rely=0.7)


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

#Dado
import random
#Apuestas

j1_dinero=int(input("Ingrese el valor inicial con el que jugara:"))
j2_dinero=int(input("Ingrese el valor inicial con el que jugara:"))
j3_dinero=int(input("Ingrese el valor inicial con el que jugara:"))

if j1_dinero and j3_dinero and j2_dinero<1000:
    print("No es posible jugar con un valor inicial menor a $1.000")
else:
    print("Listos para jugar")
#En mesa
mesa=int
jp1=j1_dinero-200
jp2=j2_dinero-200
jp3=j3_dinero-200
mesadinero=(200+200+200)
print ("En la mesa hay:", mesadinero)
print("Turno jugador 1...")

#Turno 1 
apuesta_inicial=(int)
queda1=(int)
d=random.randint(1,6)
d1=random.randint(1,6)
print("Tirando el dado...")
print(f"Numero:", d)
if (d==1 or d==6):
    print("Perdiste,Debe poner $200")
if (d==2 or 3 or 4 or 5):
    apuesta_inicial=int(input("Ingrese su apuesta:"))
    d1=random.randint(1,6)
    print("Tirando dado de nuevo...")
    print("Numero:",d1)
if (d1>d):
    print("GANASTE, Toma el dinero_apostado")
else:print("PERDISTE, Pon en la mesa el dinero_apostado")
mesa=int
mesa1=int
mesa2=int
mesa=mesadinero+200
mesa1=mesadinero+apuesta_inicial
mesa2=mesadinero-apuesta_inicial
if (mesa)<=0:
    print("El juego termino")
if j1_dinero or j2_dinero or j3_dinero==(j1_dinero+j2_dinero+j3_dinero):
    print("El juego termino")
if j1_dinero or j2_dinero or j3_dinero<=0:
    print("El juego termino")

if (d==1 or d==6):
    queda1=jp1-200
    print("Total:",queda1)
    print("Ahora en la mesa hay:", mesa)
if (d1>d):
    queda1=(jp1)+apuesta_inicial
    print("Tu total es de",queda1)
    print("Ahora en la mesa hay:",mesa2 )
else:
    queda1=(jp1)-apuesta_inicial
    print("Tu total es de:",queda1)
    print("Ahora en la mesa hay:",mesa1)

print("Es el turno del jugador 2")
