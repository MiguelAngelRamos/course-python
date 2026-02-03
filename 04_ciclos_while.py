# Ciclos en Python

"""
Los ciclos o bucles son estructuras que nos permiten repetir un bloque de código varias veces mientras se cumpla una condición específica. En Python, los dos tipos principales de ciclos son el ciclo "for" y el ciclo "while".
"""

## Ciclo While o Mientras
# El ciclo while repite un bloque de código mientras una condición sea verdadera.

# while condición:
#     # Bloque de código a repetir
#     print("Este bloque se repite mientras la condición sea verdadera")

# Importante evitar ciclos infinitos asegurándonos de que la condición eventualmente se vuelva falsa.

# while True:
#     print("Hola")  # Esto crea un ciclo infinito

# Contador simple

# contador = 1 # Variable de alcance global
# while contador <= 5:  # Condición
#     print("Contador:", contador)  # Bloque de código
#     contador += 1  # Actualización de la variable de control
    
    # contador = contador + 1 # esto se puede resumir como contador += 1

## While con input para validacion de datos

# numero = -1
# while numero < 0:
#     numero = int(input("Ingrese un número positivo: ")) # "10" -> int -> 10 el -5
#     if numero < 0:
#         print("Error: el número debe ser positivo. Intente de nuevo.")
# print("Perfecto! Ingresaste:", numero)

# Juego de adivinanza con límite de intentos
numero_secreto = 7
intentos = 0
max_intentos = 3
adivinado = False

print("¡Adivina el número entre 1 y 10!")

while intentos < max_intentos and not adivinado:
    intento = int(input(f"Intento {intentos + 1}/{max_intentos}: "))
    intentos += 1
    
    if intento == numero_secreto:
        adivinado = True
        print(f" ¡Correcto! Lo adivinaste en {intentos} intentos")
    elif intento < numero_secreto:
        print("⬆El número es mayor")
    else:
        print("⬇El número es menor")

if not adivinado:
    print(f"Se acabaron los intentos. El número era {numero_secreto}")