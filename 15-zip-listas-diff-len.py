from itertools import zip_longest

nombres = ["Juan", "Maria", "Pedro", "Sofia", "Lucas"]
edades = [20, 22, 19, 21]
# Usamos zip para combinar las listas
estudiantes = list(zip(nombres, edades))
print(estudiantes) # [('Juan', 20), ('Maria', 22), ('Pedro', 19), ('Sofia', 21)]

resultado_todos_elementos = list(zip_longest(nombres, edades))
print(resultado_todos_elementos) # [('Juan', 20), ('Maria', 22), ('Pedro', 19), ('Sofia', 21), ('Lucas', None)]