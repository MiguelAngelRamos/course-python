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

def mostrar_catalogo(inventario):
    pass

def validar_fruta_existe(nombre_fruta, inventario):
    pass

## S.O.L.I.D - S: Single Responsibility Principle
def validar_cantidad(cantidad):
    pass

def calcular_subtotal(precio_unitario, cantidad):
    pass

def aplicar_descuentos(subtotal, cantidad, es_primera_compra):
    pass

def calcular_impuesto(precio_con_descuentos):
    pass

def actualizar_stock(nombre_fruta, cantidad, inventario):
    pass

def mostrar_recibo(nombre_fruta, cantidad, precio_unitario, subtotal, 
                   descuento_porcentaje, monto_descuento, nombre_descuento, 
                   precio_con_descuentos, impuesto, total_final):
    pass

def procesar_venta():
    pass


if __name__ == "__main__":
    procesar_venta()
    