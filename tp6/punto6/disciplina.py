from participante import Participante

class Disciplina:
    def __init__(self, nombre:str, descripcion:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(descripcion, str) or descripcion.strip() == "":
            raise ValueError("La descripción debe ser una cadena no vacía.")
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__participantes = list()
    
    def establecer_nombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self.__nombre = nombre
    def establecer_descripcion(self, descripcion:str):
        if not isinstance(descripcion, str) or descripcion.strip() == "":
            raise ValueError("La descripción debe ser una cadena no vacía.")
        self.__descripcion = descripcion
    def obtener_nombre(self)->str:
        return self.__nombre
    def obtener_descripcion(self)->str:
        return self.__descripcion
    def obtener_participantes(self)->list:
        if len(self.__participantes) == 0:
            print(f"No hay participantes inscritos en la disciplina {self.__nombre}.")
        return self.__participantes
    def agregar_participante(self, participante:Participante):
        if not isinstance(participante, Participante):
            raise ValueError("El objeto debe ser una instancia de la clase Participante.")
        self.__participantes.append(participante)
    def eliminar_participante(self, participante:Participante):
        if not isinstance(participante, Participante):
            raise ValueError("El objeto debe ser una instancia de la clase Participante.")
        if participante in self.__participantes:
            self.__participantes.remove(participante)
        else:
            raise ValueError("El participante no está en la lista de la disciplina.")
    def mostrar_participantes(self):
        if len(self.__participantes) == 0:
            print(f"No hay participantes inscritos en la disciplina {self.__nombre}.")
        else:
            print(f"Participantes en la disciplina {self.__nombre}:")
            for participante in self.__participantes:
                print(f"- {participante.obtener_nombre()}, Edad: {participante.obtener_edad()}, Nacionalidad: {participante.obtener_nacionalidad()}")