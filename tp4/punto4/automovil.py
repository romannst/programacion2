import random

class Automovil:

    def __init__(self, marca:str, modelo:str, anio:int, velocidadMaxima:float, velocidadActual:float):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__velocidadMaxima = velocidadMaxima
        self.__velocidadActual = velocidadActual
    #comandos
    def establecerMarca(self, marca:str):
        self.__marca = marca
    def establecerModelo(self, modelo:str):
        self.__modelo = modelo
    def establecerAnio(self, anio:int):
        self.__anio = anio
    def establecerVelocidadMaxima(self, velocidadMaxima:float):
        self.__velocidadMaxima = velocidadMaxima
    def establecerVelocidadActual(self, velocidadActual:float):
        self.__velocidadActual = velocidadActual
    def acelerar(self, incrementoVelocidad:int):
        if incrementoVelocidad > 0:
            if self.__velocidadActual == self.__velocidadMaxima or self.__velocidadActual + incrementoVelocidad > self.__velocidadMaxima:
                self.__velocidadActual = self.__velocidadMaxima
                print(f"El automóvil alcanzó su velocidad máxima, {self.__velocidadMaxima} km/h.")
            else:
                self.__velocidadActual += incrementoVelocidad
        else:
            print("El incremento de velocidad debe ser positivo.")
    def desacelerar(self, decrementoVelocidad:int):
        if decrementoVelocidad > 0:
            if self.__velocidadActual == 0 or self.__velocidadActual - decrementoVelocidad < 0:
                self.__velocidadActual = 0
                print(f"El automóvil llegó a su velocidad mínima, {self.__velocidadActual} km/h.")
            else:
                self.__velocidadActual -= decrementoVelocidad
        else:
            print("El decremento de velocidad debe ser positivo.")
    def frenarPorCompleto(self):
        self.__velocidadActual = 0
        print("El automóvil se ha detenido por completo.")
    #consultas
    def obtenerMarca(self) -> str:
        return self.__marca
    def obtenerModelo(self) -> str:
        return self.__modelo
    def obtenerAnio(self) -> int:
        return self.__anio
    def obtenerVelocidadMaxima(self) -> float:
        return self.__velocidadMaxima
    def obtenerVelocidadActual(self) -> float:
        return self.__velocidadActual
    def calcularMinutosParaLlegar(self, distanciaKM:float) -> int:
        if self.__velocidadActual > 0:
            minutos_para_llegar = int((distanciaKM / self.__velocidadActual) * 60)
            return minutos_para_llegar
        print("El auto está detenido y no se puede calcular el tiempo para llegar.")
        return 0