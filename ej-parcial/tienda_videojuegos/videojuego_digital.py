from videojuego import Videojuego
from consola import Consola
from tipoPlataforma import TipoPlataforma
from tipoDistribuidora import TipoDistribuidora

class VideojuegoDigital(Videojuego):
    def __init__(self, id:int, nombre:str, genero:str, anio_lanz:int, descr:str, mult_online:bool, consolas_comp:list[Consola], plataforma:TipoPlataforma, tamanio:float, distribuidora:TipoDistribuidora, precio:float = 15000):
        super().__init__(id, nombre, genero, anio_lanz, descr, mult_online, consolas_comp)
        if not isinstance(plataforma, TipoPlataforma):
            raise ValueError("plataforma debe ser un valor del enum TipoPlataforma.")
        if not isinstance(tamanio, float) or tamanio <= 0:
            raise ValueError("tamanio debe ser un número positivo.")
        if not isinstance(distribuidora, TipoDistribuidora):
            raise ValueError("distribuidora debe ser un valor del enum TipoDistribuidora.")
        if precio <= 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__plataforma = plataforma
        self.__tamanio = tamanio
        self.__distribuidora = distribuidora
        self.__precio = precio
    
    def obtenerPlataforma(self)->TipoPlataforma:
        return self.__plataforma
    def obtenerTamanio(self)->float:
        return self.__tamanio
    def obtenerDistribuidora(self)->TipoDistribuidora:
        return self.__distribuidora
    def obtenerPrecio(self)->float:
        if self.__distribuidora == TipoDistribuidora.EA:
            return self.__precio + 5000  # Costo de suscripción anual
        return self.__precio
    def actualizacion(self, tamanio_agregado:float):
        if not isinstance(tamanio_agregado, float) or tamanio_agregado <= 0:
            raise ValueError("El nuevo tamaño debe ser un número positivo.")
        self.__tamanio += tamanio_agregado
    def __str__(self) -> str:
        return super().__str__() + f"\nPlataforma: {self.__plataforma.value}\nTamaño (GB): {self.__tamanio}\nDistribuidora: {self.__distribuidora.name}\nPrecio: {self.obtenerPrecio()}"