# Operaciones de Conjunto con sets vacíos

devs_backend = {"Juan", "Richard", "Sofia", "Pedro"}
devs_frontend = {"Richard", "Margarita", "Sofia", "Lucas"}

# Unión de conjuntos, todos los estudiantes sin repetir

todos_los_devs = devs_backend | devs_frontend
print("Todos los desarrolladores:", todos_los_devs)

# Intersección de conjuntos, estudiantes que están en ambos grupos
devs_comunes = devs_backend & devs_frontend
print("Desarrolladores en ambos grupos:", devs_comunes)

# Diferencia de conjuntos, estudiantes que solo están en backend
devs_solo_backend = devs_backend - devs_frontend
print("Desarrolladores solo en backend:", devs_solo_backend)