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

# Valor Asoluto
def valor_absoluto(numero):
    if numero >=0:
        return numero
    else:
        return -numero

# Invocar la función valor_absoluto
print("\nLlamando a la función valor_absoluto:")
print(f"El valor absoluto de -10 es: {valor_absoluto(-10)}")
print(f"El valor absoluto de 10 es: {valor_absoluto(10)}")

# Parametros por defecto
def crear_perfil(nombre, edad=18, pais="Chile"):
    print(f"Nombre: {nombre}, Edad: {edad}, País: {pais}")

# Invocar la función crear_perfil con diferentes combinaciones de argumentos
print("\nLlamando a la función crear_perfil:")
crear_perfil("Bob")
crear_perfil("Sofia")
crear_perfil("Charlie", 25)
crear_perfil("Diana", 30, "Argentina")