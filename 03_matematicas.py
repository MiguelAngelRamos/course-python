# Operaciones Matemáticas Básicas

print("Operaciones Matemáticas Básicas")
print(f"2 + 3 * 4 = {2 + 3 * 4}")
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")

# abs() - Valor Absoluto
print("Valor Absoluto")
print(f"abs(-10) = {abs(-10)}")
print(f"abs(10) = {abs(10)}")

# pow() - Potencia
print("Potencia")
print(f"pow(2, 3) = {pow(2, 3)}")  # 2 elevado a la 3
print(f"pow(5, 2) = {pow(5, 2)}")  # 5 elevado a la 2

# round() - Redondeo
print("Redondeo")
print(f"round(3.7) = {round(3.7)}")
print(f"round(3.5) = {round(3.5)}")
print(f"round(3.14159265359) = {round(3.14159265359, 4)}")  # Redondear a 4 decimales

# max() y min() - Valores Máximo y Mínimo
print("Valores Máximo y Mínimo")
print(f"max(1, 5, 3, 9, 2) = {max(1, 5, 3, 9, 2)}")
print(f"min(1, 5, 3, 9, 2) = {min(1, 5, 3, 9, 2)}")

# sum() - Suma de Elementos
print("Suma de Elementos")
numeros = [1, 2, 3, 4, 5]
print(f"sum({numeros}) = {sum(numeros)}")
# Sum con valor inicial
print(f"sum({numeros}, 10) = {sum(numeros, 10)}")  # Suma con valor inicial 10

# divmod() -- División y Módulo
print("División y Módulo")
cociente, resto = divmod(17, 5)
print(f"divmod(17, 5) = (Cociente: {cociente}, Resto: {resto})")

# Constantes Matematicas
import math
print("Constantes Matemáticas")
print(f"math.pi = {math.pi}")

# Funciones de redondeo de math
print("Funciones de redondeo de math")
print(f"math.ceil(4.3) = {math.ceil(4.3)}")    # Redondeo hacia arriba
print(f"math.floor(4.7) = {math.floor(4.7)}")  # Redondeo hacia abajo
print(f"math.trunc(4.7) = {math.trunc(4.7)}")  # Trunca La parte decimal

# Potecias y Raices
print("Potencias y Raíces")
print(f"math.sqrt(16) = {math.sqrt(16)}")  # Raíz cuadrada
print(f"math.pow(2, 5) = {math.pow(2, 5)}")    # Potencia usando math.pow
print(f"math.exp(2) = {math.exp(2)}")      # e elevado a la 2

# Logaritmos
print("Logaritmos")
print(f"math.log(10) = {math.log(10)}")        # Logaritmo natural (base e)
print(f"math.log10(100) = {math.log10(100)}")  # Logaritmo base 10
print(f"math.log2(8) = {math.log2(8)}")        # Logaritmo base 2
print(f"math.log(8, 2) = {math.log(8, 2)}")   # Logaritmo base arbitraria
