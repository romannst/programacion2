from evento import Evento

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
        self.__eventos = list()
    def registrarseEvento(self, evento:Evento):
        if not isinstance(evento, Evento) or evento is None:
            raise TypeError("evento debe ser una instancia de Evento")
        self.__eventos.append(evento)
        evento.agregarParticipante(self)
    def __str__(self)->str:
        return f"Participante: {self.__nombre}, Correo: {self.__correo_e}, Telefono: {self.__telefono}, Eventos: {len(self.__eventos)}"