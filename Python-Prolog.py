from pyswip import Prolog

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
    resultado = list(prolog.query("apagar_turbina({x}, {y}, {t})"))

    # Mostrar el resultado en la interfaz gráfica
    if resultado:
        print("Apagar Turvina")
    else:
        print("Error")


# Función 1 para consultar a Prolog
def control_turvina_1(x,y,z,t):
   
    # Consultar la relación de parentesco
    resultado = list(prolog.query("encender_turbina({x}, {y}, {z})"))

    # Mostrar el resultado en la interfaz gráfica
    if resultado:
        print("Encender Turvina ")
    else:
        control_turvina_2(x,y,t)

def preguntar(): #Funcion para preguntar
  boton=""

  while boton!="s" or boton!="n":
   boton = str(input("Precione (s) para encendido o  (n) para apagado ?"))
   if boton == "s":
    return "encendido"

   elif boton == "n":
    return "apagado"


#main

print("El sensor de tanque poca agua ?")
x=preguntar()# tanque_poca_agua
print(x)
print("El sensor de la cisterna poca agua ?")
y=preguntar() # cisterna_poca_agua
print(y)
print("El sensor de la turbina esta ?")
z=preguntar() # turbina
print(z)
print("El sensor del taque lleno ?")
t=preguntar() # taque_lleno
print(t)

control_turvina_1(x,y,z,t)

#Nicolás :)

