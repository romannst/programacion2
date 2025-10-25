class Libro:
    @classmethod
    # Deserializar: Crear un objeto Libro a partir de un diccionario
    def fromDict(cls, dic:dict)->"Libro":
        if not isinstance(dic, dict):
            raise ValueError("El dato proporcionado no es un diccionario.")
        return cls(
            dic["isbn"],
            dic["titulo"],
            dic["autor"],
            dic["genero"],
            dic["anio_publicacion"]
        )
    
    def __init__(self, isbn:str, titulo:str, autor:str, genero:str, anio_publicacion:int):
        if not isinstance(isbn, str) or isbn.strip() == "":
            raise ValueError("El ISBN debe ser una cadena no vacía.")
        if not isinstance(titulo, str) or titulo.strip() == "":
            raise ValueError("El título debe ser una cadena no vacía.")
        if not isinstance(autor, str) or autor.strip() == "":
            raise ValueError("El autor debe ser una cadena no vacía.")
        if not isinstance(genero, str) or genero.strip() == "":
            raise ValueError("El género debe ser una cadena no vacía.")
        if not isinstance(anio_publicacion, int) or anio_publicacion <= 0:
            raise ValueError("El año de publicación debe ser un entero positivo.")
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio_publicacion = anio_publicacion

    def obtener_isbn(self)->str:
        return self.__isbn
    def obtener_titulo(self)->str:
        return self.__titulo
    def obtener_autor(self)->str:
        return self.__autor
    def obtener_genero(self)->str:
        return self.__genero
    def obtener_anio_publicacion(self)->int:
        return self.__anio_publicacion
    # Serializar: Convertir el objeto Libro a un diccionario
    def toDict(self)->dict:
        return {
            "isbn": self.__isbn,
            "titulo": self.__titulo,
            "autor": self.__autor,
            "genero": self.__genero,
            "anio_publicacion": self.__anio_publicacion
        }