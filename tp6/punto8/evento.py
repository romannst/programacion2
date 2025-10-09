from fecha import Fecha
from organizador import Organizador
from participante import Participante

class Evento:
    def __init__(self, nombre:str, fecha:Fecha, descripcion:str):
        if not isinstance(fecha, Fecha) or fecha is None:
            raise TypeError("fecha debe ser una instancia de Fecha")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("nombre debe ser una cadena no vacía")
        if not isinstance(descripcion, str) or descripcion.strip() == "":
            raise ValueError("descripcion debe ser una cadena no vacía")
        self.__nombre = nombre
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__organizador = None
        self.__participantes = list()

    def asignarOrganizador(self, org:Organizador):
        if not isinstance(org, Organizador) or org is None:
            raise TypeError("org debe ser una instancia de Organizador")
        self.__organizador = org
    def agregarParticipante(self, p:Participante):
        if not isinstance(p, Participante) or p is None:
            raise TypeError("p debe ser una instancia de Participante")
        self.__participantes.append(p)
    def __str__(self)->str:
        return f"Evento: {self.__nombre}\n Fecha: {self.__fecha}\n Descripcion: {self.__descripcion}\n Organizador: {self.__organizador.obtenerNombre() if self.__organizador else 'No asignado'}\n Participantes: {len(self.__participantes)}"