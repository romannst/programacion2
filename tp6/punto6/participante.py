class Participante:
    def __init__(self, nombre:str, edad:int, nacionalidad:str):
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un entero no negativo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(nacionalidad, str) or nacionalidad.strip() == "":
            raise ValueError("La nacionalidad debe ser una cadena no vacía.")
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplinas = list()
    
    def establecer_nombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self.__nombre = nombre
    def establecer_edad(self, edad:int):
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un entero no negativo.")
        self.__edad = edad
    def establecer_nacionalidad(self, nacionalidad:str):
        if not isinstance(nacionalidad, str) or nacionalidad.strip() == "":
            raise ValueError("La nacionalidad debe ser una cadena no vacía.")
        self.__nacionalidad = nacionalidad
    def obtener_nombre(self)->str:
        return self.__nombre
    def obtener_edad(self)->int:
        return self.__edad
    def obtener_nacionalidad(self)->str:
        return self.__nacionalidad
    def obtener_disciplinas(self)->list:
        if len(self.__disciplinas) == 0:
            print(f"{self.__nombre} no está inscrito en ninguna disciplina.")
        return self.__disciplinas
    def agregar_disciplina(self, disciplina="Disciplina"):
        from disciplina import Disciplina
        if not isinstance(disciplina, Disciplina):
            raise ValueError("El objeto debe ser una instancia de la clase Disciplina.")
        if disciplina not in self.__disciplinas:
            self.__disciplinas.append(disciplina)
            disciplina.agregar_participante(self)
        else:
            print(f"{self.__nombre} ya está inscrito en la disciplina {disciplina.obtener_nombre()}.")
    def eliminar_disciplina(self, disciplina="Disciplina"):
        from disciplina import Disciplina
        if not isinstance(disciplina, Disciplina):
            raise ValueError("El objeto debe ser una instancia de la clase Disciplina.")
        if disciplina in self.__disciplinas:
            self.__disciplinas.remove(disciplina)
            disciplina.eliminar_participante(self)
        else:
            raise ValueError("La disciplina no está en la lista del participante.")
    def mostrar_disciplinas(self):
        if len(self.__disciplinas) == 0:
            print(f"{self.__nombre} no está inscrito en ninguna disciplina.")
        else:
            print(f"Disciplinas de {self.__nombre}:")
            for disciplina in self.__disciplinas:
                print(f"- {disciplina.obtener_nombre()}: {disciplina.obtener_descripcion()}")