
# M04 - Licencia de conducir
# Este programa verifica si una persona puede conducir de forma segura.

print("===================================")
print("   PRUEBA DE CONDUCCIÓN DE ABUELA")
print("===================================")

# Preguntar la edad del usuario
edad = int(input("¿Cuántos años tienes? "))

# Preguntar sobre las condiciones para conducir
tiene_licencia = input("¿Tienes una licencia de conducir válida? (si/no): ").lower()
necesita_lentes = input("¿Necesitas lentes para conducir? (si/no): ").lower()
usa_lentes = input("¿Estás usando tus lentes ahora mismo? (si/no): ").lower()
ha_bebido = input("¿Has tomado alcohol? (si/no): ").lower()
tiene_sueno = input("¿Tienes mucho sueño? (si/no): ").lower()

# Verificar si la persona tiene la edad suficiente
if edad < 16:
    print("¡ALTO! Eres demasiado joven para conducir. ¡Devuelve las llaves!")

# Verificar si tiene una licencia válida
elif tiene_licencia != "si":
    print("¡Sin licencia no hay conducción! ¡Abuela, entrega las llaves!")

# Verificar condiciones peligrosas
elif ha_bebido == "si" or tiene_sueno == "si":
    print("¡PELIGRO! No puedes conducir así. ¡Entrega las llaves inmediatamente!")

# Verificar si necesita lentes, pero no los está usando
elif necesita_lentes == "si" and not (usa_lentes == "si"):
    print("¡Abuela, ¿dónde están tus lentes?! ¡No conduzcas sin ellos!")

# Verificar si todas las condiciones son seguras
elif edad >= 16 and tiene_licencia == "si" and ha_bebido == "no" and tiene_sueno == "no":
    print("¡Puedes conducir! Maneja con cuidado y respeta las reglas.")

# Respuesta para casos no contemplados
else:
    print("¡Revisa tus respuestas! Las llaves se quedan aquí por ahora.")

print("===================================")
print("¡Gracias por realizar la prueba de conducción!")
