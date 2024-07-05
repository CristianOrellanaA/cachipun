import random as rd
def maquina():
    jugada = rd.randrange(0,3)
    if jugada == 0:
        return "piedra"
    elif jugada == 1:
        return "papel"
    else:
        return "tijera"

def match(jugada):
    python = maquina()

    print("python jugo " + python)

    if jugada == python:
        return 0
    if jugada == "piedra" and python == "tijera":
        return 1
    if jugada == "piedra" and python == "papel":
        return -1
    if jugada == "papel" and python == "piedra":
        return 1
    if jugada == "papel" and python == "tijera":
        return -1
    if jugada == "tijera" and python == "papel":
        return 1
    if jugada == "tijera" and python == "piedra":
        return -1

resultados = list()
rondas = 3

for i in range (0,rondas):
    jugador =input("Ingresa tu jugada: ")
    resultado = match(jugador)
    resultados.append(resultado)

if sum(resultados) == 0:
    print("EMPATE")
if sum(resultados) > 0:
    print("GANASTE")
if sum(resultados) < 0:
    print("PERDISTE")

