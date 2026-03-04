class Instrumento:
    def sonar(self):
        print("El instrumento haciendo sonido base...")

class Guitarra(Instrumento):
    def sonar(self):
        super().sonar()  # Llamamos al método sonar de la clase padre (Instrumento)
        print("La guitarra suena: ¡Strum strum!")

class Bajo(Instrumento):
    def sonar(self):
        super().sonar()  # Llamamos al método sonar de la clase padre (Instrumento)
        print("El bajo suena: ¡Dum dum!")

class InstrumentoPerfecto(Guitarra, Bajo):
    def sonar(self):
        super().sonar()
        print("El instrumento perfecto !Suena increíble!")

instrumento_perfecto = InstrumentoPerfecto()

instrumento_perfecto.sonar()  # ¿Qué sonido se escuchará? El de Guitarra o el de Bajo?
# print(InstrumentoPerfecto.__mro__)  # Muestra el orden de resolución de métodos (Method Resolution Order) para la clase InstrumentoPerfecto
print(InstrumentoPerfecto.__mro__)
