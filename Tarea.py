# Clase Estudiante para almacenar la información de cada estudiante
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asignaturas = {}

    def agregar_asignatura(self, asignatura):
        self.asignaturas[asignatura.nombre] = asignatura

    def promedio_general(self):
        if not self.asignaturas:
            return 0
        return sum(asig.promedio() for asig in self.asignaturas.values()) / len(self.asignaturas)

    def reporte_estudiante(self):
        print(f"Reporte del Estudiante: {self.nombre}")
        for asig in self.asignaturas.values():
            print(f"Asignatura: {asig.nombre}, Promedio: {asig.promedio():.2f}, Aprobado: {'Sí' if asig.aprobado() else 'No'}")
        print(f"Promedio General: {self.promedio_general():.2f}")

# Clase Asignatura para almacenar la información de cada asignatura
class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []
        self.asistencia = []

    def agregar_calificacion(self, nota):
        if 2 <= nota <= 5:
            self.calificaciones.append(nota)
        else:
            print("Nota inválida. Debe ser un entero entre 2 y 5.")

    def agregar_asistencia(self, presente):
        self.asistencia.append(presente)

    def promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0

    def aprobado(self):
        return self.promedio() >= 3 and all(self.asistencia)

# Funciones para interactuar con el usuario
def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiantes[nombre] = Estudiante(nombre)

def asignar_asignatura(estudiantes):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
    if nombre_estudiante in estudiantes:
        estudiantes[nombre_estudiante].agregar_asignatura(Asignatura(nombre_asignatura))
    else:
        print("Estudiante no encontrado.")

def agregar_calificacion(estudiantes):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
    if nombre_estudiante in estudiantes and nombre_asignatura in estudiantes[nombre_estudiante].asignaturas:
        nota = int(input("Ingrese la calificación: "))
        estudiantes[nombre_estudiante].asignaturas[nombre_asignatura].agregar_calificacion(nota)
    else:
        print("Estudiante o asignatura no encontrada.")

def agregar_asistencia(estudiantes):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
    if nombre_estudiante in estudiantes and nombre_asignatura in estudiantes[nombre_estudiante].asignaturas:
        presente = input("El estudiante asistió a clase? (s/n): ").lower() == 's'
        estudiantes[nombre_estudiante].asignaturas[nombre_asignatura].agregar_asistencia(presente)
    else:
        print("Estudiante o asignatura no encontrada.")

def reporte_general(estudiantes):
    for est in estudiantes.values():
        est.reporte_estudiante()

# Programa principal
def main():
    estudiantes = {}
    while True:
        print("\nMenú de gestión de estudiantes")
        print("1. Agregar estudiante")
        print("2. Asignar asignatura a estudiante")
        print("3. Agregar calificación")
        print("4. Agregar asistencia")
        print("5. Reporte general de estudiantes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_estudiante(estudiantes)
        elif opcion == '2':
            asignar_asignatura(estudiantes)
        elif opcion == '3':
            agregar_calificacion(estudiantes)
        elif opcion == '4':
            agregar_asistencia(estudiantes)
        elif opcion == '5':
            reporte_general(estudiantes)
        elif opcion == '6':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
