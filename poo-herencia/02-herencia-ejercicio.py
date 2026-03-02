"""
Ejercicio: Sistema de Gestión de Empleados

Dada la clase base Empleado, tu tarea es modelar el equipo de una empresa tecnológica aplicando herencia y el uso correcto de super().

Implementa las siguientes clases:

Gerente(Empleado) — Además del nombre y salario base, un gerente tiene un bono (float). 
Al obtener sus detalles de pago, debe mostrar la información 
del padre más el bono aplicado al salario: salario_total = salario_base + bono.

Diseñador(Empleado) — Además del nombre y salario base, un diseñador tiene
una herramienta principal (ej: "Figma", "Photoshop"). 
Sus detalles de pago deben incluir la herramienta que domina.

Requisitos:

Usa super().__init__(...) para inicializar los atributos heredados.
Usa super().obtener_detalles_pago() como base al sobreescribir el método.
Usa type hints en todos los parámetros y métodos.

Usa el poder de Super por extension:  El hijo usa super() para ejecutar la lógica del padre y luego añade la suya.

"""

class Empleado:
    """Representa la base de cualquier trabajador en la empresa."""
    
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    def obtener_detalles_pago(self) -> str:
        return f"Empleado: {self.nombre} | Salario: ${self.salario_base:.2f}"
