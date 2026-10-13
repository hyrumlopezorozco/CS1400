
"""
NOMBRE: Hyrum  Orozco
M5 TAREA 1
Guía de Trabajo 2: Métodos, Slicing y Matemáticas en Python
"""

# ==========================================
# Sección 1: Conteo Inverso con range()
# ==========================================

# Código 1.1: Conteo descendente
num = int(input("Introduce el número inicial: "))

for i in range(num, 0, -1):
    print("Conteo:", i)

# Análisis:
# 1. Inicio: 10 | Fin: 1

# 2. El paso debe ser negativo porque queremos contar hacia atrás,
# disminuyendo el número en cada repetición.

# 3. El valor final es 0 porque range() no incluye el límite final.
# Por eso, el conteo termina en 1.

# 4. Respuesta: range(num, -1, -2)
# Si el número inicial es par, el conteo llega a 0.
# Si es impar, contar de 2 en 2 no permite llegar exactamente a 0.


# ==========================================
# Sección 2: Funciones Matemáticas de Python
# ==========================================

import math

decNum = -34.5678
intNum = 9

print(round(decNum, 2))     # Línea A
print(round(decNum, 0))     # Línea B
print(int(decNum))          # Línea C
print(abs(decNum))          # Línea D

print(math.pow(intNum, 2))  # Línea E
print(math.sqrt(intNum))    # Línea F

# Predicciones de salida:
# 5. Línea A: -34.57
# 6. Línea B: -35.0
# 7. Línea C: -34
# 8. Línea D: 34.5678
# 9. Línea E: 81.0
# 10. Línea F: 3.0


# ==========================================
# Sección 3: Comparación de Textos ASCII / Unicode
# ==========================================

miMax = max("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)

# 11. Predicción: manzana

# 12. Resultado: manzana

# 13. "manzana" es la mayor porque la letra minúscula "m"
# tiene un valor Unicode mayor que las letras mayúsculas "B" y "Z".
# Python compara las cadenas carácter por carácter.

# 14. Resultado al usar min(): Banano
# "B" tiene un valor Unicode menor que "Z" y "m".

miMin = min("Banano", "manzana", "Zanahoria")
print("El mínimo es:", miMin)


# ==========================================
# Sección 4: Aplicación Práctica – Física y Matemáticas
# ==========================================

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

# 15. Calcula la velocidad estimada utilizando la fórmula.
v = math.sqrt(20 * d)

print("Velocidad estimada del auto:", round(v, 2), "km/h")


# ==========================================
# Sección 5: Segmentación de Cadenas (Slicing)
# ==========================================

nombre = "Building Puentes"

print("Índice 0:", nombre[0])
print("Segmento:", nombre[8:15])

# 16. El carácter que imprime nombre[0] es: B

# 17. El espacio en blanco está en el índice: 8

# 18. Opción con 2 valores: nombre[9:16]
# Opción con límite implícito: nombre[9:]
print("Palabra completa:", nombre[9:16])
print("Palabra con límite implícito:", nombre[9:])


# ==========================================
# Sección 6: Filtrado e Inspección de Caracteres
# ==========================================

texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0

for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)

# 19. Para el texto "3 tigres en 2 árboles", el resultado es: 2

# 20. Python comprueba si cada carácter es mayor o igual que "0"
# y menor o igual que "9". Si cumple ambas condiciones,
# cuenta el carácter como un dígito numérico.


# ==========================================
# Sección 7: Investigación de Métodos de Cadenas
# ==========================================

# 21. Método .rfind('a'):
# Busca la última aparición de la letra "a" en una cadena
# y devuelve su índice. Si no la encuentra, devuelve -1.

# 22. Método .isalpha():
# Devuelve True si todos los caracteres de la cadena son letras
# y la cadena no está vacía. De lo contrario, devuelve False.

# 23. Método .isdigit():
# Devuelve True si todos los caracteres de la cadena son dígitos
# y la cadena no está vacía. De lo contrario, devuelve False.
