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
    print("No está listo, pero funciona hasta ahora! ;)")

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