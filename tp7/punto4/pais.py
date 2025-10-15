class Pais:
    def __init__(self, codigo:int, nombre:str, cantDispositivos:int):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código debe ser un entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(cantDispositivos, int) or cantDispositivos < 0:
            raise ValueError("La cantidad de dispositivos debe ser un entero no negativo.")
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cantDispositivos = cantDispositivos