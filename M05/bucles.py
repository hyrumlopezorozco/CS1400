
"""
NOMBRE: Hyrum  Orozco
M5 TAREA 2
Laboratorio sobre Iteración
"""

# ==========================================
# Sección 1: ¿Por qué usar un Bucle?
# ==========================================

# Código 1: Impresión manual repetitiva
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")

# 1. Para saludar a 100 estudiantes habría que escribir muchas líneas
# repetidas, lo que toma tiempo y dificulta modificar el programa.

# 2. No es fácil adaptar la cantidad dinámicamente porque el número
# de saludos está escrito manualmente en el código.


# ==========================================
# Sección 2: Bucle while
# ==========================================

# Código 2: Repetición con if
respuesta = input("¿Deseas repetir el proceso? (si/no): ")

if respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")

# 3. El programa no preguntó una tercera vez y finalizó porque
# if ejecuta el bloque una sola vez si la condición es verdadera.

# 4. Con while, el programa sigue preguntando mientras la respuesta
# sea "si". Con if, el bloque se ejecuta como máximo una vez.

# 5. No, porque depende de las respuestas que dé el usuario.

# 6. Si no se actualiza la variable de control, la condición puede
# permanecer verdadera y producir un bucle infinito.

# 7. En la terminal se utiliza Ctrl+C para detener un programa
# que está ejecutando un bucle infinito.


# Modificación 1A: Cambio a while
# Descomenta este bloque para probar el bucle while.
# respuesta = input("¿Deseas repetir el proceso? (si/no): ")
# while respuesta == "si":
#     print("Ejecutando el bloque...")
#     respuesta = input("¿Deseas repetir el proceso? (si/no): ")
# print("Programa finalizado.")

# Modificación 1B: Bucle infinito
# Si se comenta la línea que actualiza respuesta dentro del while,
# la variable puede quedarse con "si" y el bucle no termina.
# Para probarlo, comenta la actualización dentro del bloque anterior.
# Usa Ctrl+C para detenerlo.


# ==========================================
# Sección 3: Bucle for y range()
# ==========================================

# Código 3
num = int(input("Introduce un número límite: "))

for i in range(10):
    print("Iteración:", i)

# 8. Se imprimió "Iteración" 10 veces. El número ingresado no influyó
# porque range(10) utiliza un límite fijo.

# 9. Valor inicial: 0
# Valor final: 9

# 10. No se imprimió el 10 porque range(10) empieza en 0 y excluye
# el límite superior.

# 11. No hay diferencia entre range(10) y range(0, 10):
# ambos generan los números del 0 al 9.

# Modificación 2A:
# 12. Con range(1, num) y una entrada de 20, el conteo termina en 19.

# 13. Respuesta: range(1, num + 1)

# Modificación 2B:
# 14. range(2, 11, 2) imprime 2, 4, 6, 8 y 10.
# El tercer argumento indica el paso o cuánto aumenta cada iteración.

# Para probar la modificación 2A:
# for i in range(1, num):
#     print("Iteración:", i)

# Para probar la modificación 2B:
# for i in range(2, 11, 2):
#     print("Iteración:", i)


# ==========================================
# Sección 4: Iteración sobre Secuencias
# ==========================================

# Código 4
palabra = "Python"

print("--- Letras de la palabra ---")
for letra in palabra:
    print(letra)

frutas = ["manzana", "banana", "cereza"]

print("--- Lista de frutas ---")
for fruta in frutas:
    print(fruta)

# 15. La variable letra representa el carácter actual de la palabra
# en cada repetición del bucle.

# 16. La iteración directa, for fruta in frutas, es más legible
# para principiantes porque accede directamente a cada fruta y
# no necesita manejar índices.


# ==========================================
# Sección 5: break y continue
# ==========================================

# Código 5
print("Demostración de continue:")
for num in range(1, 6):
    if num == 3:
        continue
    print("Número:", num)

print("\nDemostración de break:")
for num in range(1, 6):
    if num == 3:
        break
    print("Número:", num)

# 17. Falta el número 3 porque continue salta esa iteración
# y continúa con la siguiente.

# 18. Se imprimieron los números 1 y 2. break termina el bucle
# inmediatamente cuando num es igual a 3.

# 19. La sentencia break permite salir del bucle cuando la clave
# ingresada es correcta.


# ==========================================
# Sección 6: Acumulación y Conteo
# ==========================================

# Código 6
numeros = [4, 7, 2, 9, 10, 5]
suma_total = 0
mayores_a_cinco = 0

for num in numeros:
    suma_total += num
    if num > 5:
        mayores_a_cinco += 1

print("Suma total:", suma_total)
print("Cantidad de números mayores a 5:", mayores_a_cinco)

# 20. Ambas variables deben inicializarse en 0 antes del bucle.
# Si se inicializan dentro del bucle, sus valores se reiniciarían
# en cada repetición y no se conservaría el total acumulado.

# 21. Un acumulador suma valores, mientras que un contador aumenta
# normalmente en 1 cada vez que se cumple una condición.
# suma_total acumula números y mayores_a_cinco cuenta coincidencias.


# ==========================================
# Sección 7: Normalización con .lower()
# ==========================================

# Código 7
sujeto1 = "Python"
sujeto2 = "python"

if sujeto1 == sujeto2:
    print("Iguales")
else:
    print("Diferentes")

# 22. El primer texto comienza con P mayúscula y el segundo
# con p minúscula. El resultado inicial es "Diferentes".

# 23. Al cambiar la condición por:
# if sujeto1.lower() == sujeto2.lower():
# el resultado es "Iguales". lower() convierte las letras
# mayúsculas de la cadena a minúsculas.

# 24. .lower() permite comparar respuestas sin importar si el
# usuario escribe "SI", "Si" o "si", evitando diferencias
# causadas únicamente por el uso de mayúsculas.
