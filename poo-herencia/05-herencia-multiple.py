
"""
¿Qué es un mixin?

Un mixin es una clase diseñada para "aportar un comportamiento especifico" a otras clases a través de la herencia múltiple, un mixin no pretende ser una entidad de dominio por si misma.

Un mixin no representa un "Qué es", sino un "que puede hacer"
"""

class EmpleadoMixin:
    def comer(self):
        print("Comiendo...")
    def dormir(self):
        print("Durmiendo...")

class ProgramadorMixin:
    def programar(self):
        print("Programando...")

class DiseñadorMixin:
    def diseñar(self):
        print("Diseñando...")

class VendedorMixin:
    def vender(self):
        print("Vendiendo...")


class IngenieroInformatica(EmpleadoMixin, ProgramadorMixin):
    pass


class DiseñadorGrafico(EmpleadoMixin, DiseñadorMixin):
    pass

class VendedorTecnologico(EmpleadoMixin, VendedorMixin):
    pass


"""
Definicion copilot:
Un mixin es una clase que proporciona métodos adicionales a otras clases sin ser una clase base directa. Se utiliza para compartir funcionalidades comunes entre diferentes clases sin necesidad de crear una jerarquía de herencia compleja. Los mixins permiten agregar comportamientos específicos a las clases de manera modular y reutilizable.
"""