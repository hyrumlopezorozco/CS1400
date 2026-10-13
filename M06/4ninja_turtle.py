
"""
====================================================================
Proyecto: Dibujar una pizza con Python Turtle
====================================================================
En este ejercicio aprenderás el PODER DE LAS FUNCIONES:
1. Reutilización: Escribe el código una vez y úsalo muchas veces.
2. Modularidad: Rompe un problema grande (una tarta) en problemas
   pequeños (porciones/triángulos).
3. Parámetros: Cambia el comportamiento de tu dibujo pasando
   diferentes argumentos (tamaño, número de rebanadas, color).
====================================================================
"""

import math
import turtle

# ==================================================================
# 1. Configuración Inicial del Entorno
# ==================================================================
pantalla = turtle.Screen()
pantalla.bgcolor("lightcyan")
pantalla.title("El Poder de las Funciones: Tarta de Triángulos")

t = turtle.Turtle()
t.shape("turtle")
t.speed(5)


# ==================================================================
# 2. Definición de Funciones
# ==================================================================

# TODO 1: Completa la definición de la función 'dibujar_triangulo'
def dibujar_triangulo(t, longitud, angulo, color_relleno="orange"):
    """
    Dibuja una porción de tarta (triángulo isósceles) usando la tortuga 't'.

    Parámetros:
    - t: El objeto Turtle que dibuja.
    - longitud: La longitud de los dos lados iguales (el radio de la tarta).
    - angulo: El ángulo en el vértice central (en grados).
    - color_relleno: El color con el que se pintará la porción.
    """

    # --------------------------------------------------------------
    # Paso A: Cálculos Matemáticos (Geometría del Triángulo)
    # --------------------------------------------------------------

    # 1. Convertimos la mitad del ángulo a radianes para usar trigonometría
    mitad_angulo = math.radians(angulo / 2)

    # TODO 2: Calcula la longitud de la base del triángulo isósceles.
    base = 2 * longitud * math.sin(mitad_angulo)

    # TODO 3: Calcula el ángulo de giro exterior para la tortuga.
    angulo_giro_base = 90 + (angulo / 2)

    # --------------------------------------------------------------
    # Paso B: Dibujo del Triángulo Isósceles
    # --------------------------------------------------------------
    t.color("darkred", color_relleno)
    t.begin_fill()

    # TODO 4: Trazado del triángulo
    t.forward(longitud)
    t.left(angulo_giro_base)
    t.forward(base)
    t.left(angulo_giro_base)
    t.forward(longitud)
    t.left(180)

    t.end_fill()


# TODO 5: Función para construir la tarta completa.
def dibujar_tarta(t, n_porciones, longitud, color_relleno="orange"):
    """
    Dibuja una tarta completa de 'n_porciones' llamando repetidamente
    a la función dibujar_triangulo.
    """

    # TODO 6: Calcula el ángulo central de cada porción.
    angulo = 360 / n_porciones

    # TODO 7: Dibuja todas las porciones usando un bucle for.
    for _ in range(n_porciones):
        dibujar_triangulo(t, longitud, angulo, color_relleno)


# TODO 8 (EXTRA/OPCIONAL): Función auxiliar para mover la tortuga sin dejar rastro.
def mover_tortuga(t, x, y):
    """Mueve la tortuga a las coordenadas (x, y) sin dibujar."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)


# ==================================================================
# 3. Demostración del Poder de las Funciones
# ==================================================================

# TODO 9: Instrucciones para dibujar tres tartas en diferentes posiciones.

# --- Tarta 1: Tarta clásica de 6 porciones ---
mover_tortuga(t, -250, 0)
dibujar_tarta(t, 6, 80, "orange")

# --- Tarta 2: Tarta grande de 12 porciones ---
mover_tortuga(t, 0, 0)
dibujar_tarta(t, 12, 100, "gold")

# --- Tarta 3: Tarta pequeña de 4 porciones ---
mover_tortuga(t, 180, 0)
dibujar_tarta(t, 4, 60, "tomato")

# TODO 10: Finalizar ejecución al hacer clic.
pantalla.exitonclick()
