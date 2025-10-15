from visitante import Visitante
from atraccion import Atraccion

class GuiaAventura:
    def __init__(self, nombre:str, turno_trabajo:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise TypeError("El nombre del guía debe ser una cadena de texto.")
        if not isinstance(turno_trabajo, str) or turno_trabajo.strip() == "":
            raise TypeError("El turno de trabajo debe ser una cadena de texto.")
        self.__nombre = nombre
        self.__turno_trabajo = turno_trabajo

    def obtenerNombre(self):
        return self.__nombre
    def obtenerTurnoTrabajo(self):
        return self.__turno_trabajo
    def autorizaIngreso(self, visitante:Visitante, atraccion:Atraccion)->bool:
        if not isinstance(visitante, Visitante):
            raise TypeError("El visitante debe ser una instancia de la clase Visitante.")
        if visitante.obtenerEstatura() >= atraccion.obtenerMinEstatura():
            visitante.atraccionesVisitadas().append(atraccion)
            return True
        return False
    def __str__(self):
        return f"Nombre: {self.__nombre}\n Turno de trabajo: {self.__turno_trabajo}"