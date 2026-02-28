from typing import List

class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.__titulo: str = titulo
        self.__autor: str = autor
        self.set_paginas(paginas) # Validamos el número de páginas al crear el libro

    # Getters para acceder a los atributos privados solo de lectura
    def get_titulo(self) -> str:
        return self.__titulo

    def get_autor(self) -> str:
        return self.__autor

    def get_paginas(self) -> int:
        return self.__paginas

    # Setters para modificar los atributos privados si es necesario
    def set_titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    def set_autor(self, autor: str) -> None:
        self.__autor = autor

    def set_paginas(self, paginas: int) -> None:
        if paginas > 0:
            self.__paginas = paginas
        else:
            raise ValueError("El número de páginas debe ser un entero positivo.")
    
"""
Relacion de agregacion:
- crea una clase llamada biblioteca que tenga un atributo libros(una lista de objetos de la clase libro)
- implementa un metodo agregar_libro(libro: Libro) que permita agregar un libro a la lista
- implementa un metodo mostrar_libros() que muestre los titulos de todos los libros en la biblioteca.
"""
class Biblioteca:
    def __init__(self) -> None:
        self.libros: List[Libro] = [] # La lista de libros nace vacia

    def agregar_libro(self, libro: Libro) -> None:
        # la biblioteca recibe un libro que YA EXISTE de forma independiente, es aqui donde se establece la relacion de agregacion entre la biblioteca y el libro
        self.libros.append(libro)

    def mostrar_libros(self) -> None:
        print("Libros en la biblioteca:")
        for libro in self.libros:
            print(libro.get_titulo())


"""
Relacion agregacion:
"""

class Estante:
    def __init__(self) -> None:
        self.libros: List[Libro] = [] # La lista de libros nace vacia

    def agregar_libro(self, libro: Libro) -> None:
        # el estante recibe un libro que YA EXISTE de forma independiente, es aqui donde se establece la relacion de composicion entre el estante y el libro
        self.libros.append(libro)

    def mostrar_libros(self) -> None:
        print("Libros en el estante:")
        for libro in self.libros:
            print(libro.get_titulo())