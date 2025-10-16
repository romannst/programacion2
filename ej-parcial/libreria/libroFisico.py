from libro import Libro

class LibroFisico(Libro):
    def __init__(self, isbn:int, titulo:str, autor, genero:str, anio_publ, descr:str, cant_pag:int, cant_stock:int, precio:float):
        super().__init__(isbn, titulo, autor, genero, anio_publ, descr, cant_pag)
        if not isinstance(cant_stock, int) or cant_stock < 0:
            raise ValueError("La cantidad en stock debe ser un número entero no negativo.")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        self.__cant_stock = cant_stock
        self.__precio = precio

    def obtenerPrecio(self)->float:
        return self.__precio
    def actualizarStock(self, cantidad:int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad a actualizar debe ser un número entero positivo.")
        self.__cant_stock += cantidad
    def __str__(self) -> str:
        return super().__str__() + f"\nCantidad en stock: {self.__cant_stock}\nPrecio: {self.__precio}"