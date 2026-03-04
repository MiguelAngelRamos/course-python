"""
Ejercicio: Sistema de Gestión de Empleados

Dada la clase base Empleado, tu tarea es modelar el equipo de una empresa tecnológica aplicando herencia y el uso correcto de super().

Implementa las siguientes clases:

Gerente(Empleado) — Además del nombre y salario base, un gerente tiene un bono (float). Al obtener sus detalles de pago, debe mostrar la información del padre más el bono aplicado al salario: salario_total = salario_base + bono.

Diseñador(Empleado) — Además del nombre y salario base, un diseñador tiene una herramienta principal (ej: "Figma", "Photoshop"). Sus detalles de pago deben incluir la herramienta que domina.

Requisitos:

Usa super().__init__(...) para inicializar los atributos heredados.
Usa super().obtener_detalles_pago() como base al sobreescribir el método.
Usa type hints en todos los parámetros y métodos.

Usa el poder de Super por extension:  El hijo usa super() para ejecutar la lógica del padre y luego añade la suya.

"""

class Empleado:
    """Representa la base de cualquier trabajador en la empresa."""
   
    def __init__(self, nombre: str, salario_base: float) -> None:
        self.nombre: str = nombre
        self.salario_base: float = salario_base
 
    def obtener_detalles_pago(self) -> str:
        return f"Empleado: {self.nombre} | Salario base: ${self.salario_base:.2f}"
 
 
class Gerente(Empleado):
    """Representa a un gerente con un bono adicional."""
   
    def __init__(self, nombre: str, salario_base: float, bono: float) -> None:
        super().__init__(nombre, salario_base)
        self.bono: float = bono
 
    def obtener_detalles_pago(self) -> str:
        # Usamos la lógica del padre
        detalles_base: str = super().obtener_detalles_pago()
        salario_total: float = self.salario_base + self.bono
       
        # Extendemos la funcionalidad
        return f"{detalles_base} | Bono: ${self.bono:.2f} | Salario total: ${salario_total:.2f}"
 
 
class Diseñador(Empleado):
    """Representa a un diseñador con una herramienta principal."""
   
    def __init__(self, nombre: str, salario_base: float, herramienta_principal: str) -> None:
        super().__init__(nombre, salario_base)
        self.herramienta_principal: str = herramienta_principal
 
    def obtener_detalles_pago(self) -> str:
        # Usamos la lógica del padre
        detalles_base: str = super().obtener_detalles_pago()
       
        # Extendemos la funcionalidad
        return f"{detalles_base} | Herramienta principal: {self.herramienta_principal}"
 
 
# 🔹 Ejemplo de uso
if __name__ == "__main__":
    gerente: Gerente = Gerente("Carla", 3000.0, 800.0)
    diseñador: Diseñador = Diseñador("Diego", 2200.0, "Figma")
 
    print(gerente.obtener_detalles_pago())
    print(diseñador.obtener_detalles_pago())