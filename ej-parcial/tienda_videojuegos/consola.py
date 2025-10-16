from tipoPlataforma import TipoPlataforma

class Consola:
    def __init__(self, codigo:int, marca:str, modelo:TipoPlataforma, almacenamiento:float, cant_joystick:int, stock:int, precio:float = 80000):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código debe ser un entero positivo.")
        if not isinstance(marca, str) or marca.strip() == "":
            raise ValueError("La marca debe ser una cadena no vacía.")
        if not isinstance(modelo, str) or modelo.strip() == "":
            raise ValueError("El modelo debe ser una cadena no vacía.")
        if not isinstance(almacenamiento, float) or almacenamiento <= 0:
            raise ValueError("El almacenamiento debe ser un número positivo.")
        if not isinstance(cant_joystick, int) or cant_joystick < 1:
            raise ValueError("La consola debe tener al menos un joystick.")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un entero no negativo.")
        if precio <= 0:
            raise ValueError("La consola no puede tener un precio negativo.")
        self.__codigo = codigo
        self.__marca = marca
        self.__modelo = modelo
        self.__almacenamiento = almacenamiento
        self.__cant_joystick = cant_joystick
        self.__stock = stock
        self.__precio = precio

    def obtenerCodigo(self) -> int:
        return self.__codigo
    def obtenerMarca(self) -> str:
        return self.__marca
    def obtenerModelo(self) -> str:
        return self.__modelo
    def obtenerAlmacenamiento(self) -> float:
        return self.__almacenamiento
    def obtenerCantJoystick(self) -> int:
        return self.__cant_joystick
    def obtenerStock(self) -> int:
        return self.__stock
    def obtenerPrecio(self) -> float:
        return self.__precio
    def __str__(self) -> str:
        return f"Código: {self.__codigo}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nAlmacenamiento: {self.__almacenamiento} GB\nCantidad de Joysticks: {self.__cant_joystick}\nStock: {self.__stock}\nPrecio: {self.__precio}"