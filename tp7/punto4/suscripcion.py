from abc import ABC, abstractmethod

class Suscripcion(ABC):
    def __init__(self, nombre:str, email:str, telefono:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(email, str) or "@" not in email or email.strip() == "":
            raise ValueError("El email debe ser una cadena válida que contenga '@'.")
        if not isinstance(telefono, str) or telefono.strip() == "":
            raise ValueError("El teléfono debe ser una cadena no vacía.")
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    @abstractmethod
    def reproducirMusica(self):
        pass