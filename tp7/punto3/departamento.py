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
        super().establecerEstado(nuevoEstado)
    def costoAlquiler(self, base:int)->float:
        if self.__cochera:
            return super().costoAlquiler(base) + 2000 + self.__gastosComunes
        return super().costoAlquiler(base) + self.__gastosComunes
    def precioVenta(self, m2:float)->float:
        if self.__cochera:
            return super().precioVenta(m2) + 3 * m2
        return super().precioVenta(m2)
    def __str__(self):
        return f"{super().__str__()}\nGastos Comunes: {self.__gastosComunes}\nCochera: {'Tiene' if self.__cochera else 'No tiene'}"