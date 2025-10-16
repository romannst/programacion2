from venta import Venta
from libro import Libro

class Tienda:
    def __init__(self, nombre:str, direccion:str, stock_libros:list = None, ventas:list = None):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre de la tienda no puede estar vacío.")
        if not isinstance(direccion, str) or direccion.strip() == "":
            raise ValueError("La dirección de la tienda no puede estar vacía.")
        self.__nombre = nombre
        self.__direccion = direccion
        if stock_libros != None:
            if not isinstance(stock_libros, list):
                raise ValueError("El stock de libros debe ser una lista de instancias de la clase Libro.")
            else:
                self.__stock_libros = stock_libros
        else:
            self.__stock_libros = list()
        if ventas != None:
            if not isinstance(ventas, list):
                raise ValueError("Las ventas deben ser una lista de instancias de la clase Venta.")
            else:
                self.__ventas = ventas
        else:
            self.__ventas = list()
    
    def actualizarStock(self, libro, cantidad:int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un número entero positivo.")
        if libro in self.__stock_libros:
            raise ValueError("El libro ya está en stock.")
        for _ in range(cantidad):
            self.__stock_libros.append(libro)
    def venta(self, info:Venta):
        if not isinstance(info, Venta):
            raise ValueError("La información de la venta debe ser una instancia de la clase Venta.")
        for libro in info.productos():
            if isinstance(libro, Libro):
                if libro in self.__stock_libros:
                    self.__stock_libros.remove(libro)
                else:
                    raise ValueError(f"El libro {libro.obtenerTitulo()} no está en stock.")
            else:
                raise ValueError("Todos los productos deben ser instancias de la clase Libro.")
        self.__ventas.append(info)
    def __str__(self)->str:
        return f"Tienda: {self.__nombre}\nDirección: {self.__direccion}\nStock de libros: {len(self.__stock_libros)}\nVentas realizadas: {len(self.__ventas)}"