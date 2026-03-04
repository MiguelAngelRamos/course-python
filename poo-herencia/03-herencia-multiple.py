class Empleado:
    def trabajar(self):
        print("Trabajando...")

class FrontendDeveloper(Empleado):
    def render(self):
        print("Rendering the frontend...")
    def trabajar(self):
        super().trabajar()  # Llamamos al método trabajar de la clase padre (Empleado)
        print("Trabajando en el frontend...")


class BackendDeveloper(Empleado):
    def conectar_base_datos(self):
        print("Connecting to the database...")
    def trabajar(self):
        super().trabajar()  # Llamamos al método trabajar de la clase padre (Empleado)
        print("Trabajando en el backend...")

# Queres aplicar el concepto de multiple herencia para crear una clase FullStackDeveloper que herede de ambas clases anteriores.
class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def trabajar(self):
        super().trabajar()
        print("Trabajando como Full Stack Developer... soy el mejor de los dos mundos!")

# Uso

developer = FullStackDeveloper() # Creando una instancia de FullStackDeveloper y asignandola a la variable "developer"
developer.render()  # Método heredado de FrontendDeveloper
developer.conectar_base_datos()  # Método heredado de BackendDeveloper
developer.trabajar()  # ¿Cuál método se ejecutará? El de FrontendDeveloper o el de BackendDeveloper?

print(FullStackDeveloper.__mro__)  # Muestra el orden de resolución de métodos (Method Resolution Order) para la clase FullStackDeveloper