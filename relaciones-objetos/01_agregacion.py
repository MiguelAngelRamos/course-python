from typing import List

class Jugador:
    def __init__(self, nombre: str):
        self.nombre = nombre

class ClubFutbol:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.jugadores: List[Jugador] = [] # La lista nace vacia

    def fichar_jugador(self, jugador: Jugador) -> None:
        # el club recibe un jugador que YA EXISTE de forma independiente
        self.jugadores.append(jugador)


cr7 = Jugador("Cristiano Ronaldo") # El jugador nace de forma independiente
messi = Jugador("Lionel Messi") # El jugador nace de forma independiente

real_madrid = ClubFutbol("Real Madrid") # El club nace de forma independiente
real_madrid.fichar_jugador(cr7) #* Se establece la relacion de agregacion entre el club y el jugador

barcelona = ClubFutbol("Barcelona") # El club nace de forma independiente
barcelona.fichar_jugador(messi) #* Se establece la relacion de agregacion entre el club y el jugador

del real_madrid # Destruimos el club, pero el jugador sigue existiendo
print(cr7.nombre) # El jugador sigue existiendo a pesar de que el club ha sido

del barcelona # Destruimos el club, pero el jugador sigue existiendo
print(messi.nombre) # El jugador sigue existiendo a pesar de que el club ha sido