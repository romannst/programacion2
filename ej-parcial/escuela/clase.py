from curso import Curso

class Clase:
    def __init__(self, fecha:str, hora:str, curso:Curso):
        if not isinstance(fecha, str) or fecha.strip() == "":
            raise ValueError("La fecha debe ser una cadena no vacía.")
        if not isinstance(hora, str) or hora.strip() == "":
            raise ValueError("La hora debe ser una cadena no vacía.")
        if not isinstance(curso, Curso):
            raise ValueError("El curso debe ser una instancia de la clase Curso.")
        self.__fecha = fecha
        self.__hora = hora
        self.__curso = curso

    def obtenerHorario(self)->str:
        return f"{self.__fecha} a las {self.__hora}"
    def obtenerCurso(self)->Curso:
        return self.__curso
    def __str__(self)->str:
        return f"Horario: {self.obtenerHorario()}\nCurso: {self.__curso.obtenerNombre()} - Dictado por: {self.__curso.obtenerProfesor().obtenerNombre()}"