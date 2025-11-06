from ciudad import Ciudad
from tipoPension import TipoPension

class Hotel:
    @classmethod
    def fromDict(cls, data:dict)->"Hotel":
        if not isinstance(data, dict):
            raise TypeError("El dato debe ser un diccionario")
        return cls(
            nombre=data["nombre"],
            ciudad=Ciudad.fromDict(data["ciudad"]),
            descr=data["descr"],
            estrellas=data["estrellas"],
            pension=TipoPension[data["pension"]]
        )

    def __init__(self, nombre:str, ciudad:Ciudad, descr:str, estrellas:int, pension:TipoPension):
        if nombre.strip() == "":
            raise ValueError("El nombre del hotel no puede estar vacio")
        if not isinstance(ciudad, Ciudad):
            raise TypeError("La ciudad debe ser una instancia de Ciudad")
        if descr.strip() == "":
            raise ValueError("La descripcion no puede estar vacia")
        if not isinstance(estrellas, int) or estrellas < 1 or estrellas > 5:
            raise ValueError("Las estrellas deben ser un entero entre 1 y 5")
        if not isinstance(pension, TipoPension):
            raise TypeError("El tipo de pension debe ser una instancia de TipoPension")
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__descr = descr
        self.__estrellas = estrellas
        self.__pension = pension
    
    def toDict(self)->dict:
        return {
            "nombre": self.__nombre,
            "ciudad": self.__ciudad.toDict(),
            "descr": self.__descr,
            "estrellas": self.__estrellas,
            "pension": self.__pension.name
        }
    
    def __str__(self)->str:
        return f"------ Hotel ------\nNombre: {self.__nombre}\nDescripcion: {self.__descr}\nEstrellas: {self.__estrellas}\nPension: {self.__pension.name}"