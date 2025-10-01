class Color:
    __MAX_VALOR = 255
    def __init__(self, rojo:int, verde:int, azul:int):
        if not isinstance(rojo, int) or not isinstance(verde, int) or not isinstance(azul, int):
            raise TypeError("Los valores de color deben ser enteros.")
        self.rojo = Color.__MAX_VALOR
        self.verde = Color.__MAX_VALOR
        self.azul = Color.__MAX_VALOR
    
    def __str__(self):
        return f"Color(R: {self.rojo}, G: {self.verde}, B: {self.azul})"