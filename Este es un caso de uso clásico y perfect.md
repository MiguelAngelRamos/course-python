Este es un caso de uso clásico y perfecto para enseñar lógica de seguridad básica: **El Cajero Automático (ATM) y el bloqueo por intentos fallidos.**

Es un problema cotidiano que todo el mundo entiende: tienes un número limitado de oportunidades para acertar. Si aciertas, entras (break). Si agotas las oportunidades, el sistema toma una medida drástica (bloquear la tarjeta).

Aquí tienes el ejercicio planteado para una clase:

---

### 🏧 Caso de Uso: El Cajero Automático

**Enunciado del Problema:**
Estás programando el módulo de seguridad de un cajero automático. El sistema debe solicitar al usuario que ingrese su PIN de 4 dígitos.

* El usuario tiene un máximo de **3 intentos**.
* Si el usuario ingresa el PIN correcto, el sistema debe darle la bienvenida y detener el ciclo inmediatamente.
* Si el usuario falla, debe mostrar cuántos intentos le quedan.
* **Requisito Crítico:** Si el usuario agota los 3 intentos sin acertar, el sistema debe ejecutar una rutina de seguridad para **bloquear la tarjeta** y alertar al banco.

**Reto:** Implementar la lógica sin usar variables tipo "bandera" (ej: `tarjeta_bloqueada = False`), utilizando exclusivamente la estructura `while-else` de Python.

---

### Solución en Python

```python
# Configuración del sistema
pin_secreto = "1234"
max_intentos = 3
intentos_realizados = 0

print("🏦 Bienvenido al Banco Python. Inserte su tarjeta.")

while intentos_realizados < max_intentos:
    # Solicitamos el PIN
    entrada = input(f"Ingrese su PIN (Intento {intentos_realizados + 1}/{max_intentos}): ")
    
    # Verificamos credenciales
    if entrada == pin_secreto:
        print("\n✅ ¡PIN Correcto! Acceso concedido.")
        print("Cargando menú principal...")
        # El 'break' rompe el ciclo y evita que se ejecute el 'else'
        break
    
    # Si llegamos aquí, el PIN fue incorrecto
    intentos_realizados += 1
    print("❌ PIN incorrecto.")

else:
    # Este bloque SOLO se ejecuta si el while terminó porque la condición
    # (intentos_realizados < max_intentos) se volvió Falsa.
    # Es decir, NUNCA se ejecutó el break (nunca acertó).
    
    print("\n🚫 ALERTA DE SEGURIDAD")
    print("Ha excedido el número máximo de intentos.")
    print("SU TARJETA HA SIDO BLOQUEADA. Contacte a su ejecutivo.")
    # Aquí iría la lógica real de bloqueo en base de datos

```

### ¿Por qué este ejemplo funciona pedagógicamente?

1. **Elimina la Bandera:** En otros lenguajes, tendrías que haber creado una variable `exito = false` antes del bucle, ponerla en `true` si acierta, y luego hacer un `if not exito` afuera. El `while-else` hace el código más limpio.
2. **Realismo:** Simula una "transacción" donde el resultado negativo (bloqueo) es una consecuencia directa de haber agotado el ciclo, no una condición aparte.
3. **Claridad:** El `break` representa el éxito (salir del bucle de validación), y el `else` representa el fracaso total del proceso repetitivo.

¿Te sirve este escenario para tus explicaciones?