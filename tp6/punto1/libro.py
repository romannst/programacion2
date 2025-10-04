class Libro:
    def __init__(self, nombre:str, autor:str, editorial:str, categoria:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(autor, str) or autor.strip() == "":
            raise ValueError("El autor debe ser una cadena no vacía.")
        if not isinstance(editorial, str) or editorial.strip() == "":
            raise ValueError("La editorial debe ser una cadena no vacía.")
        if not isinstance(categoria, str) or categoria.strip() == "":
            raise ValueError("La categoría debe ser una cadena no vacía.")
        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria
    def obtenerNombre(self):
        return self.__nombre
    def obtenerAutor(self):
        return self.__autor
    def obtenerEditorial(self):
        return self.__editorial
    def obtenerCategoria(self):
        return self.__categoria
    def __str__(self)->str:
        return f"'{self.__nombre}' de {self.__autor} \nEditorial: {self.__editorial} \nCategoría: {self.__categoria}"