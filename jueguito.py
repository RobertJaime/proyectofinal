from email import message
from re import A
import tkinter
from tkinter import messagebox
from typing import Text
import random

ventana=tkinter.Tk()
ventana.geometry("360x300")
etiqueta=tkinter.Label(ventana, text=("GUAYABITA"),bg="blue")

etiqueta.pack(fill=tkinter.X)



# botones jugadores input nombre plata
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
    j1.config(background="plum2")
    tj1=tkinter.Label(j1,text="hola jugador 1")
    tj1.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)
    nombre=tkinter.Label(j1,text="Nombre:")
    nombre.place(relx=0.1,rely=0.4)
    cajatextonombre=tkinter.Entry(j1)
    cajatextonombre.place(relx=0.3,rely=0.4)
    boton=tkinter.Button(j1,text="aceptar",command=cyg)
    boton.pack(side=tkinter.BOTTOM)
    tj1p=tkinter.Label(j1,text="Ingrese su dinero total")
    tj1p.place(relx=0.1,rely=0.5)
    cajatextoplata=tkinter.Entry(j1)
    cajatextoplata.place(relx=0.5,rely=0.5)

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

def jugador3():
    def cyg():
        x=cajatextonombre.get()
        y=cajatextoplata.get()
        pl=int(y)
        jugadores["c"]["nombre"]=x
        jugadores["c"]["plata"]=y
        print(jugadores)
        if (pl >=200):
            j3.destroy()
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



#botones inicio pestañas jugadores info
boton1=tkinter.Button(ventana,command=jugador1,text="jugador 1")
boton2=tkinter.Button(ventana,command=jugador2,text="jugador 2")
boton3=tkinter.Button(ventana,command=jugador3,text="jugador 3")


boton1.place(relx=0.1,rely=0.5)
boton2.place(relx=0.45,rely=0.5)
boton3.place(relx=0.8,rely=0.5)
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


    
    pl1=int(jugadores["a"]["plata"])
    pl2=int(jugadores["b"]["plata"])
    pl3=int(jugadores["c"]["plata"])

        


    if (pl1!=0 and pl2!=0 and pl3!=0):
        ventana.withdraw()
        ini=tkinter.Toplevel()
        ini.geometry("700x450")
        ini.config(background="light cyan")
        tini=tkinter.Label(ini,text="aqui va el juego",bg="light cyan")
        tini.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)
        #info jugadores
        turno_jugador1=tkinter.Label(ini,text="TURNO DEL JUGADOR 1 😎",font=("Helvetica",10))
        turno_jugador1.place(relx=0.4,rely=0.2)       

        a=jugadores["a"]["nombre"]
        b=jugadores["b"]["nombre"]
        c=jugadores["c"]["nombre"]

        

        p1=jugadores["a"]["plata"]
        p2=jugadores["b"]["plata"]
        p3=jugadores["c"]["plata"]

        pini1=int(p1)-200
        pini2=int(p2)-200
        pini3=int(p3)-200

        jugadores["a"]["plata"]=pini1
        jugadores["b"]["plata"]=pini2
        jugadores["c"]["plata"]=pini3
        
        print(pini1,pini2,pini3)
        
        #nombres y dinero en bolsillo
        nombre1=tkinter.Label(ini,text=a)
        nombre2=tkinter.Label(ini,text=b)
        nombre3=tkinter.Label(ini,text=c)

        plata1=tkinter.Label(ini,text=pini1)
        plata2=tkinter.Label(ini,text=pini2)
        plata3=tkinter.Label(ini,text=pini3)

        nombre1.place(relx=0.1,rely=0.8)
        nombre2.place(relx=0.45,rely=0.8)
        nombre3.place(relx=0.8,rely=0.8)

        plata1.place(relx=0.1,rely=0.84)
        plata2.place(relx=0.45,rely=0.84)
        plata3.place(relx=0.8,rely=0.84)
        #boton resta
        def resta():
            a1=int(jugadores["a"]["plata"])
            a2=a1-1
            jugadores["a"]["plata"]=a2
            plata1["text"]=a2
            print(jugadores)
        restar=tkinter.Button(ini,command=resta,text="restar")
        restar.place(relx=0.8,rely=0.5)
    #valentina
    #descuento dinero cuando saque 1 o 6 
        #boton dado
        
        def dado():
            pm=int(jugadores["mesa"]["plata"])

            pj1=jugadores["a"]["plata"]
            pj2=jugadores["b"]["plata"]
            pj3=jugadores["c"]["plata"]

            
            if pm<=0:
                messagebox.showinfo("fin del juego","no queda plata en la mesa el ganador es..")
                ini.destroy
            if (pj1<=0 or pj2<=0 or pj3<=0):
                messagebox.showinfo("fin del juego","el juego a terminado")
                ini.destroy

            turno=jugadores["dado"]["turno"]
            turint=int(turno)

            
            
            

            d=random.randint(1,6)
            ap1=jugadores["a"]["apuesta"]
            ap2=jugadores["b"]["apuesta"]
            ap3=jugadores["c"]["apuesta"]

            pm=int(jugadores["mesa"]["plata"])
            platamesa["text"]=f"Dinero en la mesa: ${pm}"
            plata1["text"]=jugadores["a"]["plata"]
            plata2["text"]=jugadores["b"]["plata"]
            plata3["text"]=jugadores["c"]["plata"]

            if ((turno==0 or turno==1 or turno==6) and (d==1 or d==6) ) :                    
                if turno==6:
                    mg=pm+200
                    jp_1=pj1-200
                    jugadores["a"]["plata"]=jp_1
                    messagebox.showinfo("pierdes","jugador 1 pones 200")  

                    jugadores["mesa"]["plata"]=mg

                elif turno==1:
                    mg=pm+200
                    jp_2=pj2-200
                    jugadores["b"]["plata"]=jp_2
                    messagebox.showinfo("pierdes","jugador 2 pones 200")  
                    jugadores["mesa"]["plata"]=mg
                    

                elif((turno==3) and (d==1 or d==5)):
                    messagebox.showinfo("pierdes","jugador 3 pones 200")
                    mg=pm+200
                    jp_3=pj3-200
                    jugadores["c"]["plata"]=jp_3

                    jugadores["mesa"]["plata"]=mg
                            
            else:
                if turno==0  or turno==5:
                    turno_jugador1=tkinter.Label(ini,text="TURNO DEL JUGADOR 1 😎",font=("Helvetica",10))
                    turno_jugador1.place(relx=0.4,rely=0.2)
                    
                    
                    if d>jugadores["dado"]["numero"] and turno==0:
                        messagebox.showinfo("GANASTE",f"Ganaste toma{ap1}")
                        mg=pm-ap1
                        jugadores["mesa"]["plata"]=mg
                        j1p=pj1+ap1
                        jugadores["a"]["plata"]=j1p


                    if d<=jugadores["dado"]["numero"] and turno==1:
                        messagebox.showinfo("perdiste",f"Perdiste, pon en la mesa :{ap1}")
                        mg=pm+ap1
                        jugadores["mesa"]["plata"]=mg
                        j1p=pj1-ap1
                        jugadores["a"]["plata"]=j1p

                elif turno==1 or turno==2:
                    turno_jugador2=tkinter.Label(ini,text="TURNO DEL JUGADOR 2 😎",font=("Helvetica",10))
                    turno_jugador2.place(relx=0.4,rely=0.2)
                                    
                    if d>jugadores["dado"]["numero"] and turno==2:
                        messagebox.showinfo("GANASTE",f"Ganaste toma{ap2}")
                        mg=pm-ap2
                        j2p=pj2+ap2
                        jugadores["b"]["plata"]=j2p

                        jugadores["mesa"]["plata"]=mg
                    if d<=jugadores["dado"]["numero"] and turno==2:
                        messagebox.showinfo("perdiste",f"Perdiste, pon en la mesa :{ap2}")
                        mg=pm+ap2
                        j2p=pj2-ap2
                        jugadores["b"]["plata"]=j2p

                        jugadores["mesa"]["plata"]=mg

                elif turno==3 or turno==4:
                    turno_jugador3=tkinter.Label(ini,text="TURNO DEL JUGADOR 3 😎",font=("Helvetica",10))
                    turno_jugador3.place(relx=0.4,rely=0.2)
                                     
                    if d>jugadores["dado"]["numero"] and turno==4:
                        messagebox.showinfo("GANASTE",f"Ganaste toma{ap3}")
                        mg=pm-ap3
                        j3p=pj3+ap3
                        jugadores["c"]["plata"]=j3p
                        jugadores["mesa"]["plata"]=mg
                    if d<=jugadores["dado"]["numero"] and turno==4:
                        messagebox.showinfo("perdiste",f"Perdiste, pon en la mesa :{ap3}")
                        mg=pm+ap3
                        j3p=pj3-ap3
                        jugadores["c"]["plata"]=j3p
                        jugadores["mesa"]["plata"]=mg

                
                

            jugadores["dado"]["numero"]=d
            
            
            #turnos 
            if turint<=5:
                trn=turint+1
                jugadores["dado"]["turno"]=trn
                
            else:
                jugadores["dado"]["turno"]=1
            
            

            
            
            #mensaje apuesta
            #turno jugador 1
            if turno==1: 
                apj1=tkinter.Toplevel()
                apj1.geometry("300x100")
                apj1.config(background="gold")

                tapj1=tkinter.Label(apj1,text="apuesta jugador 2 💰💰💰")
                tapj1.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)

                tapj2=tkinter.Label(apj1,text="Cuanto desea apostar? :")
                tapj2.place(relx=0.1,rely=0.4)

                def ap100():
                    jugadores["b"]["apuesta"]=100
                    apj1.destroy()
                    print (jugadores)

                boton100=tkinter.Button(apj1,text="$100",command=ap100)
                boton100.place(relx=0.54,rely=0.4)

                
                def ap200():
                    jugadores["b"]["apuesta"]=200
                    apj1.destroy()
                    print (jugadores)

                boton200=tkinter.Button(apj1,text="$200",command=ap200)
                boton200.place(relx=0.67,rely=0.4)

                
                def ap500():
                    jugadores["b"]["apuesta"]=500
                    apj1.destroy()
                    print (jugadores)

                boton500=tkinter.Button(apj1,text="$500",command=ap500)
                boton500.place(relx=0.8,rely=0.4)

                a=jugadores["a"]["plata"]
                deb=tkinter.Label(apj1,text=f"Le queda {a} pesos")
                deb.place(relx=0.25,rely=0.8)

                def apostar():
                    apj1.destroy()

                
            #turno jugador 3  
            if turno==3 :
                apj2=tkinter.Toplevel()
                apj2.geometry("300x100")
                apj2.config(background="gold")

                tapj2=tkinter.Label(apj2,text="apuesta jugador 3 💰💰💰")
                tapj2.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)

                tapj2=tkinter.Label(apj2,text="Cuanto desea apostar? :")
                tapj2.place(relx=0.1,rely=0.4)

                def ap100():
                    jugadores["c"]["apuesta"]=100
                    apj2.destroy()
                    print (jugadores)

                boton100=tkinter.Button(apj2,text="$100",command=ap100)
                boton100.place(relx=0.54,rely=0.4)

                
                def ap200():
                    jugadores["c"]["apuesta"]=200
                    apj2.destroy()
                    print (jugadores)

                boton200=tkinter.Button(apj2,text="$200",command=ap200)
                boton200.place(relx=0.67,rely=0.4)

                
                def ap500():
                    jugadores["c"]["apuesta"]=500
                    apj2.destroy()
                    print (jugadores)

                boton500=tkinter.Button(apj2,text="$500",command=ap500)
                boton500.place(relx=0.8,rely=0.4)

                a=jugadores["b"]["plata"]
                deb=tkinter.Label(apj2,text=f"Le queda {a} pesos")
                deb.place(relx=0.25,rely=0.8)
                
                def apostar():
                    apj2.destroy()

                cerrar=tkinter.Button(apj2,text="¡Apostar!",command=apostar)
                cerrar.place(relx=0.8,rely=0.8)
            #turno jugador 1
            if turno==5 :
                apj3=tkinter.Toplevel()
                apj3.geometry("300x100")
                apj3.config(background="gold")

                tapj3=tkinter.Label(apj3,text="apuesta jugador 1 💰💰💰")
                tapj3.pack(padx=4,pady=5,ipadx=6,ipady=5,fill=tkinter.X)

                tapj2=tkinter.Label(apj3,text="Cuanto desea apostar? :")
                tapj2.place(relx=0.1,rely=0.4)

                def ap100():
                    jugadores["a"]["apuesta"]=100
                    apj3.destroy()
                    print (jugadores)

                boton100=tkinter.Button(apj3,text="$100",command=ap100)
                boton100.place(relx=0.54,rely=0.4)

                
                def ap200():
                    jugadores["a"]["apuesta"]=200
                    apj3.destroy()
                    print (jugadores)

                boton200=tkinter.Button(apj3,text="$200",command=ap200)
                boton200.place(relx=0.67,rely=0.4)

                
                def ap500():
                    jugadores["a"]["apuesta"]=500
                    apj3.destroy()
                    print (jugadores)

                boton500=tkinter.Button(apj3,text="$500",command=ap500)
                boton500.place(relx=0.8,rely=0.4)

                a=jugadores["c"]["plata"]
                deb=tkinter.Label(apj3,text=f"Le queda {a} pesos")
                deb.place(relx=0.25,rely=0.8)
                
                def apostar():
                    apj3.destroy()

                cerrar=tkinter.Button(apj3,text="¡Apostar!",command=apostar)
                cerrar.place(relx=0.8,rely=0.8)

                

            texdado=tkinter.Label(ini,text=d,font=("Helvetica",40))
            texdado.place(relx=0.5,rely=0.4)
            print(jugadores)
            
            
            
                   
        
        apuesta=tkinter.Button(ini,text="Tirar dados",command=dado)
        apuesta.place(relx=0.1,rely=0.5)
        #plata en la mesa
        pm=int(jugadores["mesa"]["plata"])
        platamesa=tkinter.Label(ini,text=f"Dinero en la mesa: ${pm}")
        platamesa.place(relx=0.45,rely=0.6)
        


                
    else:
         messagebox.showerror("Error","llene la informacion de los 3 jugadores")

bini=tkinter.Button(ventana,command=inicio,text="Jugar",bg="green",fg="white")
bini.place(relx=0.3,rely=0.7)

#codigo juego

jugadores={
    "a":{
        "nombre":"",
        "plata":"0",
        "apuesta":"",
    },
    "b":{
        "nombre":"",
        "plata":"0",
        "apuesta":"",
    },
    "c":{
        "nombre":"",
        "plata":"0",
        "apuesta":"",
    },
    "mesa":{
        "plata":"600"
    },
    "dado":{
        "numero":"",
        "turno":"0" ,       
    },
}
#Codigo dado por turnos de cada jugador 



    

print(jugadores)
ventana.mainloop()
