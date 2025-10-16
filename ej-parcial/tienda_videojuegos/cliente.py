class Cliente:
    def __init__(self, nombre:str, dni:int, telefono:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("El DNI debe ser un entero positivo.")
        if not isinstance(telefono, str) or telefono.strip() == "":
            raise ValueError("El teléfono debe ser una cadena no vacía.")
        self.__nombre = nombre
        self.__dni = dni
        self.__telefono = telefono
    
    def __str__(self)->str:
        return f"Nombre: {self.__nombre}\tDNI: {self.__dni}\tTeléfono: {self.__telefono}"