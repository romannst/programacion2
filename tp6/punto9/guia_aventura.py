from visitante import Visitante
from atraccion import Atraccion

class GuiaAventura:
    def __init__(self, numero:int, turno_trabajo:str):
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("El número de guía debe ser un número entero no negativo.")
        if not isinstance(turno_trabajo, str) or turno_trabajo.strip() == "":
            raise TypeError("El turno de trabajo debe ser una cadena de texto.")
        self.__numero = numero
        self.__turno_trabajo = turno_trabajo
    
    def obtenerNumero(self):
        return self.__numero
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
        return f"Número: {self.__numero}\n Turno de trabajo: {self.__turno_trabajo}"