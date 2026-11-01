
"""
Tarea 1: Preparando la Oferta (Listas y Tuplas)
"""

# Tarea 1: Lista de elementos para el altar de muertos

# Lista de ofrendas editables (pueden agregarse o quitarse elementos)
ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]

# Tupla con los niveles tradicionales del altar (constante, no debe cambiar)
NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")

# Mostrar la segunda ofrenda (índice 1)
print("Segunda ofrenda:", ofrendas[1])

# 1. Modificación 1 (Listas)
ofrendas.append("Incienso copal")
ofrendas.sort()

print("\nLista de ofrendas ordenada alfabéticamente:")
print(ofrendas)

# Respuesta 1:
# La lista se modifica al agregar "Incienso copal" y se ordena alfabéticamente.
# Las listas son mutables, por lo que se pueden modificar después de crearlas.
# La variable ofrendas ahora contiene los elementos en orden alfabético.

# 2. Modificación 2 (Tuplas)
try:
    NIVELES_ALTAR[0] = "Gloria"
except TypeError as e:
    print("\nError al modificar la tupla:", e)

# Respuesta 2:
# Se produce un TypeError porque las tuplas son inmutables.
# No se puede cambiar, agregar o eliminar directamente un elemento de una tupla.

# 3. Utilizar enumerate() para mostrar cada ofrenda con su posición
print("\nOfrendas con su número de posición:")

for posicion, ofrenda in enumerate(ofrendas, start=1):
    print(f"{posicion}. {ofrenda}")

# Respuesta 3:
# enumerate() permite recorrer la lista y obtener tanto la posición
# como el elemento correspondiente en cada iteración.

