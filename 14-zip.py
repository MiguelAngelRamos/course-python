### Ejercicio: Cálculo de Precios con IVA

# 1. Definimos las listas de datos
productos = ["Monitor", "Teclado", "Mouse", "Escritorio"]
precios_netos = [150000, 15000, 10000, 85000]

# 2. Variable para el impuesto (19%)
IVA = 1.19

print("--- LISTADO DE PRECIOS FINALES ---")

# 3. Usamos zip para unir producto con su precio correspondiente
for producto, precio in zip(productos, precios_netos):
    
    # 4. Realizamos el cálculo
    precio_final = precio * IVA
    
    # 5. Mostramos el resultado formateado
    print(f"Producto: {producto:<12} | Total (IVA inc.): ${precio_final:,.0f}")

   # 150000.75 -> 150,001