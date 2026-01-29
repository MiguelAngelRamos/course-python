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
    }

}

# CONSTANTES DE DESCUENTOS
UMBRAL_MAYORISTA = 10.0 # Cantidad minina para ser considerado mayorista
IMPUESTO = 0.19 # Impuesto sobre las ventas (19%)
DESCUENTO_PRIMERA_COMPRA = 0.10 # 10% para nuevos clientes