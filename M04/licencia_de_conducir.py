
# M04 - Licencia de conducir
# Autor: Hyrum
# Este programa verifica si una persona puede conducir de forma segura.

print("======================================")
print("   PRUEBA DE CONDUCCION DE ABUELA")
print("======================================")

# Pedir la edad del usuario
edad = int(input("¿Cuantos años tienes? "))

# Preguntar sobre las condiciones para conducir
tiene_licencia = input("¿Tienes licencia valida? (si/no): ").lower()
necesita_lentes = input("¿Necesitas lentes para conducir? (si/no): ").lower()
usa_lentes = input("¿Estas usando tus lentes? (si/no): ").lower()
ha_bebido = input("¿Has tomado alcohol? (si/no): ").lower()
tiene_sueno = input("¿Tienes mucho sueño? (si/no): ").lower()

# Primera sentencia: verificar la edad
if edad < 16:
    print("¡Eres demasiado joven para conducir! Devuelve las llaves.")

# Segunda sentencia: verificar la licencia
elif tiene_licencia != "si":
    print("¡Abuela, entrega las llaves! No tienes licencia.")

# Tercera sentencia: verificar condiciones peligrosas
elif ha_bebido == "si" or tiene_sueno == "si":
    print("¡PELIGRO! No conduzcas. ¡Entrega las llaves inmediatamente!")

# Cuarta sentencia: verificar los lentes
elif necesita_lentes == "si" and not (usa_lentes == "si"):
    print("¡Abuela, busca tus lentes! No puedes conducir sin ellos.")

# Quinta sentencia: verificar las condiciones de seguridad
elif edad >= 16 and tiene_licencia == "si" and ha_bebido == "no" and tiene_sueno == "no":
    print("¡Puedes conducir! Maneja con cuidado.")

# Si ninguna condicion anterior se cumple
else:
    print("Revisa tus respuestas antes de conducir.")

print("======================================")
print("Fin de la prueba de conduccion.")


# ==========================================
# ANALYSIS - PREGUNTAS Y RESPUESTAS
# ==========================================

# 1. ¿Cuantos commits hiciste?
# Respuesta: Hice varios commits para guardar los cambios
# de mi programa. Debo escribir el numero real de commits.

# 2. ¿Que metodo te parecio mas facil para guardar y subir
# tus cambios a GitHub? ¿Por que?
# Respuesta: Me parecio mas facil usar la interfaz visual
# de Visual Studio Code porque puedo ver los archivos
# modificados y guardar mis cambios facilmente.

# 3. ¿Para que sirve ejecutar git status?
# Respuesta: Sirve para revisar que archivos fueron
# modificados y cuales estan pendientes de guardar
# o agregar a un commit.

# 4. ¿Por que es importante usar git pull antes de trabajar?
# Respuesta: Porque descarga los cambios mas recientes
# del repositorio de la profesora y ayuda a evitar
# conflictos al subir mis modificaciones.

# 5. ¿Cual es la diferencia entre fork y clone?
# Respuesta: Fork crea una copia del repositorio en mi
# cuenta de GitHub. Clone descarga una copia del repositorio
# a mi computadora para trabajar en los archivos.

# 6. ¿Por que debemos escribir mensajes claros en cada commit?
# Respuesta: Porque explican los cambios que hice y me
# ayudan a entender el historial del proyecto.

# 7. ¿Que tipos de mensajes agregaste?
# Respuesta: Agregue mensajes para pedir datos al usuario
# y mensajes de advertencia, seguridad y permiso para conducir.

# 8. ¿Cual es tu sentencia preferida?
# Respuesta: Mi sentencia preferida es if porque permite
# comprobar una condicion y ejecutar una accion dependiendo
# del resultado.

# 9. ¿Cuando entra el programa a la segunda sentencia?
# Respuesta: Entra al primer elif cuando la condicion
# anterior no se cumple y la persona no tiene una licencia
# de conducir valida.

# 10. ¿Que aprendiste del README.md en tu carpeta M04?
# Respuesta: Aprendi que el README.md contiene informacion
# e instrucciones importantes sobre la tarea. Los comentarios
# tambien ayudan a explicar el funcionamiento del codigo.
# Debo revisar el README.md real para incluir sus instrucciones.
