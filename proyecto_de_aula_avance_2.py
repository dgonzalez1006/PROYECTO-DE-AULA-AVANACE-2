# -*- coding: utf-8 -*-
"""PROYECTO DE AULA AVANCE 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UNZy-LNqhPQ1FNsog00iqXVf1vTRMh6K
"""

# Simulacion del sistema
import os

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, ID, correo, carrera):
        self.nombre = nombre
        self.ID = ID
        self.correo = correo
        self.carrera = carrera
        self.historialCursos = []

    def actualizarDatos(self, nuevo_nombre, nuevo_correo):
        self.nombre = nuevo_nombre
        self.correo = nuevo_correo
        print(f"Datos actualizados: {self.nombre}, {self.correo}")

    def verHistorial(self):
        if not self.historialCursos:
            print("No hay cursos en el historial.")
        else:
            for curso in self.historialCursos:
                print(f"{curso.nombre} - {curso.semestre}")

    def agregarCurso(self, curso):
        self.historialCursos.append(curso)

# Clase Curso
class Curso:
    def __init__(self, nombre, codigo, creditos, semestre):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.semestre = semestre

    def mostrarDetalles(self):
        print(f"{self.nombre} ({self.codigo}) - Créditos: {self.creditos}, Semestre: {self.semestre}")

# Clase Noticia
class Noticia:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion

    def mostrarNoticia(self):
        print(f"Noticia: {self.titulo}\nDescripción: {self.descripcion}")

# Clase Sistema (gestión del sistema)
class Sistema:
    def __init__(self):
        self.listaEstudiantes = []
        self.listaCursos = []
        self.listaNoticias = []

    def gestionarEst(self, estudiante):
        self.listaEstudiantes.append(estudiante)

    def gestionarCursos(self, curso):
        self.listaCursos.append(curso)

    def gestionarNoticias(self, noticia):
        self.listaNoticias.append(noticia)

# Crear una función para limpiar la pantalla (sin os.system)
def limpiar_pantalla():
    # usamos saltos de línea
    print("\n" * 100)

# Agregamos datos de prueba al sistema
sistema = Sistema()

# Crear estudiantes de prueba
est1 = Estudiante("Juan Pérez", "12345", "juan.perez@unab.edu", "Ingeniería")
est2 = Estudiante("Ana Gómez", "67890", "ana.gomez@unab.edu", "Administración")

# Agregar cursos al historial de los estudiantes
curso1 = Curso("Matemáticas", "MAT101", 3, "1er semestre")
curso2 = Curso("Programación", "PRG202", 4, "2do semestre")

est1.agregarCurso(curso1)
est2.agregarCurso(curso2)

# Agregar estudiantes y cursos al sistema
sistema.gestionarEst(est1)
sistema.gestionarEst(est2)
sistema.gestionarCursos(curso1)
sistema.gestionarCursos(curso2)

# Menú principal
def menu():
    print('''
        |V| _ __
        | |(/| |||
    ''')
    # Mostrar el menú
    print("Por favor seleccione una opción:")
    print("\t1- Ver historial de calificaciones")
    print("\t2- Cursos disponibles")
    print("\t3- Actualización de datos de estudiante")
    print("\t4- Validación de requisitos para graduación")
    print("\t5- Buzón de sugerencias")
    print("\t0- Salir")

# Inicio del programa
print("     /)    /)")
print("     (｡•ㅅ•｡)〝₎₎ Bienvenid@! ✦₊")
print("      ╭∪─∪────────── ✦ ⁺")

input("SISTEMA DE GESTIÓN DE CRÉDITOS\nPulsa una tecla para iniciar sesión")
usuario = input("Usuario: ")
password = input("Contraseña: ")

while True:
    limpiar_pantalla()
    menu()
    opcion = input("Por favor inserta un número >> ")

    if opcion == "1":
        print("Elegiste la opción 1: Ver historial de calificaciones")
        estudiante_nombre = input("Ingrese el nombre del estudiante: ")
        for est in sistema.listaEstudiantes:
            if est.nombre == estudiante_nombre:
                est.verHistorial()
        input("Pulsa una tecla para continuar")

    elif opcion == "2":
        print("Elegiste la opción 2: Cursos disponibles")
        for curso in sistema.listaCursos:
            curso.mostrarDetalles()
        input("Pulsa una tecla para continuar")

    elif opcion == "3":
        print("Elegiste la opción 3: Actualización de datos de estudiante")
        estudiante_nombre = input("Ingrese el nombre del estudiante: ")
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nuevo_correo = input("Ingrese el nuevo correo: ")
        for est in sistema.listaEstudiantes:
            if est.nombre == estudiante_nombre:
                est.actualizarDatos(nuevo_nombre, nuevo_correo)
        input("Pulsa una tecla para continuar")

    elif opcion == "4":
        print("Elegiste la opción 4: Validación de requisitos para graduación")
        estudiante_nombre = input("Ingrese el nombre del estudiante: ")
        for est in sistema.listaEstudiantes:
            if est.nombre == estudiante_nombre:
                total_creditos = sum([curso.creditos for curso in est.historialCursos])
                if total_creditos >= 120:  # Ejemplo de requisito de créditos
                    print("Cumple con los requisitos para graduación.")
                else:
                    print(f"Créditos actuales: {total_creditos}. Aún no cumple con los requisitos.")
        input("Pulsa una tecla para continuar")

    elif opcion == "5":
        print("Elegiste la opción 5: Buzón de sugerencias")
        sugerencia = input("Ingrese su sugerencia: ")
        print(f"Gracias por su sugerencia: {sugerencia}")
        input("Pulsa una tecla para continuar")

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("No elegiste una opción válida.")
        input("Pulsa una tecla para continuar")

