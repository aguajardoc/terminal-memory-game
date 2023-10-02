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
        
        
    # Están guardados los índices, pero creo que sería más lógico comparar los valores que existen en esas dos casillas para identificar su paridad

    tablero = numpy.zeros((6,6))
    tableroEscondido = numpy.asmatrix(valoresRandom).reshape(6,6)
    tableroVerifiacion = numpy.ones((6,6))

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

    while True:
        # Esperar un input de casilla 1 del jugador
        while True:
            casillaSeleccionadaX = int(input("Escriba las coordenadas de una casilla\nCoordenada-X:  "))
            casillaSeleccionadaY = int(input("Coordenada-Y: "))
            if casillaSeleccionadaX >= 1 and casillaSeleccionadaX <= 6 and casillaSeleccionadaY >= 1 and casillaSeleccionadaY <= 6 and tablero.item((casillaSeleccionadaX - 1, casillaSeleccionadaY - 1)) == 0:
                break
        
        # Mostrar valor de casilla 1
        numpy.put(tablero, casillaSeleccionadaY * 6 - (6 - casillaSeleccionadaX) - 1, tableroEscondido.item((casillaSeleccionadaX - 1, casillaSeleccionadaY - 1)))
        print("\n",tablero)

        # Esperar un input de casilla 2 del jugador
        while True:
            casillaSeleccionadaX2 = int(input("\nEscriba las coordenadas de otra casilla\nCoordenada-X:  "))
            casillaSeleccionadaY2 = int(input("Coordenada-Y: "))
            if casillaSeleccionadaX2 >= 1 and casillaSeleccionadaX2 <= 6 and casillaSeleccionadaY2 >= 1 and casillaSeleccionadaY2 <= 6 and (casillaSeleccionadaY2 != casillaSeleccionadaY or casillaSeleccionadaX != casillaSeleccionadaX2) and tablero.item((casillaSeleccionadaX2 - 1, casillaSeleccionadaY2 - 1)) == 0:
                break
        
        # Mostrar valor de casilla 2
        numpy.put(tablero, casillaSeleccionadaY2 * 6 - (6 - casillaSeleccionadaX2) - 1, tableroEscondido.item((casillaSeleccionadaX2 - 1, casillaSeleccionadaY2 - 1)))
        print("\n",tablero)

        # Verificar paridad
        if tableroEscondido.item((casillaSeleccionadaX - 1, casillaSeleccionadaY - 1)) == tableroEscondido.item((casillaSeleccionadaX2 - 1, casillaSeleccionadaY2 - 1)):
            numpy.put(tablero, casillaSeleccionadaY * 6 - (6 - casillaSeleccionadaX) - 1, 1)
            numpy.put(tablero, casillaSeleccionadaY2 * 6 - (6 - casillaSeleccionadaX2) - 1, 1)
            print("\n ¡Encontraste un par!")
        else:
            numpy.put(tablero, casillaSeleccionadaY * 6 - (6 - casillaSeleccionadaX) - 1, 0)
            numpy.put(tablero, casillaSeleccionadaY2 * 6 - (6 - casillaSeleccionadaX2) - 1, 0)
            print("\nEstos números no son pares, intenta de nuevo.")

        # Verificar si se han encontrado todos los pares
        if (tablero==tableroVerifiacion).all():
            print("\n\n\n¡Has Ganado!")
            return 1
    
# TERMINAN FUNCIONES ------------------------------------------

while True:     

    # Verificar si el usuario quiere jugar otra vez, en caso de ya haber jugado       
    if otraVez == "n":
        print("\n\nMuchas gracias por jugar, ¡hasta la próxima!")
        break

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
        ganar = juego()

    if ganar == 1:
        while True:
            otraVez = input(("\n¿Quieres jugar otra vez? (y/n): "))
            if otraVez == "y" or otraVez == "n":
                break