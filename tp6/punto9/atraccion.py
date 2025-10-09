class Atraccion:
    def __init__(self, nombre:str, tipo:str, nivel_emocion:str, min_estatura:float):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(tipo, str) or tipo.strip() == "":
            raise TypeError("El tipo debe ser una cadena de texto.")
        if not isinstance(nivel_emocion, str) or nivel_emocion.strip() == "":
            raise TypeError("El nivel de emoción debe ser una cadena de texto.")
        if not isinstance(min_estatura, (int, float)) or min_estatura < 0.5:
            raise ValueError("La estatura mínima debe ser un número no negativo.")
        self.__nombre = nombre
        self.__tipo = tipo
        self.__nivel_emocion = nivel_emocion
        self.__min_estatura = min_estatura
        self.__turnos = list()

    def obtenerNombre(self):
        return self.__nombre
    def obtenerTipo(self):
        return self.__tipo
    def obtenerNivelEmocion(self):
        return self.__nivel_emocion
    def obtenerMinEstatura(self):
        return self.__min_estatura
    def agregarTurno(self, turno:str):
        if not isinstance(turno, str) or turno.strip() == "":
            raise TypeError("El turno debe ser una cadena de texto.")
        self.__turnos.append(turno)
    