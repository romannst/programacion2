class Color:
    __MAX_VALOR = 255
    __MIN_VALOR = 0
    def __init__(self, rojo:int, verde:int, azul:int):
        if not isinstance(rojo, int) or not isinstance(verde, int) or not isinstance(azul, int):
            raise TypeError("Los valores de color deben ser enteros.")
        self.__rojo = Color.__MAX_VALOR
        self.__verde = Color.__MAX_VALOR
        self.__azul = Color.__MAX_VALOR
    def variar(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un entero.")
        
    def variarRojo(self, valor:int):
        pass
    def variarAzul(self, valor:int):
        pass
    def variarVerde(self, valor:int):
        pass
    def establecerRojo(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor de rojo debe ser un entero.")
        else:
            if valor <= Color.__MIN_VALOR:
                self.__rojo = Color.__MIN_VALOR
            elif valor >= Color.__MAX_VALOR:
                self.__rojo = Color.__MAX_VALOR
    def establecerAzul(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor de azul debe ser un entero.")
        else:
            if valor <= Color.__MIN_VALOR:
                self.__azul = Color.__MIN_VALOR
            elif valor >= Color.__MAX_VALOR:
                self.__azul = Color.__MAX_VALOR
    def establecerVerde(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor de verde debe ser un entero.")
        else:
            if valor <= Color.__MIN_VALOR:
                self.__verde = Color.__MIN_VALOR
            elif valor >= Color.__MAX_VALOR:
                self.__verde = Color.__MAX_VALOR
    def copiar(self, otroColor:"Color"):
        if not isinstance(otroColor, Color):
            raise TypeError("El parámetro debe ser una instancia de Color.")
        self.__rojo = otroColor.obtenerRojo()
        self.__verde = otroColor.obtenerVerde()
        self.__azul = otroColor.obtenerAzul()
    def obtenerRojo(self) -> int:
        return self.__rojo
    def obtenerVerde(self) -> int:
        return self.__verde
    def obtenerAzul(self) -> int:
        return self.__azul
    def esRojo(self) -> bool:
        return self.__rojo == Color.__MAX_VALOR and self.__verde == Color.__MIN_VALOR and self.__azul == Color.__MIN_VALOR
    def esGris(self) -> bool:
        return self.__rojo == self.__verde == self.__azul
    def esNegro(self) -> bool:
        return self.__rojo == Color.__MIN_VALOR and self.__verde == Color.__MIN_VALOR and self.__azul == Color.__MIN_VALOR
    def complemento(self)->"Color": 
        return Color(0,0,0)
    def esIgualQue(self, otroColor:"Color")->bool:
        return self.__rojo == otroColor.obtenerRojo() and self.__verde == otroColor.obtenerVerde() and self.__azul == otroColor.obtenerAzul()
    def clonar(self)->"Color":
        color_clonado = Color(self.__rojo, self.__verde, self.__azul)
        return color_clonado
    def __str__(self):
        return f"Color(R: {self.__rojo}, G: {self.__verde}, B: {self.__azul})"