from color import Color

class Borde:
    def __init__(self, grosor:int, color:Color):
        if not isinstance(grosor, int) or grosor < 0:
            raise ValueError("El grosor debe ser un entero no negativo.")
        if not isinstance(color, Color):
            raise ValueError("El color debe ser una instancia de la clase Color.")
        self.__grosor = grosor
        self.__color = color
    def establecerGrosor(self, grosor:int):
        if not isinstance(grosor, int) or grosor < 0:
            raise ValueError("El grosor debe ser un entero no negativo.")
        self.__grosor = grosor
    def establecerColor(self, color:Color):
        if not isinstance(color, Color):
            raise ValueError("El color debe ser una instancia de la clase Color.")
        self.__color = color
    def copiarValores(self, borde="Borde"):
        if not isinstance(borde, Borde):
            raise ValueError("El borde debe ser una instancia de la clase Borde.")
        self.__grosor = borde.obtenerGrosor()
        self.__color = borde.obtenerColor()
    def obtenerGrosor(self)->int:
        return self.__grosor
    def obtenerColor(self)->Color:
        return self.__color
    def clonar(self)->"Borde":
        borde_clonado = Borde(self.__grosor, self.__color)
        return borde_clonado
    def esIgualQue(self, borde:"Borde")->bool:
        if not isinstance(borde, Borde):
            raise ValueError("El borde debe ser una instancia de la clase Borde.")
        return self.__grosor == borde.obtenerGrosor() and self.__color.esIgualQue(borde.obtenerColor())
    def __str__(self) -> str:
        return f"Borde(grosor={self.__grosor}, color={self.__color})"