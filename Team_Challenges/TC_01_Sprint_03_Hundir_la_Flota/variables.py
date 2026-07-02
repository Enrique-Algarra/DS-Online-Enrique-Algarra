# variables.py
# Constantes del juego: dimensiones, barcos y símbolos del tablero

FILAS = 10
COLUMNAS = 10

# Diccionario de barcos: nombre -> eslora (casillas que ocupa)
# 1 barco de 4, 2 de 3, 3 de 2, 4 de 1
BARCOS = {
    "portaaviones": 4,
    "acorazado_1": 3,
    "acorazado_2": 3,
    "destructor_1": 2,
    "destructor_2": 2,
    "destructor_3": 2,
    "submarino_1": 1,
    "submarino_2": 1,
    "submarino_3": 1,
    "submarino_4": 1,
}

# Símbolos para representar cada casilla al imprimir el tablero
AGUA = "~"           # casilla de agua sin disparar
AGUA_TOCADA = "O"    # disparo que dio agua
BARCO = "B"          # barco sin tocar (solo visible en tu tablero)
BARCO_TOCADO = "X"   # barco impactado