# clases.py
# Contiene la clase Tablero, que representa el tablero de cada jugador

import numpy as np
from variables import FILAS, COLUMNAS, BARCOS, AGUA, AGUA_TOCADA, BARCO, BARCO_TOCADO


class Tablero:

    def __init__(self, id_jugador):
        # Guardamos el nombre del jugador ("Jugador" o "Máquina")
        self.id_jugador = id_jugador
        self.barcos = BARCOS

        # Tablero propio: contiene tus barcos y los impactos que recibes
        self.tablero_propio = np.full((FILAS, COLUMNAS), AGUA, dtype=object)

        # Tablero de disparos: lo que has descubierto del tablero rival
        self.tablero_disparos = np.full((FILAS, COLUMNAS), AGUA, dtype=object)

        # Set con las coordenadas donde hay barco vivo
        # Cuando esté vacío, todos los barcos están hundidos
        self.coordenadas_barcos_vivos = set()

        # Colocamos los barcos al inicializar
        self.inicializar_tablero()

    def inicializar_tablero(self):
        # Coloca cada barco en una fila distinta, empezando en columna 0
        # Es la opción más sencilla: sin solapamientos ni salidas del tablero
        fila_actual = 0
        for nombre_barco, eslora in self.barcos.items():
            for columna in range(eslora):
                self.tablero_propio[fila_actual][columna] = BARCO
                self.coordenadas_barcos_vivos.add((fila_actual, columna))
            fila_actual += 1

    def recibir_disparo(self, fila, columna):
        # Comprueba qué hay en esa casilla y actúa en consecuencia
        # Devuelve True (impacto), False (agua) o None (disparo repetido)
        valor = self.tablero_propio[fila][columna]

        if valor == BARCO:
            self.tablero_propio[fila][columna] = BARCO_TOCADO
            self.coordenadas_barcos_vivos.discard((fila, columna))
            return True
        elif valor == AGUA:
            self.tablero_propio[fila][columna] = AGUA_TOCADA
            return False
        else:
            return None  # ya se había disparado antes aquí

    def todos_barcos_hundidos(self):
        # Si el set está vacío, no queda ningún barco vivo
        return len(self.coordenadas_barcos_vivos) == 0

    def actualizar_tablero_disparos(self, fila, columna, hubo_impacto):
        # Actualiza la vista del tablero rival tras un disparo tuyo
        if hubo_impacto:
            self.tablero_disparos[fila][columna] = BARCO_TOCADO
        else:
            self.tablero_disparos[fila][columna] = AGUA_TOCADA

    def imprimir_tablero_propio(self):
        print(f"\n--- Tablero de {self.id_jugador} ---")
        self._imprimir(self.tablero_propio)

    def imprimir_tablero_disparos(self):
        print(f"\n--- Disparos de {self.id_jugador} ---")
        self._imprimir(self.tablero_disparos)

    def _imprimir(self, array):
        # Imprime el array con cabecera de columnas y número de fila
        print("   " + " ".join(str(c).rjust(2) for c in range(COLUMNAS)))
        for fila in range(FILAS):
            fila_str = "  ".join(array[fila][col] for col in range(COLUMNAS))
            print(f"{str(fila).rjust(2)} {fila_str}")
        