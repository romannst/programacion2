class Empleado:
    #constructor
    def __init__(self, legajo:int, cantHoras:int=0, valorHora:float=0.0):
        self.__legajo = legajo
        self.__cantHoras = cantHoras
        self.__valorHora = valorHora
    #comandos
    def establecerHorasTrabajadas(self, cantHoras:int):
        self.__cantHoras = cantHoras
    def establecerValorHora(self, valorHora:float):
        self.__valorHora = valorHora
    #consultas
    def obtenerLegajo(self) -> int:
        return self.__legajo
    def obtenerHorasTrabajadas(self) -> int:
        return self.__cantHoras
    def obtenerValorHora(self) -> float:
        return self.__valorHora
    def obtenerSueldo(self) -> float:
        return self.__cantHoras * self.__valorHora