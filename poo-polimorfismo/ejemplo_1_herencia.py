# Polimorfismo clasico mediante herencia y sobreescritura de metodos
from typing import List

class Animal:
    """
    Clase base, superclase o clase padre, de esta clase van a heredar otras clases
    """
    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre

    def hacer_sonido(self) -> str:
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
class Gato(Animal):
    def hacer_sonido(self) -> str:
        return f"{self.nombre} dice: !Miau miau!"

class Perro(Animal):
    def hacer_sonido(self) -> str:
        return f"{self.nombre} dice: !Guau guau!"

class Cerdo(Animal):
    def hacer_sonido(self) -> str:
        return f"{self.nombre} dice: !Oink oink!"

class Vaca(Animal):
    def hacer_sonido(self) -> str:
        return f"{self.nombre} dice: !Muu muu!"
    
# Funcion que puede trabajar con multiples objetos( estos objetos son este caso Gato y Perro)
def hacer_sonar_animales(animales: List[Animal]) -> None:
    print("=" * 60)
    print("🎶Concierto de Animales - Polimorfismo en Acción")
    for animal in animales:
        # Aqui ocurre el polimorfismo
        # Misma llamada animal.hacer_sonido(), pero cada objeto
        # Ejecuta su propia implementacion del metodo hacer_sonido() segun su clase
        sonido:str = animal.hacer_sonido()
        print(sonido)

def demostrar_polimorfismo_con_tipos() -> None:
    mi_perro = Perro("Bakis")
    mi_gato = Gato("Benito")
    mi_vaca = Vaca("Lola")
    mi_cerdo = Cerdo("Porky")

    granja: List[Animal] = [mi_perro, mi_gato, mi_vaca, mi_cerdo]
    hacer_sonar_animales(granja)

if __name__ == "__main__":
    demostrar_polimorfismo_con_tipos()

# animal_gato:Animal = Gato("Benito")

# animal_perro:Animal = Perro("Bakis")

# lista_animales: List[Animal] = [Gato("Benito"), Perro("Bakis"), Gato("Michi")]