from fecha import Fecha
from tipoEntrada import TipoEntrada

class Entrada:
    def __init__(self, numero:int, fecha:Fecha, tipo:TipoEntrada):
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("El número de entrada debe ser un número entero no negativo.")
        if not isinstance(fecha, Fecha) or fecha is None:
            raise TypeError("La fecha debe ser una instancia de la clase Fecha.")
        if not isinstance(tipo, TipoEntrada) or tipo is None:
            raise TypeError("El tipo debe ser una instancia de la clase TipoEntrada.")
        self.__numero = numero
        self.__fecha = fecha
        self.__tipo = tipo

    def obtenerNumero(self):
        return self.__numero
    def obtenerFecha(self):
        return self.__fecha
    def obtenerTipo(self):
        return self.__tipo
    def __str__(self):
        return f"Número: {self.__numero}\n Fecha: {self.__fecha}\n Tipo: {self.__tipo}"