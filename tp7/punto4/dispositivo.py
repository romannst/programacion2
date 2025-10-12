class Dispositivo:
    def __init__(self, id:int, nombre:str, tipo:str):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("El ID debe ser un entero positivo.")
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(tipo, str) or not tipo:
            raise ValueError("El tipo debe ser una cadena no vacía.")
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo

    def obtenerId(self)->int:
        return self.__id
    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerTipo(self)->str:
        return self.__tipo