from typing import List

class Capitulo:
    def __init__(self, titulo_capitulo: str, numero_paginas: int) -> None:
        self.titulo_capitulo = titulo_capitulo
        self.numero_paginas = numero_paginas

    def get_titulo(self) -> str:
        return self.titulo_capitulo


class Libro:
    def __init__(self, titulo: str, autor: str) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.capitulos: List[Capitulo] = [] # La lista de capitulos nace vacia

    def get_titulo(self) -> str:
        return self.__titulo
    
    def get_autor(self) -> str:
        return self.__autor
    
    # COMPOSICION
    def crear_y_agregar_capitulo(self, titulo_capitulo: str, numero_paginas: int) -> None:
        # el libro crea un capitulo que NO EXISTE de forma independiente, es aqui donde se establece la relacion de composicion entre el libro y el capitulo
        nuevo_capitulo = Capitulo(titulo_capitulo, numero_paginas)
        self.capitulos.append(nuevo_capitulo)
    
    def mostrar_indice(self):
        print(f"Índice de '{self.__titulo}':")
        for capitulo in self.capitulos:
            print(f"- {capitulo.get_titulo()}")



class Biblioteca:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.catalogo: List[Libro] = [] # La lista de libros nace vacia
    
    # Que tipo de asociacion es esta? Agregacion o composicion? Justifica tu respuesta
    def agregar_libro(self, libro: Libro) -> None:
        # la biblioteca recibe un libro que YA EXISTE de forma independiente, es aqui donde se establece la relacion de agregacion entre la biblioteca y el libro
        self.catalogo.append(libro)
    
    def mostrar_catalogo(self) -> None:
        print(f"Catálogo de la biblioteca '{self.nombre}':")
        for libro in self.catalogo:
            print(f"- {libro.get_titulo()}")


class Lector:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
    
    # Colaboracion
    # El lector no tiene una relacion de agregacion ni composicion con el libro, simplemente colabora con el libro al leerlo, el libro no forma parte del lector ni el lector forma parte del libro, ambos existen de forma independiente y pueden colaborar entre si sin que uno dependa del otro
    # No hay persistencia de la relacion entre el lector y el libro, el lector puede leer cualquier libro sin necesidad de que el libro forme parte del lector o viceversa, simplemente colaboran entre si en el momento de la lectura

    def leer_libro(self, libro: Libro) -> None:
        print(f"{self.nombre} está leyendo '{libro.get_titulo()}' de {libro.get_autor()}")
        libro.mostrar_indice()




if __name__ == "__main__":
    pass
