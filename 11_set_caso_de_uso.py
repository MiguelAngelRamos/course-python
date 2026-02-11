# Crearemos una lista de correo de gente de tecnologia
correos_tecnologia = [
    "richard.stallman@gnu.com",
    "ada.lovelace@analyticalengine.com", 
    "linus.torvalds@linux.com",
    "james.gosling@java.com",
    "linus.torvalds@linux.com",
    "richard.stallman@gnu.com",
    "ada.lovelace@analyticalengine.com"  # Este correo está repetido
]

def obtener_correos_unicos(correos):
    # Convertimos la lista a un set para eliminar duplicados
    correos_unicos = set(correos)
    return list(correos_unicos)

print("Correos únicos de tecnología:", obtener_correos_unicos(correos_tecnologia))