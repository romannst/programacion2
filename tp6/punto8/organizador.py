from evento import Evento

class Organizador:
    def __init__(self, nombre:str, correo_e:str, especialidad:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("nombre debe ser una cadena no vacía")
        if not isinstance(correo_e, str) or correo_e.strip() == "":
            raise ValueError("correo_e debe ser una cadena no vacía")
        if not isinstance(especialidad, str) or especialidad.strip() == "":
            raise ValueError("especialidad debe ser una cadena no vacía")
        self.__nombre = nombre
        self.__correo_e = correo_e
        self.__especialidad = especialidad
        self.__eventos = list()

    def asignarEvento(self, evento:Evento):
        if not isinstance(evento, Evento) or evento is None:
            raise TypeError("evento debe ser una instancia de Evento")
        self.__eventos.append(evento)
        evento.asignarOrganizador(self)
    def __str__(self)->str:
        return f"Organizador: {self.__nombre}, Correo: {self.__correo_e}, Especialidad: {self.__especialidad}, Eventos: {len(self.__eventos)}"