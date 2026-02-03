print(" === Sistema de Registro === ")

numeros_usuarios = int(input("¿Cuántos usuarios desea registrar? ")) # 5
usuarios = []

# range(5) # [0, 1, 2, 3, 4]

for indice in range(numeros_usuarios):
    print(f"\n--- Registro del usuario {indice + 1} ---")
    # Usar un while para validar nombre no vacío
    nombre = ""
    while nombre.strip() == "":
        nombre = input("Ingrese el nombre del usuario: ")
        if nombre.strip() == "":
            print("Error: El nombre no puede estar vacío. Intente de nuevo.")

    # Usar un while para validar edad (mayor a 0)
    edad = 0
    while edad <= 0:
        try:
            edad = int(input("Ingrese la edad del usuario: "))
            if edad <= 0:
                print("Error: La edad debe ser un número positivo. Intente de nuevo.")
        except ValueError:
            print("Error: Por favor ingrese un número válido para la edad.")

    usuarios.append({"nombre": nombre, "edad": edad})
    # Esto quedaria asi para el primer usuario usuarios = [{"nombre": "Sofia", "edad": 28}]

print("\n" + "="*30)
print("Usuarios registrados:")
print("="*30)

for usuario in usuarios:
    print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")
