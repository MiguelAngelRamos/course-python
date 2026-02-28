class Habitacion:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

class Casa:
    def __init__(self, direccion: str) -> None:
        self.direccion = direccion
        # las habitaciones son parte de la casa, no existen de forma independiente
        # hay un alto grado de acoplamiento entre la casa y sus habitaciones
        self.habitaciones = [
            Habitacion("Dormitorio"),
            Habitacion("Cocina"),
            Habitacion("Baño")
        ]

mi_casa = Casa("Av. Siempre Viva 742") # La casa nace con sus habitaciones ya creadas

del mi_casa # Destruimos la casa, lo que también destruye sus habitaciones
# Intentamos acceder a las habitaciones después de destruir la casa
print(mi_casa.habitaciones) # Esto generará un error porque la casa y sus habitaciones ya no existen