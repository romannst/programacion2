import random

class Automovil:

    def __init__(self, marca:str, modelo:str, anio:int, velocidadMaxima:float, velocidadActual:float):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidadMaxima = velocidadMaxima
        self.velocidadActual = velocidadActual
    #comandos
    def establecerMarca(self, marca:str):
        self.marca = marca
    def establecerModelo(self, modelo:str):
        self.modelo = modelo
    def establecerAnio(self, anio:int):
        self.anio = anio
    def establecerVelocidadMaxima(self, velocidadMaxima:float):
        self.velocidadMaxima = velocidadMaxima
    def establecerVelocidadActual(self, velocidadActual:float):
        self.velocidadActual = velocidadActual
    def acelerar(self, incrementoVelocidad:int):
        if incrementoVelocidad > 0:
            if self.velocidadActual == self.velocidadMaxima or self.velocidadActual + incrementoVelocidad > self.velocidadMaxima:
                self.velocidadActual = self.velocidadMaxima
                print(f"El automóvil alcanzó su velocidad máxima, {self.velocidadMaxima} km/h.")
            else:
                self.velocidadActual += incrementoVelocidad
        else:
            print("El incremento de velocidad debe ser positivo.")
    def desacelerar(self, decrementoVelocidad:int):
        if decrementoVelocidad > 0:
            if self.velocidadActual == 0 or self.velocidadActual - decrementoVelocidad < 0:
                self.velocidadActual = 0
                print(f"El automóvil llegó a su velocidad mínima, {self.velocidadActual} km/h.")
            else:
                self.velocidadActual -= decrementoVelocidad
        else:
            print("El decremento de velocidad debe ser positivo.")
    def frenarPorCompleto(self):
        self.velocidadActual = 0
        print("El automóvil se ha detenido por completo.")
    #consultas
    def obtenerMarca(self) -> str:
        return self.marca
    def obtenerModelo(self) -> str:
        return self.modelo
    def obtenerAnio(self) -> int:
        return self.anio
    def obtenerVelocidadMaxima(self) -> float:
        return self.velocidadMaxima
    def obtenerVelocidadActual(self) -> float:
        return self.velocidadActual
    def calcularMinutosParaLlegar(self, distanciaKM:float) -> int:
        if self.velocidadActual > 0:
            minutos_para_llegar = int((distanciaKM / self.velocidadActual) * 60)
            return minutos_para_llegar
        print("El auto está detenido y no se puede calcular el tiempo para llegar.")
        return 0