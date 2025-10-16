from libro import Libro
from platLibro import PlatLibro

class LibroDigital(Libro):
    def __init__(self, isbn:int, titulo:str, autor, genero:str, anio_publ, descr:str, cant_pag:int, plataforma:PlatLibro, tamanio:float, precio:float):
        super().__init__(isbn, titulo, autor, genero, anio_publ, descr, cant_pag)
        if not isinstance(plataforma, PlatLibro):
            raise ValueError("La plataforma debe ser una instancia de la clase PlatLibro.")
        if not isinstance(tamanio, (int, float)) or tamanio <= 0:
            raise ValueError("El tamaño debe ser un número positivo.")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        self.__plataforma = plataforma
        self.__tamanio = tamanio
        self.__precio = precio
    
    def obtenerPrecio(self)->float:
        return self.__precio
    def __str__(self)->str:
        return super().__str__() + f"\nPlataforma: {self.__plataforma}\nTamaño (MB): {self.__tamanio}\nPrecio: {self.__precio}"
