from inmueble import Inmueble
from propietario import Propietario

class Quinta(Inmueble):
    def __init__(self, codigo:int, domicilio:str, prop:Propietario, metros2:int, estado:int, metrosParque:int):
        super().__init__(codigo, domicilio, prop, metros2, estado)
        if not isinstance(metrosParque, int) or metrosParque <= 0:
            raise ValueError("Los metros de parque deben ser un entero positivo.")
        self.__metrosParque = metrosParque
    
    def establecerEstado(self, nuevoEstado: int):
        super().establecerEstado(nuevoEstado)
    def costoAlquiler(self, base:int)->float:
        return super().costoAlquiler(base) + 500 * (self.__metrosParque / 15)
    def precioVenta(self, m2:float)->float:
        return super().precioVenta(m2) + self.__metrosParque * (m2 / 2)
    def __str__(self):
        return f"{super().__str__()}\nMetros de Parque: {self.__metrosParque}"