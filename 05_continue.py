# QUE ES EL CONTINUE EN PYTHON

"""
lA Instruccion Continue es una palabra clave en python que se utiliza dentro bucles (for o while) para saltar el resto del codigo en la iteracion actual y pasar inmediatamente a la siguiente iteracion del bucle.
"""

# Ejemplo en codigo

# for elemento in secuencia:
#     if condicion_para_saltar:
#         continue  # Salta a la siguiente iteracion del bucle
#     # Bloque de codigo que se ejecuta si no se cumple la condicion_para_saltar
#     print(elemento)


# # lista de numeros del 1 al 20
# numeros = list(range(1, 11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for numero in numeros:
#     if numero % 2 == 0:  # Si el numero es par
#         continue  # Saltar el resto del codigo y pasar a la siguiente iteracion
#     print(f"Procesando número: {numero}")

lenguajes_programacion = ["   Python","  ","    JavaScript", "Java", "  Ruby", "Swift", "       "]




for lenguaje in lenguajes_programacion:
    nombre_limpio = lenguaje.strip()  # Eliminar espacios en blanco al inicio y al final

    if nombre_limpio == "":
        continue  # Saltar si el nombre esta vacio despues de limpiar espacios
    print(f"Lenguaje de programación: {nombre_limpio}")