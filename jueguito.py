from email import message
import tkinter
from tkinter import messagebox

ventana=tkinter.Tk()
ventana.geometry("360x300")
etiqueta=tkinter.Label(ventana, text=("GUAYABITA"))

etiqueta.pack(fill=tkinter.X)





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
