from abc import ABC, abstractmethod
from consola import Consola

class Videojuego(ABC):
    def __init__(self, id:int, nombre:str, genero:str, anio_lanz:int, descr:str, mult_online:bool, consolas_comp:list[Consola]):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("El id debe ser un entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(genero, str) or genero.strip() == "":
            raise ValueError("El género debe ser una cadena no vacía.")
        if not isinstance(anio_lanz, int) or anio_lanz <= 1800:
            raise ValueError("El año de lanzamiento debe ser un entero mayor que 1800.")
        if not isinstance(descr, str) or descr.strip() == "":
            raise ValueError("La descripción debe ser una cadena no vacía.")
        if not isinstance(mult_online, bool):
            raise ValueError("mult_online debe ser un valor booleano.")
        if not isinstance(consolas_comp, list):
            raise ValueError("consolas_comp debe ser una lista de objetos Consola.")
        self._id = id
        self._nombre = nombre
        self._genero = genero
        self._anio_lanz = anio_lanz
        self._descr = descr
        self._mult_online = mult_online
        self._consolas_comp = consolas_comp

    def obtenerId(self)->int:
        return self._id
    def obtenerNombre(self)->str:
        return self._nombre
    def obtenerGenero(self)->str:
        return self._genero
    def obtenerAnioLanz(self)->int:
        return self._anio_lanz
    def obtenerDescr(self)->str:
        return self._descr
    def obtenerMultOnline(self)->bool:
        return self._mult_online
    def obtenerConsolasComp(self)->list[Consola]:
        return self._consolas_comp
    def actualizarMO(self, nuevo_estado:bool):
        if not isinstance(nuevo_estado, bool):
            raise ValueError("El nuevo estado debe ser un valor booleano.")
        self._mult_online = nuevo_estado
    def esCompatible(self, consola:Consola)->bool:
        if not isinstance(consola, Consola):
            raise ValueError("El parámetro debe ser un objeto Consola.")
        return consola in self._consolas_comp
    
    @abstractmethod
    def obtenerPrecio(self)->float:
        pass
    def __str__(self) -> str:
        return f"ID: {self._id}\tNombre: {self._nombre}\tGénero: {self._genero}\tAño de Lanzamiento: {self._anio_lanz}\tDescripción: {self._descr}\tMultijugador Online: {self._mult_online}\tConsolas Compatibles: {len(self._consolas_comp)}"