from videojuego import Videojuego
from consola import Consola

class VideojuegoFisico(Videojuego):
    def __init__(self, id:int, nombre:str, genero:str, anio_lanz:int, descr:str, mult_online:bool, consolas_comp:list[Consola], cant_stock:int, precio:float = 15000):
        super().__init__(id, nombre, genero, anio_lanz, descr, mult_online, consolas_comp)
        if not isinstance(cant_stock, int) or cant_stock < 0:
            raise ValueError("La cantidad de stock debe ser un entero no negativo.")
        if precio <= 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__cant_stock = cant_stock
        self.__precio = precio
    
    def obtenerStock(self)->int:
        return self.__cant_stock
    def obtenerPrecio(self)->float:
        if self.__cant_stock <= 5:
            return self.__precio * 1.10  # Aumenta un 10% si el stock es 5 o menos
        return self.__precio
    def actualizarStock(self, nueva_cant:int):
        if not isinstance(nueva_cant, int) or nueva_cant < 0:
            raise ValueError("La nueva cantidad de stock debe ser un entero no negativo.")
        self.__cant_stock = nueva_cant
    def __str__(self) -> str:
        return super().__str__() + f"\nStock: {self.__cant_stock}\nPrecio: {self.__precio}"
    