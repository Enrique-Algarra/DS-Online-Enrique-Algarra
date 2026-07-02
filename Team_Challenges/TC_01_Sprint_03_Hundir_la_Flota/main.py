# main.py
# Programa principal del juego. Aquí corre todo.

from clases import Tablero
from funciones import pedir_coordenada, disparo_maquina, bienvenida, mensaje_disparo


def main():

    # 1. Bienvenida (se ejecuta solo una vez)
    bienvenida()

    # 2. Inicialización de los dos tableros (se ejecuta solo una vez)
    tablero_jugador = Tablero("Jugador")
    tablero_maquina = Tablero("Máquina")

    turno_jugador = True  # empieza el jugador

    # 3. Bucle principal del juego
    while True:

        if turno_jugador:
            # --- Turno del jugador ---
            tablero_jugador.imprimir_tablero_propio()
            tablero_jugador.imprimir_tablero_disparos()

            print("\n🎯 Tu turno.")
            fila, columna = pedir_coordenada()
            resultado = tablero_maquina.recibir_disparo(fila, columna)

            mensaje_disparo("Jugador", resultado)

            if resultado is None:
                continue  # disparo repetido, no cambia el turno

            tablero_jugador.actualizar_tablero_disparos(fila, columna, resultado)

            if tablero_maquina.todos_barcos_hundidos():
                print("\n🏆 ¡Has ganado! Hundiste toda la flota enemiga.")
                break

            turno_jugador = resultado  # si acertó True -> repite, si falló False -> turno máquina

        else:
            # --- Turno de la máquina ---
            print("\n🤖 Turno de la máquina...")
            fila, columna = disparo_maquina(tablero_jugador.tablero_propio)
            resultado = tablero_jugador.recibir_disparo(fila, columna)

            print(f"   La máquina dispara a ({fila}, {columna})")
            mensaje_disparo("Máquina", resultado)

            if tablero_jugador.todos_barcos_hundidos():
                print("\n💀 La máquina ha ganado. Hundió toda tu flota.")
                break

            turno_jugador = not resultado  # si acertó False -> repite máquina, si falló True -> turno jugador


if __name__ == "__main__":
    main()
    