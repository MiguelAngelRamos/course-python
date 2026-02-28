class Empleado:
    def __init__(self, nombre: str, departamento: str):
        self.nombre = nombre
        self.departamento = departamento

    # Un metodo abstraco sin implementacion, que sera implementado por las subclases
    # y voy a obligar a sus subclases a implementar este metodo, para que cada tipo de empleado tenga su propia implementacion de como calcular su salario
    def calcular_salario(self) -> float:
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
    # El metodo __str__ es un metodo especial que se utiliza para representar el objeto como una cadena de texto, es decir, cuando se imprime el objeto o se convierte a string, se ejecuta este metodo para mostrar una representacion legible del objeto

    # En el vamos a imprimir todos los atributos del empleado, para que cuando imprimamos un objeto de tipo empleado, podamos ver su nombre y departamento de forma clara y legible, en lugar de mostrar la direccion de memoria del objeto o una representacion poco informativa
    def __str__(self) -> str:
        return f"Empleado: {self.nombre}, Departamento: {self.departamento}"


class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre: str, departamento: str, salario_base: float, bono_mensual: float = 0.0) -> None:
        super().__init__(nombre, departamento)
        self.salario_base = salario_base
        self.bono_mensual = bono_mensual

    def calcular_salario(self) -> float:
        salario_calculado = self.salario_base + self.bono_mensual
        return salario_calculado

class Vendedor(Empleado):
    PORCENTAJE_COMISION: float = 0.08 # 8% de comision sobre las ventas del mes
    def __init__(self, nombre:str, departamento:str, salario_base:float, ventas_del_mes:float) -> None:
        super().__init__(nombre, departamento)
        self.salario_base = salario_base
        self.ventas_del_mes = ventas_del_mes

    def calcular_salario(self) -> float:
        comision:float = self.ventas_del_mes * self.PORCENTAJE_COMISION
        salario_calculado:float = self.salario_base + comision
        return salario_calculado
    
class Freelancer(Empleado):
    def __init__(self, nombre:str, departamento:str, proyectos_entregados:int, pago_por_proyecto:float) -> None:
        super().__init__(nombre, departamento)
        self.proyectos_entregados = proyectos_entregados
        self.pago_por_proyecto = pago_por_proyecto

    def calcular_salario(self) -> float:
        salario_calculado:float = self.proyectos_entregados * self.pago_por_proyecto
        return salario_calculado
    
# Funciones de demostracion del polimorfismo con herencia
def procesar_nomina(empleados: list[Empleado]) -> None:
    print("=" * 60)
    print("Procesando Nómina - Polimorfismo en Acción")
    total_nomina:float = 0.0 # Variable para acumular el total de la nómina

    for empleado in empleados:
        salario:float = empleado.calcular_salario()
        total_nomina += salario # Acumulamos el salario de cada empleado al total de la nómina
        # total_nomina = total_nomina + salario
        print(f"{empleado} - Salario Calculado: ${salario:.2f}")
    
    print(f"Total de la Nómina: ${total_nomina:.2f}")


def demostrar_polimorfismo_con_tipos() -> None:
    print("Demostración de Polimorfismo con Herencia")
    sofia: EmpleadoAsalariado = EmpleadoAsalariado("Sofía", "Recursos Humanos", salario_base=3000.0, bono_mensual=500.0)
    catalina: Vendedor = Vendedor("Catalina", "Ventas", salario_base=2000.0, ventas_del_mes=15000.0)
    diego: Freelancer = Freelancer("Diego", "Desarrollo", proyectos_entregados=5, pago_por_proyecto=800.0)

    equipo: list[Empleado] = [sofia, catalina, diego]
    procesar_nomina(equipo)


if __name__ == "__main__":
    demostrar_polimorfismo_con_tipos()