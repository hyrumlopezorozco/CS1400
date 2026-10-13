
"""
====================================================================
Mi Primera Función en Turtle
====================================================================
NOMBRE: Hyrum  Orozco
FECHA: October 12, 2026
Objetivo:
Entender cómo encapsular código en una función para reutilizarlo y
dibujar figuras personalizadas de manera sencilla.

Corre este programa y toma captura del resultado.
====================================================================
"""

import turtle

# ==================================================================
# 1. Configuración de la Pantalla y Tortuga
# ==================================================================
pantalla = turtle.Screen()
pantalla.bgcolor("lightyellow")
pantalla.title("Funciones y Figuras")

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)


# ==================================================================
# 2. DEFINICIÓN DE LA FUNCIÓN
# ==================================================================

# Función para dibujar diferentes polígonos regulares.
def dibujar_figura(lados, tamaño, color_borde, color_relleno):
    """
    Dibuja cualquier polígono regular basado en el número de lados.

    Parámetros:
    - lados: Número de lados de la figura.
    - tamaño: Longitud de cada lado.
    - color_borde: Color de las líneas.
    - color_relleno: Color del interior de la figura.
    """

    # La suma de los ángulos exteriores de cualquier polígono es 360 grados.
    angulo = 360 / lados

    # Configuración de colores
    t.color(color_borde, color_relleno)
    t.begin_fill()

    # Repite el avance y el giro según el número de lados.
    for _ in range(lados):
        t.forward(tamaño)
        t.left(angulo)

    t.end_fill()


# Función auxiliar para mover la tortuga sin dibujar.
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# ==================================================================
# 3. DEMOSTRACIÓN / PRUEBAS
# ==================================================================

# Dibujar un triángulo (3 lados)
mover(-200, 0)
dibujar_figura(lados=3, tamaño=80, color_borde="darkgreen", color_relleno="lightgreen")

# Dibujar un pentágono (5 lados)
mover(-50, 0)
dibujar_figura(lados=5, tamaño=60, color_borde="purple", color_relleno="plum")

# Dibujar un hexágono (6 lados)
mover(100, 0)
dibujar_figura(lados=6, tamaño=50, color_borde="darkblue", color_relleno="skyblue")

# Cuarta figura: dibujar un cuadrado sin usar dibujar_figura()
mover(-50, -130)
t.color("darkred", "salmon")
t.begin_fill()

for _ in range(4):
    t.forward(60)
    t.left(90)

t.end_fill()


# ==================================================================
# 4. PREGUNTAS
# ==================================================================

"""
1. Hay 2 funciones en este programa.
   dibujar_figura() dibuja polígonos con diferentes lados, tamaños y colores.
   mover() mueve la tortuga a una posición específica sin dibujar.

2. El parámetro que se debe cambiar es lados.
   Para hacer un octágono: lados=8.

3. La función mover() termina antes de la sección
   3. DEMOSTRACIÓN / PRUEBAS.

4. Se agregó un cuadrado usando un bucle for, sin utilizar
   la función dibujar_figura().

5. Guarda una captura de pantalla con las 4 figuras en la carpeta M06.
"""

pantalla.exitonclick()
