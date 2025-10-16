from abc import ABC, abstractmethod
from autor import Autor

class Libro(ABC):
    def __init__(self, isbn:int, titulo:str, autor:Autor, genero:str, anio_publ:str, descr:str, cant_pag:int):
        if not isinstance(isbn, int) or isbn <= 0:
            raise ValueError("El ISBN debe ser un número entero positivo.")
        if not isinstance(titulo, str) or titulo.strip() == "":
            raise ValueError("El título no puede estar vacío.")
        if not isinstance(autor, Autor):
            raise ValueError("El autor debe ser una instancia de la clase Autor.")
        if not isinstance(genero, str) or genero.strip() == "":
            raise ValueError("El género no puede estar vacío.")
        if not isinstance(anio_publ, str) or anio_publ.strip() == "":
            raise ValueError("El año de publicación debe ser una fecha válida y no puede ser en el futuro.")
        if not isinstance(descr, str) or descr.strip() == "":
            raise ValueError("La descripción no puede estar vacía.")
        if not isinstance(cant_pag, int) or cant_pag <= 0:
            raise ValueError("La cantidad de páginas debe ser un número entero positivo.")
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._anio_publ = anio_publ
        self._descr = descr
        self._cant_pag = cant_pag
    
    def obtenerISBN(self)->int:
        return self._isbn
    def obtenerTitulo(self)->str:
        return self._titulo
    def obtenerAutor(self)->Autor:
        return self._autor
    def obtenerGenero(self)->str:
        return self._genero
    def obtenerAnioPubl(self)->str:
        return self._anio_publ
    def obtenerDescr(self)->str:
        return self._descr
    def obtenerCantPag(self)->int:
        return self._cant_pag
    def establecerDescr(self, nueva_descr:str):
        if not isinstance(nueva_descr, str) or nueva_descr.strip() == "":
            raise ValueError("La nueva descripción no puede estar vacía.")
        self._descr = nueva_descr
    @abstractmethod
    def obtenerPrecio(self)->float:
        pass
    def __str__(self)->str:
        return f"ISBN: {self._isbn}\nTítulo: {self._titulo}\nAutor: {self._autor}\nGénero: {self._genero}\nAño de publicación: {self._anio_publ}\nDescripción: {self._descr}\nCantidad de páginas: {self._cant_pag}"