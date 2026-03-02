# Cálculo de Precio con Impuestos y Descuentos

"""
1. la clase "Producto": calcula el precio base aplicando el impuesto nacional (IVA)
2. Una clase hija llamada "ProductoImportado": Necesita cálculo del padre (Precio + Iva), pero "ademas" debe sumarle el arancel de aduana.
"""

class Producto:
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base
        self.iva = 0.19  # IVA del 19%

    def calcular_precio(self):
        print(f"Calculando IVA para: {self.nombre}...")
        return self.precio_base * (1 + self.iva)
    
class ProductoImportado(Producto):
    def __init__(self, nombre, precio_base, arancel):
        super().__init__(nombre, precio_base)  # Llamada al constructor de la clase padre
        self.arancel = arancel  # Arancel adicional para productos importados

    def calcular_precio(self):
        precio_con_iva = super().calcular_precio()  # Llamada al método de la clase padre
        print(f"Calculando arancel para: {self.nombre}...")
        return precio_con_iva + self.arancel
