"""
Módulo de funciones de ejemplo.

Contenidos:
- Definición de funciones
- Uso de parámetros y valores de retorno
- Valores devueltos (return)
- Alcance de variables (scope)
- Importación de módulos

"""

# Definición de una función simple
def saludar():
    print("Hola Mundo!")


print("Llamando a la función saludar:")
saludar()

# Función con parámetros
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

# Invocar la función con un argumento
print("\nLlamando a la función saludar_usuario:")
saludar_usuario("Alice")

# Función con valor de retorno
def sumar(a, b):
    return a + b
# Invocar la función y capturar el valor retornado
print("\nLlamando a la función sumar:")
resultado = sumar(5, 7)
print(f"La suma de 5 y 7 es: {resultado}")