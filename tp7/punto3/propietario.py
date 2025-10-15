class Propietario:
    def __init__(self, nombre:str, dni:int):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(dni, int) or len(str(dni)) != 8 or dni <= 0:
            raise ValueError("El DNI debe ser un entero positivo.")
        self.__dni = dni
        self.__nombre = nombre

    def obtenerDni(self) -> int:
        return self.__dni
    def obtenerNombre(self) -> str:
        return self.__nombre
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}\nDNI: {self.__dni}"