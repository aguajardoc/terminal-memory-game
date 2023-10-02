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
        print("\n\n¡Bienvenido al Memorama!\nEl número de jugadores se limita a 1.\nSe presentará un tablero de cartas en un arreglo 6x6 en el que se esconden pares de elementos.\nTu objetivo: encontrar todos los pares.\nCada turno, podrás seleccionar dos cartas.\nEsto lo harás tecleando la coordenada-X y la coordenada-Y correspondiente a la casilla que quieras seleccionar.\nToma en cuenta que los valores aceptados van del 1 al 6 para X y para Y.\nSi estas forman un par, se removerán del tablero y ¡estarás más cerca de ganar!\nPero si no forman un par, se regresarán a su posición inicial para que lo vuelvas a intentar.\n")
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
    
    # Empezar el cronómetro
    cronoEmpieza = time.time()

    while True:
        print('\n' * 50)
        print(numpy.matrix(tablero),"\n")
        # Esperar un input de casilla 1 del jugador
        while True:
            X = int(input("Escriba las coordenadas de una casilla\nCoordenada-X:  "))
            Y = int(input("Coordenada-Y: "))
            fetch = Y * 6 - (6 - X) - 1
            if X >= 1 and X <= 6 and Y >= 1 and Y <= 6 and tablero.item(fetch) == 0:
                break
            else:
                print("\n¡Esta coordenada es inválida!\nRecuerda que los espacios marcados con \"1\" están fuera de juego y que el rango de las coordenadas es de 1 a 6.\n")
        
        # Mostrar valor de casilla 1
        numpy.put(tablero, fetch, tableroEscondido.item(fetch))
        print("\n",tablero)

        # Esperar un input de casilla 2 del jugador
        while True:
            X2 = int(input("\nEscriba las coordenadas de otra casilla\nCoordenada-X:  "))
            Y2 = int(input("Coordenada-Y: "))
            fetch2 = Y2 * 6 - (6 - X2) - 1
            if X2 >= 1 and X2 <= 6 and Y2 >= 1 and Y2 <= 6 and (Y2 != Y) or (X != X2) and tablero.item(fetch2) == 0:
                break
            else:
                print("\n¡Esta coordenada es inválida!\nRecuerda que los espacios marcados con \"1\" están fuera de juego y que el rango de las coordenadas es de 1 a 6.\n")
        
        # Mostrar valor de casilla 2
        numpy.put(tablero, fetch2, tableroEscondido.item(fetch2))
        print("\n",tablero)

        # Verificar paridad
        if tableroEscondido.item(fetch) == tableroEscondido.item(fetch2):
            numpy.put(tablero, fetch, 1)
            numpy.put(tablero, fetch2, 1)
            print("\n¡Encontraste un par!")
            time.sleep(1)
        else:
            numpy.put(tablero, fetch, 0)
            numpy.put(tablero, fetch2, 0)
            print("\nEstos números no son pares, intenta de nuevo.")
            time.sleep(1)

        # Verificar si se han encontrado todos los pares
        if (tablero==tableroVerifiacion).all():
            print("\n\n\n¡Has Ganado!")
            cronoTermina = time.time()
            tiempo = cronoTermina - cronoEmpieza
            print(f"¡Completaste el memorama en {tiempo} segundos!\n¿Crees poder mejorarlo?\n")
            return 1
    
# TERMINAN FUNCIONES ------------------------------------------

while True:
    otraVez = "y"
    # Verificar si el usuario quiere jugar otra vez, en caso de ya haber jugado       
    if otraVez == "n":
        print("\n\nMuchas gracias por jugar, ¡hasta la próxima!")
        exit()

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
            time.sleep(1)
            otraVez = input(("\n¿Quieres jugar otra vez? (y/n): "))
            if otraVez == "y" or otraVez == "n":
                break