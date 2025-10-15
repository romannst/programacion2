from inmueble import Inmueble
from propietario import Propietario

class Departamento(Inmueble):
    def __init__(self, codigo:int, domicilio:str, prop:Propietario, metros2:int, estado:int, gastosComunes:float, cochera:bool):
        super().__init__(codigo, domicilio, prop, metros2, estado)
        if not isinstance(gastosComunes, (int, float)) or gastosComunes < 0:
            raise ValueError("Los gastos comunes deben ser un número no negativo.")
        if not isinstance(cochera, bool):
            raise ValueError("Cochera debe ser un valor booleano.")
        self.__gastosComunes = gastosComunes
        self.__cochera = cochera
    
    def establecerEstado(self, nuevoEstado: int):
        return super().establecerEstado(nuevoEstado)
    def costoAlquiler(self, base:int)->float:
        if not isinstance(base, int) or base <= 0:
            raise ValueError("La base debe ser un entero positivo.")
        if self.__cochera:
            return super().costoAlquiler(base) + self.__gastosComunes * 0.55
        return super().costoAlquiler(base) + self.__gastosComunes
    def precioVenta(self, m2:float)->float:
        if not isinstance(m2, (int, float)) or m2 <= 0:
            raise ValueError("El precio por metro cuadrado debe ser un número positivo.")
        if self.__cochera:
            return super().precioVenta(m2) * 1.10
        return super().precioVenta(m2)
    def __str__(self):
        return f"{super().__str__()}\nGastos Comunes: {self.__gastosComunes}\nCochera: {'Tiene' if self.__cochera else 'No tiene'}"