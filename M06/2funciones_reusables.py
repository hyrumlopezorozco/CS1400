
"""
NOMBRE: Hyrum  Orozco
M6 Tarea: Funciones Reusables
"""

# =============================================================
# Parte 1: Funciones sin retorno (Acciones directas)
# =============================================================

def mostrar_bienvenida(nombre):
    """Muestra un mensaje de bienvenida para la persona indicada."""
    print(f"¡Hola, {nombre}! Bienvenido a clase hoy.")

# PREGUNTAS:
# 1. La variable "nombre" dentro de los paréntesis se llama parámetro.
# 2. Para ser más reutilizable, se puede documentar la función con
# un docstring y permitir que reciba distintos nombres como argumento.


# =============================================================
# Parte 2: Funciones con retorno (Procesamiento de datos)
# =============================================================

def calcular_descuento(precio, porcentaje=10):
    """Calcula y devuelve el precio después de aplicar un descuento."""
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

def es_par(numero):
    """Devuelve True si el número es par y False si es impar."""
    return numero % 2 == 0

# PREGUNTAS:
# 3. La palabra clave para definir una función es def.
# 4. Las dos funciones son calcular_descuento y es_par.
# 5. calcular_descuento(100) usa el descuento predeterminado del 10%.
# El precio final es 90.0.
# 6. calcular_descuento(200, 20) aplica un descuento del 20%.
# El precio final es 160.0.


# =============================================================
# Parte 3: Pruebas de ejecución
# =============================================================

print("--- PRUEBA 1: Mostrar Bienvenida ---")
mostrar_bienvenida("Ana")
mostrar_bienvenida("Carlos")

print("\n--- PRUEBA 2: Cálculo de Descuentos ---")

compra_1 = calcular_descuento(100)
print(f"Precio con descuento por defecto: ${compra_1}")

compra_2 = calcular_descuento(200, 20)
print(f"Precio con 20% de descuento: ${compra_2}")

# PREGUNTAS:
# 7. Pseudocódigo:
# FUNCIÓN calcular_descuento(precio, porcentaje = 10)
#     descuento = precio * (porcentaje / 100)
#     precio_final = precio - descuento
#     DEVOLVER precio_final
#
# FUNCIÓN es_par(numero)
#     DEVOLVER si el residuo de numero / 2 es igual a 0
#
# 8. Explicación: calcular_descuento recibe un precio y un porcentaje.
# Calcula cuánto dinero se descuenta y devuelve el precio final.
# El propósito del programa es reutilizar funciones para calcular
# descuentos sin repetir las mismas operaciones.
#
# 9. Las funciones ya aceptan precios decimales porque Python
# permite utilizar números como 19.99. No se necesita cambiar
# la fórmula para calcular descuentos con decimales.


# =============================================================
# Parte 4: Alcance (Scope) y Retorno
# =============================================================

# La función mostrar_bienvenida() usa print(), mientras que
# calcular_descuento() usa return.

resultado = mostrar_bienvenida("Julio")
print(resultado)

# PREGUNTAS:
# 10. La variable resultado guarda None porque mostrar_bienvenida()
# imprime un mensaje, pero no tiene una instrucción return.

# 11. return es necesario porque devuelve el precio final a quien
# llama a calcular_descuento(), permitiendo guardarlo en compra_1
# y compra_2 y utilizarlo posteriormente.

# 12. Al ejecutar print(descuento) fuera de la función,
# Python muestra NameError porque descuento no está definido
# en ese ámbito.

# Para comprobarlo, descomenta la siguiente línea:
# print(descuento)

# 13. La variable descuento es local a calcular_descuento().
# Solo existe dentro de esa función y no es accesible directamente
# desde fuera.

# 14. Si se cambia return precio_final por print(precio_final),
# la función imprime el resultado pero devuelve None.
# Por eso compra_1 + 5 produciría TypeError, porque intenta sumar
# None y un número.

# 15. Se puede utilizar un keyword argument así:
# calcular_descuento(200, porcentaje=20)

# 16. Cada función tiene un docstring entre triple comillas
# inmediatamente después de su definición. Explica su propósito.
