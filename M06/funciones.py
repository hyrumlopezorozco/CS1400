\
# --------------------------------------------------------------------------
#          FUNCIÓN PARA SIMULAR EL LANZAMIENTO DE UN DADO
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una función que no tome parámetros y que, cada vez
# que se llame, simule el lanzamiento de un dado de seis caras, devolviendo
# un número aleatorio entre 1 y 6.
#
# Instrucciones para el estudiante:
# 1. Importa el módulo random de Python.
# 2. Define una función llamada lanzar_dado que no acepte parámetros.
# 3. Utiliza random.randint(1, 6) para generar un número aleatorio.
# 4. Devuelve el número generado usando return.
# --------------------------------------------------------------------------

# TODO: Paso 1. Importa el módulo random.
import random


def lanzar_dado():
    """
    Simula el lanzamiento de un dado de seis caras.

    No recibe parámetros.

    Returns:
        int: Un número entero aleatorio entre 1 y 6.
    """

    # TODO: Paso 2. Genera un número aleatorio entre 1 y 6.
    # Guárdalo en una variable llamada resultado.
    resultado = random.randint(1, 6)

    # TODO: Paso 3. Devuelve el resultado.
    return resultado


# --- Bloque para probar tu función ---
if __name__ == "__main__":
    print("Lanzando el dado 5 veces:")

    # Usamos un bucle para llamar a la función varias veces.
    for i in range(5):
        resultado_lanzamiento = lanzar_dado()
        print(f"Lanzamiento {i + 1}: {resultado_lanzamiento}")
