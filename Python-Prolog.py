# Carlos Nicolás Osorio Sagaró
# FITIB

from tkinter import Entry, Checkbutton
from pyswip import Prolog
import tkinter as tk

prolog = Prolog()
prolog.consult("c:/Users/Pc/Desktop/Tanque_de_Agua.pl")  # Direccion donde esta el .PL

# Función para enviar la consulta a Prolog y mostrar el resultado en la interfaz gráfica
def Comprobar():
    nombre1 = v1.get()  # Obtener el dato ingresado para tanque_poca_agua
    nombre2 = v2.get()  # Obtener el dato ingresado para cisterna_poca_agua
    nombre3 = v3.get()  # Obtener el dato ingresado para turbina
    nombre4 = v4.get()  # Obtener el dato ingresado para tanque_lleno

    # X para tanque_poca_agua
    # Y para cisterna_poca_agua
    # T para turbina
    # Z para tanque_lleno

    # Regla:
    # encender_turbina( X, Y, T, Z)

    # Consultar si se cumple la Regla
    resultado = list(prolog.query(f"encender_turbina({nombre1}, {nombre2}, {nombre3}, {nombre4})"))

    # if not : es porque es mas probale un error
    # Mostrar el resultado en la interfaz gráfica
    if not resultado:
        resultado_label.config( bg="red", text=" No se Cumple Turbina Apagada")

    # Mostrar el resultado en la interfaz gráfica
    else:
        resultado_label.config( bg="green", text=f' Se Cumple Turbina Encendida')


# La interfaz gráfica
root = tk.Tk()
root.geometry("270x370+50+50")


v1= tk.StringVar()
v2= tk.StringVar()
v3= tk.StringVar()
v4= tk.StringVar()

root.title("Sensores de Tanque de Agua")

nombre5_label = tk.Label(root, text="Sensores")
nombre5_label.pack()

# Etiquetas y entradas para  la consulta
# Ojo solo: apagado  o  encendido
nombre1_label = tk.Label(root, bg="gold", text="tanque con poca agua:")
nombre1_label.pack()

nombre1_label = tk.Radiobutton(root, text="apagado", variable=v1, value="apagado").pack()
nombre1_label = tk.Radiobutton(root, text="encendido", variable=v1, value="encendido").pack()

nombre2_label = tk.Label(root, bg="gold", text="cisterna con poca agua:")
nombre2_label.pack()

nombre2_label = tk.Radiobutton(root, text="apagado", variable=v2, value="apagado").pack()
nombre2_label = tk.Radiobutton(root, text="encendido", variable=v2, value="encendido").pack()


nombre3_label = tk.Label(root, bg="gold", text="turbina:")
nombre3_label.pack()

nombre3_label = tk.Radiobutton(root, text="apagado", variable=v3, value="apagado").pack()
nombre3_label = tk.Radiobutton(root, text="encendido", variable=v3, value="encendido").pack()


nombre4_label = tk.Label(root, bg="gold", text="tanque lleno:").pack()

nombre4_label = tk.Radiobutton(root, text="apagado", variable=v4, value="apagado").pack()
nombre4_label = tk.Radiobutton(root, text="encendido", variable=v4, value="encendido").pack()


# Botón para Comprobar estado del Sistema
consultar_button = tk.Button(root, text="Consultar", command=Comprobar)
consultar_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack()

root.mainloop()

# Nicolás :)
