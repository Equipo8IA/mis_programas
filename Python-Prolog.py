from pyswip import Prolog
import tkinter as tk

#Nicolás

# Conectar con Prolog
prolog = Prolog()
prolog.consult("c:/Users/Pc/Desktop/Tanque_de_Agua.pl")  # Cargar base de conocimiento en Prolog

#variables
x=""# tanque_poca_agua
y=""# cisterna_poca_agua
z=""# turbina
t=""# taque_lleno

# Función 2 para consultar a Prolog
def control_turvina_2(x,y,t):
   
    # Consultar la relación de parentesco
    resultado = prolog.query(f"apagar_turbina({x}, {y}, {t})")

    # Mostrar el resultado en la interfaz gráfica
    if resultado:
        print("Apagar Turvina")
    else:
        print("Error")


# Función 1 para consultar a Prolog
def control_turvina_1(x,y,z,t):
   
    # Consultar la relación de parentesco
    resultado = prolog.query(f"encender_turbina({x}, {y}, {z})")

    # Mostrar el resultado en la interfaz gráfica
    if resultado:
        print("Encender Turvina ")
    else:
        control_turvina_2(x,y,t)

def preguntar(): #Funcion para preguntar
  boton=0

  while boton!=1 or boton!=2:
   boton = int(input("El sensor esta encendido o apagado ?"))
   if boton == 1:
    return "encendido"

   elif boton == 2:
    return "apagado"


#main

print("El tanque poca agua ?")
x=preguntar() # tanque_poca_agua
print("La cisterna poca agua ?")
y=preguntar() # cisterna_poca_agua
print("La turbina esta ?")
z=preguntar() # turbina
print("El taque lleno ?")
t=preguntar() # taque_lleno

control_turvina_1(x,y,z,t)

#Nicolás :)
