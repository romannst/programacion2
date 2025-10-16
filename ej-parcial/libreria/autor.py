class Autor:
    def __init__(self, codigo:int, nombre:str, biografia:str):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código del autor debe ser un número entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre del autor no puede estar vacío.")
        if not isinstance(biografia, str) or biografia.strip() == "":
            raise ValueError("La biografía del autor no puede estar vacía.")
        self.__codigo = codigo
        self.__nombre = nombre
        self.__biografia = biografia
    
    def __str__(self)->str:
        return f"Autor: {self.__nombre}\nBiografía: {self.__biografia}"