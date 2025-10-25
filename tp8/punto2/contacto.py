class Contacto:
    @classmethod
    def fromDict(cls, dic:dict)->"Contacto":
        return cls(
            nombre=dic.get("nombre", ""),
            apellido=dic.get("apellido", ""),
            telefono=dic.get("telefono", ""),
            correo_e=dic.get("correo_e", ""),
            direccion=dic.get("direccion", "")
        )

    def __init__(self, nombre:str, apellido:str, telefono:str, correo_e:str, direccion:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(apellido, str) or apellido.strip() == "":
            raise ValueError("El apellido debe ser una cadena no vacía.")
        if not isinstance(telefono, str) or telefono.strip() == "":
            raise ValueError("El teléfono debe ser una cadena no vacía.")
        if not isinstance(correo_e, str) or correo_e.strip() == "":
            raise ValueError("El correo electrónico debe ser una cadena no vacía.")
        if not isinstance(direccion, str) or direccion.strip() == "":
            raise ValueError("La dirección debe ser una cadena no vacía.")
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correo_e = correo_e
        self.__direccion = direccion

    def obtener_nombre(self)->str:
        return self.__nombre
    def obtener_apellido(self)->str:
        return self.__apellido
    def obtener_telefono(self)->str:
        return self.__telefono
    def obtener_correo_e(self)->str:
        return self.__correo_e
    def obtener_direccion(self)->str:
        return self.__direccion
    def toDict(self)->dict:
        return {
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "telefono": self.__telefono,
            "correo_e": self.__correo_e,
            "direccion": self.__direccion
        }