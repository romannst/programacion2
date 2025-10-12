class Cancion:
    def __init__(self, codigo:int, nombre:str, duracion:int, genero:str):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código debe ser un entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(duracion, int) or duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo.")
        if not isinstance(genero, str) or genero.strip() == "":
            raise ValueError("El género debe ser una cadena no vacía.")
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__genero = genero
    
    def obtenerCodigo(self)->int:
        return self.__codigo
    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerDuracion(self)->int:
        return self.__duracion
    def obtenerGenero(self)->str:
        return self.__genero
    def reproducir(self):
        print(f"Reproduciendo la canción: {self.__nombre}")