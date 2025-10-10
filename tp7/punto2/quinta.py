from inmueble import Inmueble
from propietario import Propietario

class Quinta(Inmueble):
    def __init__(self, codigo:int, domicilio:str, prop:Propietario, metros2:int, estado:int, metrosParque:int):
        super().__init__(codigo, domicilio, prop, metros2, estado)
        if not isinstance(metrosParque, int) or metrosParque <= 0:
            raise ValueError("Los metros de parque deben ser un entero positivo.")
        self.__metrosParque = metrosParque
    
    def costoAlquiler(self, base:int)->float:
        if not isinstance(base, int) or base <= 0:
            raise ValueError("La base debe ser un entero positivo.")
        return super().costoAlquiler(base) + (self.__metrosParque * 2)
    def precioVenta(self, m2:float)->float:
        if not isinstance(m2, (int, float)) or m2 <= 0:
            raise ValueError("El precio por metro cuadrado debe ser un número positivo.")
        return super().precioVenta(m2) + self.__metrosParque * m2 * 0.5
    def __str__(self):
        return f"{super().__str__()}\nMetros de Parque: {self.__metrosParque}"