# funciones.py
# Funciones auxiliares que usa main.py

import random
from variables import FILAS, COLUMNAS, AGUA, BARCO


def pedir_coordenada():
    # Pide fila y columna al usuario y valida que sean correctas
    while True:
        entrada = input("Introduce coordenadas (fila,columna): ").strip()
        partes = entrada.split(",")

        if len(partes) != 2:
            print("Formato incorrecto. Ejemplo: 3,5")
            continue

        try:
            fila = int(partes[0].strip())
            columna = int(partes[1].strip())
        except ValueError:
            print("Las coordenadas deben ser números. Ejemplo: 3,5")
            continue

        if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
            return fila, columna
        else:
            print(f"Las coordenadas deben estar entre 0 y {FILAS - 1}.")


def disparo_maquina(tablero_jugador):
    # Elige una casilla aleatoria que no haya sido disparada antes
    while True:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        valor = tablero_jugador[fila][columna]
        if valor == AGUA or valor == BARCO:
            return fila, columna


def bienvenida():
    print("=" * 40)
    print("   HUNDIR LA FLOTA")
    print("=" * 40)
    print("""
Introduce coordenadas en formato fila,columna (ej: 3,5).
Si aciertas, repites turno. Si fallas, dispara la máquina.
Gana el primero que hunda todos los barcos del rival.

Símbolos:
  ~  agua sin tocar
  O  agua ya disparada
  B  tu barco
  X  impacto
""")


def mensaje_disparo(jugador, resultado):
    if resultado is None:
        print(f"⚠️  Ya habías disparado ahí. Elige otra casilla.")
    elif resultado:
        print(f"💥 ¡{jugador} ha tocado un barco! Repite turno.")
    else:
        print(f"💧 {jugador} ha disparado al agua. Turno del rival.")