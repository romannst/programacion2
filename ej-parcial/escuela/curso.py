from profesor import Profesor

class Curso:
    def __init__(self, codigo:int, nombre:str, profesor:Profesor):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código del curso debe ser un entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre del curso debe ser una cadena no vacía.")
        if not isinstance(profesor, Profesor):
            raise ValueError("El profesor debe ser una instancia de la clase Profesor.")
        self.__codigo = codigo
        self.__nombre = nombre
        self.__profesor = profesor
        self.__estudiantes = list()
    
    def obtenerCodigo(self)->int:
        return self.__codigo
    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerProfesor(self)->Profesor:
        return self.__profesor
    def seDicta(self)->bool:
        return len(self.__estudiantes) >= 25
    def __str__(self) -> str:
        return f"Código: {self.__codigo}\nNombre: {self.__nombre}\nProfesor: {self.__profesor.obtenerNombre()}\nCantidad de inscriptos: {len(self.__estudiantes)}"