# Recopilación de información
nombre_usuario = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre_usuario}!")

# Preguntar por la edad
edad_usuario = int(input("¿Cuántos años tienes? "))
print(f"En 5 años mas tendras: {edad_usuario + 5}")

# Tipos en Python
print(type(nombre_usuario))  # Tipo de dato string
print(type(edad_usuario))    # Tipo de dato entero

# Imprimir
variable = 42
print(f"El valor de la variable es: {variable}")
print(f"type(variable) = {type(variable)}")

# Funcion isinstance()
print(f"isinstance(42, int) = {isinstance(42, int)}")
print(f"isinstance(3.14, float) = {isinstance(3.14, float)}")