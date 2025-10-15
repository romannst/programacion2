from propietario import Propietario

class Inmueble:
    def __init__(self, codigo:int, domicilio:str, prop:Propietario, metros2:int, estado:int):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código debe ser un entero positivo.")
        if not isinstance(domicilio, str) or domicilio.strip() == "":
            raise ValueError("El domicilio debe ser una cadena no vacía.")
        if not isinstance(prop, Propietario) or prop is None:
            raise ValueError("El propietario debe ser una instancia válida de Propietario.")
        if not isinstance(metros2, int) or metros2 <= 0:
            raise ValueError("Los metros2 deben ser un entero positivo.")
        if not isinstance(estado, int) or estado < 0:
            raise ValueError("El estado debe ser un entero no negativo.")
        self._codigo = codigo
        self._domicilio = domicilio
        self._propietario = prop
        self._metros2 = metros2
        self._estado = estado #refiere a las condiciones del inmueble, desde 0 a 10
    
    def establecerEstado(self, nuevoEstado:int):
        if not isinstance(nuevoEstado, int) or nuevoEstado < 0:
            raise ValueError("El estado debe ser un entero no negativo.")
        self._estado = nuevoEstado
    def costoAlquiler(self, base:int)->float:
        if not isinstance(base, int) or base <= 0:
            raise ValueError("La base debe ser un entero positivo.")
        return base * self._metros2 * (1 + self._estado * 0.1)
    def precioVenta(self, m2:float)->float:
        if not isinstance(m2, (int, float)) or m2 <= 0:
            raise ValueError("El precio por metro cuadrado debe ser un número positivo.")
        return m2 * self._metros2 * (1 + self._estado * 0.1)
    def __str__(self):
        return f"Código: {self._codigo}\nDomicilio: {self._domicilio}\nPropietario: {self._propietario.obtenerNombre()}\nMetros Cuadrados: {self._metros2}\nEstado: {self._estado}"