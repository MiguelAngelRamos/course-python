# Diccionario
inventario_frutas = {
    "manzana": {
        "precio": 2.50, # float numero decimal representa dinero
        "stock": 50, # int: cantidad en inventario
        "unidad": "kg" # str: unidad de medida
    },
    "banana": {
        "precio": 1.80,
        "stock": 100,
        "unidad": "kg"
    },
    "naranja": {
        "precio": 3.00,
        "stock": 75,
        "unidad": "kg"
    },
    "pera": {
        "precio": 2.80,
        "stock": 60,
        "unidad": "kg"
    },
    "uva": {
        "precio": 4.00,
        "stock": 40,
        "unidad": "kg"
    },
    "fresa": {
        "precio": 5.00,
        "stock": 30,
        "unidad": "kg"
    }

}

# CONSTANTES DE DESCUENTOS
DESCUESTO_MAYORISTA = 0.15 # 15% de descuento para compras mayores a 10kg
UMBRAL_MAYORISTA = 10.0 # Cantidad minina para ser considerado mayorista
DESCUENTO_PRIMERA_COMPRA = 0.10 # 10% para nuevos clientes
IMPUESTO = 0.19 # Impuesto sobre las ventas (19%)
