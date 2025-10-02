class Color:
    __MAX_VALOR = 255
    __MIN_VALOR = 0
    def __init__(self, rojo:int=__MAX_VALOR, verde:int=__MAX_VALOR, azul:int=__MAX_VALOR):
        if not isinstance(rojo, int) or not isinstance(verde, int) or not isinstance(azul, int):
            raise TypeError("Los valores de color deben ser enteros.")
        self.__rojo = rojo if Color.__MIN_VALOR <= rojo <= Color.__MAX_VALOR else (Color.__MIN_VALOR if rojo < Color.__MIN_VALOR else Color.__MAX_VALOR)
        self.__verde = verde if Color.__MIN_VALOR <= verde <= Color.__MAX_VALOR else (Color.__MIN_VALOR if verde < Color.__MIN_VALOR else Color.__MAX_VALOR)
        self.__azul = azul if Color.__MIN_VALOR <= azul <= Color.__MAX_VALOR else (Color.__MIN_VALOR if azul < Color.__MIN_VALOR else Color.__MAX_VALOR)
    def variar(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un entero.")
        self.variarRojo(valor)
        self.variarAzul(valor)
        self.variarVerde(valor)
    def variarRojo(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un entero.")
        if self.__rojo + valor >= Color.__MAX_VALOR:
            self.__rojo = Color.__MAX_VALOR
        elif self.__rojo + valor <= Color.__MIN_VALOR:
            self.__rojo = Color.__MIN_VALOR
        else:
            self.__rojo += valor
    def variarAzul(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un entero.")
        if self.__azul + valor >= Color.__MAX_VALOR:
            self.__azul = Color.__MAX_VALOR
        elif self.__azul + valor <= Color.__MIN_VALOR:
            self.__azul = Color.__MIN_VALOR
        else:
            self.__azul += valor
    def variarVerde(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un entero.")
        if self.__verde + valor >= Color.__MAX_VALOR:
            self.__verde = Color.__MAX_VALOR
        elif self.__verde + valor <= Color.__MIN_VALOR:
            self.__verde = Color.__MIN_VALOR
        else:
            self.__verde += valor
    def establecerRojo(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor de rojo debe ser un entero.")
        if valor <= Color.__MIN_VALOR:
            self.__rojo = Color.__MIN_VALOR
        elif valor >= Color.__MAX_VALOR:
            self.__rojo = Color.__MAX_VALOR
    def establecerAzul(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor de azul debe ser un entero.")
        if valor <= Color.__MIN_VALOR:
            self.__azul = Color.__MIN_VALOR
        elif valor >= Color.__MAX_VALOR:
            self.__azul = Color.__MAX_VALOR
    def establecerVerde(self, valor:int):
        if not isinstance(valor, int):
            raise TypeError("El valor de verde debe ser un entero.")
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
        return Color(255-self.__rojo, 255-self.__verde, 255-self.__azul)
    def esIgualQue(self, otroColor:"Color")->bool:
        return self.__rojo == otroColor.obtenerRojo() and self.__verde == otroColor.obtenerVerde() and self.__azul == otroColor.obtenerAzul()
    def clonar(self)->"Color":
        color_clonado = Color(self.__rojo, self.__verde, self.__azul)
        return color_clonado
    def __str__(self):
        return f"Color(R: {self.__rojo}, G: {self.__verde}, B: {self.__azul})"