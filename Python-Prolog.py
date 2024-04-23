#Carlos Nicolás Osorio Sagaró
#FITIB

from tkinter import Entry
from pyswip import Prolog
import tkinter as tk

prolog = Prolog() 
prolog.consult("c:/Users/Pc/Desktop/Tanque_de_Agua.pl")  # Direccion donde esta el .PL

# Función para enviar la consulta a Prolog y mostrar el resultado en la interfaz gráfica
def Comprobar():
    nombre1 = entry_nombre1.get()  # Obtener el dato ingresado para tanque_poca_agua
    nombre2 = entry_nombre2.get()  # Obtener el dato ingresado para cisterna_poca_agua
    nombre3 = entry_nombre3.get()  # Obtener el dato ingresado para turbina
    nombre4 = entry_nombre4.get()  # Obtener el dato ingresado para taque_lleno

    #X para tanque_poca_agua
    #Y para cisterna_poca_agua
    #T para turbina
    #Z para taque_lleno

    #Regla:
    #encender_turbina( X, Y, T, Z)

    # Consultar si se cumple la Regla
    resultado = list(prolog.query(f"encender_turbina({nombre1}, {nombre2}, {nombre3}, {nombre4})"))

    # if not : es porque es mas probale un error
    # Mostrar el resultado en la interfaz gráfica
    if not resultado:
        resultado_label.config(text=" No se Cumple Turbina Apagada")

    # Mostrar el resultado en la interfaz gráfica
    else:
        resultado_label.config(text=f' Se Cumple Turbina Encendida')


# La interfaz gráfica
root = tk.Tk()
root.title("Sensores de Tanque de Agua")

nombre4_label = tk.Label(root, text="Sensores")
nombre4_label.pack()


# Etiquetas y entradas para  la consulta
# Ojo solo se debe responder: apagado  o  encendido
nombre1_label = tk.Label(root, text="tanque con poca agua:")
nombre1_label.pack()
entry_nombre1 = tk.Entry(root)
entry_nombre1.pack()

nombre2_label = tk.Label(root, text="cisterna con poca agua:")
nombre2_label.pack()
entry_nombre2 = tk.Entry(root)
entry_nombre2.pack()

nombre3_label = tk.Label(root, text="turbina:")
nombre3_label.pack()
entry_nombre3 = tk.Entry(root)
entry_nombre3.pack()

nombre4_label = tk.Label(root, text="tanque lleno:")
nombre4_label.pack()
entry_nombre4 = tk.Entry(root)
entry_nombre4.pack()

# Botón para Comprobar estado del Sistema
consultar_button = tk.Button(root, text="Consultar", command=Comprobar)
consultar_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack()

root.mainloop()

# Nicolás :)
