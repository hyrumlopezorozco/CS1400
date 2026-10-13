
"""
Hyrum  Orozco
Fecha: October 12, 2026
Título: Mi primera tortuga en Python
"""

# Importamos la biblioteca turtle (ya viene incluida en Python)
import turtle

# Configuración de la pantalla y la tortuga
pantalla = turtle.Screen()  # Usamos sintaxis de punto para acceder a Screen()
pantalla.bgcolor("lightcyan")  # TODO 2: Cambia el color de fondo usando bgcolor()
pantalla.title("Mi primera tortuga en Python")  # TODO 3: Asigna un título usando title()

# Corre el programa hasta este punto utilizando """ """ o # para asegurar que funcione bien.

# Solo una t para hacer menos código después.
t = turtle.Turtle()
t.shape("turtle")  # Forma de la tortuga.
t.speed(3)  # Velocidad del dibujo (1 es lento, 10 es rápido).

<<<<<<< HEAD
# TODO 4: Ejecuta el programa hasta este punto y toma una captura de pantalla.
# Luego guarda la captura dentro de la carpeta M06.
=======
# TODO 4 para correr el programa hasta este punto y toma una captura de pantalla. Luego lo guardaras entre la carpeta M6
>>>>>>> upstream/main

# =============================================================
# EJEMPLO: Dibujar la base de la casa (un cuadrado azul)
# =============================================================

t.color("darkblue", "lightblue")  # TODO 5: Son argumentos de la función color().
t.begin_fill()

# TODO 6: El for loop repite los movimientos cuatro veces para dibujar un cuadrado.
for _ in range(4):
    t.forward(100)  # Mueve la tortuga 100 unidades hacia adelante.
    t.left(90)  # Gira la tortuga 90 grados a la izquierda.

# TODO 7: El relleno empieza en la línea t.begin_fill().
t.end_fill()

# Mantiene la ventana abierta hasta que hagas clic en ella.
pantalla.exitonclick()
