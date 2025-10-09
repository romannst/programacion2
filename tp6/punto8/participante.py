class Participante:
    def __init__(self, nombre:str, correo_e:str, telefono:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("nombre debe ser una cadena no vacía")
        if not isinstance(correo_e, str) or correo_e.strip() == "":
            raise ValueError("correo_e debe ser una cadena no vacía")
        if not isinstance(telefono, str) or telefono.strip() == "":
            raise ValueError("telefono debe ser una cadena no vacía")
        self.__nombre = nombre
        self.__correo_e = correo_e
        self.__telefono = telefono

    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerCorreo(self)->str:
        return self.__correo_e
    def obtenerTelefono(self)->str:
        return self.__telefono
    def __str__(self)->str:
        return f"Participante: {self.__nombre}\n Correo: {self.__correo_e}\n Telefono: {self.__telefono}"