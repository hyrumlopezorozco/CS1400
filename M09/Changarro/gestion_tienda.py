
# gestion_tienda.py

# Este módulo contiene las funciones para gestionar el inventario de la tienda.

def agregar_producto(inventario, nombre, precio):
    """
    Agrega un producto al inventario con su precio.
    Convierte el precio a número decimal.
    Si el precio no es válido, devuelve False.
    """
    try:
        # Convertimos a float para asegurar que sea un número
        precio_num = float(precio)
        inventario[nombre] = precio_num
        return True
    except ValueError:
        # Si no se puede convertir a número, devolvemos False
        return False


def buscar_precio(inventario, nombre):
    """
    Busca un producto en el inventario y devuelve su precio.
    Si el producto no existe, devuelve None.
    """
    # Usamos .get() para evitar que el programa falle si la llave no existe
    return inventario.get(nombre, None)


def listar_productos(inventario):
    """
    Muestra todos los productos y sus precios.
    Si el inventario está vacío, muestra un mensaje.
    """
    if not inventario:
        print("\n> El inventario está vacío.")
    else:
        print("\n--- Inventario Actual ---")
        for producto, precio in inventario.items():
            print(f"• {producto}: ${precio:.2f}")
