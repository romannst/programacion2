class Propietario:
    def __init__(self, dni:int, nombre:str, telefono:int):
        if not isinstance(dni, int) or len(str(dni)) != 8 or dni <= 0:
            raise ValueError("El DNI debe ser un entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(telefono, int) or telefono <= 0:
            raise ValueError("El teléfono debe ser un entero positivo.")
        self.__dni = dni
        self.__nombre = nombre
        self.__telefono = telefono

    def obtenerDni(self) -> int:
        return self.__dni
    def obtenerNombre(self) -> str:
        return self.__nombre
    def obtenerTelefono(self) -> int:
        return self.__telefono
    def __str__(self) -> str:
        return f"DNI: {self.__dni}\n Nombre: {self.__nombre}\n Teléfono: {self.__telefono}"