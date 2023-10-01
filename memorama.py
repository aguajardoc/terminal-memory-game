import time
import numpy
import random

# Imprimir el prompt hasta que el usuario decida jugar
def inicio():
    while True:
        empezar = input("¿Quieres jugar al memorama? (y/n): ")
        if empezar == "y":
            return 0
        else:
            exit() # Salir si no quiere jugar :(

def leerReglas():
    while True:
        leerReglas = input("¿Quieres leer las reglas antes de comenzar? (y/n): ")
        if leerReglas == "y":
            return 1 # Lee las reglas
        elif leerReglas == "n":
            return 0 # Se salta la función de reglas y empieza el juego
        else:
            continue

def reglas():
    while True:
        print("\n\n¡Bienvenido al Memorama!\nEl número de jugadores se limita a 1.\nSe presentará un tablero de cartas en un arreglo 6x6 en el que se esconden pares de elementos.\nTu objetivo: encontrar todos los pares.\nCada turno, podrás seleccionar dos cartas.\nSi estas forman un par, se removerán del tablero y ¡estarás más cerca de ganar!\nPero si no forman un par, se regresarán a su posición inicial para que lo vuelvas a intentar.\n")
        rEmpezar = input("¡¿Estás listo para jugar!? (y/n): ")
        if rEmpezar == "y":
            return 1 # Empieza el juego
        elif rEmpezar == "n":
            exit() # Salir si no quiere jugar :(
        else:
            continue

def juego():
    cargando = "cargando"

    # Generar una matriz 6x6 con valores aleatorios
    valoresRandom = numpy.full(36,0)
    valoresIndexados = numpy.full(36,-1)

    # Llenar los espacios
    for i in range(18):

        # Escoger una casilla random hasta encontrar una que no ha sido usada
        while True:
            index = random.randint(0,35)
            if index not in valoresIndexados:
                valoresIndexados[i] = index
                break

        # Generar un valor aleatorio hasta encontrar uno que no haya sido usado y asignarlo a la casilla encontrada previamente
        while True:
            casilla = random.randint(10,99)
            if casilla not in valoresRandom:
                valoresRandom[index] = casilla
                break
        
        # Hacer su par en otra casilla random
        while True:
            otros18 = random.randint(0,35)
            if otros18 not in valoresIndexados:
                valoresIndexados[35-i] = otros18
                valoresRandom[otros18] = casilla
                break
        
        # Evitar que el usuario se aburra si la generación tarda mucho
        if i%6 == 0:
            cargando += "."
            print(cargando)
        
        
    # Están guardados los índices, pero creo que sería más lógico comparar los valores que existen en esas dos casillas para identificar su paridad

    tablero = numpy.zeros((6,6))
    tableroEscondido = numpy.asmatrix(valoresRandom).reshape(6,6)

    # Comenzar el juego
    print("\nEl juego comienza en: ")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1\n")
    time.sleep(1)

    print(numpy.matrix(tablero),"\n")
    #TODO: inputs
    
# TERMINAN FUNCIONES ------------------------------------------

# Iniciar el juego
principio = inicio() 

# Preguntarle si quiere leer las reglas
if principio == 0:
    opcionLeerReglas = leerReglas()

# Si quiere leer las reglas, las muestra
if opcionLeerReglas == 1:
    opcionReglas = reglas() 

# Si no quiso leer las reglas, o si ya las leyó, empieza el juego
if opcionLeerReglas == 0 or opcionReglas == 1: 
    juego()