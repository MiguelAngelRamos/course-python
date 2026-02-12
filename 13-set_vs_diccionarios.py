# Set (Conjunto)
# Un set es una colección desordenada de elementos únicos.

tecnologias_backend = {"Python", "Django", "Flask", "SQL"}
numeros_set = {1, 2, 3, 4, 5}
set_vacio = set()  # Forma correcta de crear un set vacío

# Diccionario
# Un diccionario es una colección de pares clave-valor.

capitales = {"Colombia": "Bogotá", "Perú": "Lima", "Argentina": "Buenos Aires"}
dict_vacio = {}  # Forma correcta de crear un diccionario vacío

# Diferencias clave entre sets y diccionarios:
# En el Set son solo valores únicos sin claves asociadas.

colores = {"rojo", "verde", "azul"}

# Diccionario con colores
colores_hex = {
    "rojo": "#FF0000",
    "verde": "#00FF00",
    "azul": "#0000FF"
}

# Acceso a elementos:

mi_set = {10, 20, 30}
print(mi_set[0])