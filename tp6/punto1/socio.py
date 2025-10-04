from fecha import Fecha

class Socio:
    def __init__(self, nombre:str, nacimiento:Fecha):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(nacimiento, Fecha):
            raise ValueError("nacimiento debe ser una instancia de Fecha.")
        self.__nombre = nombre
        self.__fechaNacimiento = nacimiento
        self.__fechaPenalizacion = None
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self.__nombre = nombre
    def establecerFechaNacimiento(self, fecha:Fecha):
        if not isinstance(fecha, Fecha):
            raise ValueError("fecha debe ser una instancia de Fecha.")
        self.__fechaNacimiento = fecha
    def establecerFechaPenalizacion(self, fechaHasta:Fecha):
        if not isinstance(fechaHasta, Fecha):
            raise ValueError("fechaHasta debe ser una instancia de Fecha.")
        self.__fechaPenalizacion = fechaHasta
    def estaHabilitado(self, fecha:Fecha)->bool:
        if not isinstance(fecha, Fecha):
            raise ValueError("fecha debe ser una instancia de Fecha.")
        if self.__fechaPenalizacion is None:
            return True
        return self.__fechaPenalizacion.esAnterior(fecha)
    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerFechaNacimiento(self)->Fecha:
        return self.__fechaNacimiento
    def obtenerFechaPenalizacion(self)->Fecha:
        if self.__fechaPenalizacion is None:
            raise ValueError("El socio no tiene penalización.")
        return self.__fechaPenalizacion
    def __str__(self) -> str:
        return f"Socio: {self.__nombre} \nFecha de Nacimiento: {self.__fechaNacimiento} \nPenalización: {self.__fechaPenalizacion if self.__fechaPenalizacion else 'Ninguna'}"