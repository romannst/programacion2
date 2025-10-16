from curso import Curso

class Estudiante:
    def __init__(self, id:int, nombre:str, fecha_nac:str):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("El ID debe ser un número entero.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena de texto no vacía.")
        if not isinstance(fecha_nac, str) or fecha_nac.strip() == "":
            raise ValueError("La fecha de nacimiento debe ser una cadena de texto no vacía.")
        self.__id = id
        self.__nombre = nombre
        self.__fecha_nac = fecha_nac
        self.__cursos = list()
    
    def obtenerID(self):
        return self.__id
    def obtenerNombre(self):
        return self.__nombre
    def obtenerFechaNac(self):
        return self.__fecha_nac
    def cursosInscripto(self)->str:
        cod_cursos = ""
        for curso in self.__cursos:
            if isinstance(curso, Curso):
                #guardo los cursos con tabulaciones
                cod_cursos += f"\t{curso.obtenerCodigo()}\n"
            else:
                raise ValueError("La lista de cursos contiene un elemento que no es una instancia de la clase Curso.")
        return f"Cursos Inscripto: {cod_cursos}"
    def inscribirse(self, curso:Curso):
        if not isinstance(curso, Curso):
            raise ValueError("El curso debe ser una instancia de la clase Curso.")
        if curso in self.__cursos:
            raise ValueError("El estudiante ya está inscrito en este curso.")
        self.__cursos.append(curso)
    def darse_baja(self, curso:Curso):
        if not isinstance(curso, Curso):
            raise ValueError("El curso debe ser una instancia de la clase Curso.")
        if curso not in self.__cursos:
            raise ValueError("El estudiante no está inscrito en este curso.")
        self.__cursos.remove(curso)
    def __str__(self)->str:
        return f"ID: {self.__id}\nNombre: {self.__nombre}\nFecha de Nacimiento: {self.__fecha_nac}\nCursos Inscripto: {len(self.__cursos)}"