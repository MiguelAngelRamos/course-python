"""
Enunciado del Problema:
Estás programando el módulo de seguridad de un cajero automático. El sistema debe solicitar al usuario que ingrese su PIN de 4 dígitos.

El usuario tiene un máximo de **3 intentos**.

- Si el usuario ingresa el PIN correcto, el sistema debe darle la bienvenida y detener el ciclo inmediatamente.
Si el usuario falla, debe mostrar cuántos intentos le quedan.

*Requisito Crítico:* Si el usuario agota los 3 intentos sin acertar, el sistema debe ejecutar una rutina de seguridad para *bloquear la tarjeta* y alertar al banco.

*Reto:* Implementar la lógica sin usar variables tipo "bandera" (ej: `tarjeta_bloqueada = False`), utilizando exclusivamente la estructura `while-else` de Python.

"""
pin_secreto = "8384"
max_intentos = 3
intentos_realizados = 0

print("Bienvenido al cajero automático. Por favor, ingrese su PIN de 4 dígitos.")

while intentos_realizados < max_intentos:
    entrada = input(f"Ingrese su PIN (Intento {intentos_realizados + 1} de {max_intentos}): ")
    if entrada == pin_secreto:
        print("PIN correcto. Bienvenido al sistema.")
        print("Acceso concedido. Puede realizar sus operaciones.")
        break

    # Si llego a este punto significa que el PIN es incorrecto
    intentos_realizados += 1 # intentos_realizados = intentos_realizados + 1
    print(f"PIN incorrecto.")
else:
    print("Has agotado tus intentos. Tu tarjeta ha sido bloqueada por seguridad.")
    print("Por favor, contacta a tu banco para más información.")
    