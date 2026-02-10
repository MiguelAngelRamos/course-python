"""
Ejercicio 1: Sistema de Descuentos en Tienda
Enunciado: Una tienda departamental tiene un sistema de descuentos basado en el monto de compra y el tipo de membresía del cliente.

Reglas:

Si el cliente tiene membresía Premium:

- Compras mayores a $1000: 25% de descuento
- Compras entre $500 y $1000: 20% de descuento
- Compras menores a $500: 15% de descuento

Si el cliente tiene membresía Regular:

- Compras mayores a $1000: 15% de descuento
- Compras entre $500 y $1000: 10% de descuento
- Compras menores a $500: 5% de descuento

Si el cliente No tiene membresía:

- Compras mayores a $1000: 5% de descuento
- Compras menores a $1000: Sin descuento

Tareas:

- Solicitar al usuario el monto de la compra
- Solicitar el tipo de membresía (Premium, Regular, Ninguna)
- Calcular el descuento correspondiente
- Mostrar el monto final a pagar

"""

## Sistema de descuentos en tienda
# Solicitar al usuario el monto de la compra
monto_compra = float(input("Ingrese el monto de su compra: $"))
# Solicitar el tipo de membresía
tipo_membresia = input("Ingrese su tipo de membresía (Premium, Regular, Ninguna): ").strip().lower()

# Calcular el descuento correspondiente
descuento = 0

if tipo_membresia == "premium":
    if monto_compra > 1000:
        descuento = 0.25
        print("¡Eres un cliente Premium! Tienes un descuento del 25%.")
    elif monto_compra >= 500 and monto_compra <= 1000:
        descuento = 0.20
    elif monto_compra < 500:
        descuento = 0.15

elif tipo_membresia == "regular":
    if monto_compra > 1000:
        descuento = 0.15
    elif monto_compra >= 500 and monto_compra <= 1000:
        descuento = 0.10
    elif monto_compra < 500:
        descuento = 0.05
else: # No tiene membresía
    if monto_compra > 1000:
        descuento = 0.05
    else:
        descuento = 0