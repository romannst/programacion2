class Profesor:
    def __init__(self, id:int, nombre:str, especialidad:str, cursos_dictados:list = None):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("El ID debe ser un entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(especialidad, str) or especialidad.strip() == "":
            raise ValueError("La especialidad debe ser una cadena no vacía.")
        if cursos_dictados is None:
            self.__cursos_dictados = list()
        else:
            if not isinstance(cursos_dictados, list):
                raise ValueError("Los cursos dictados deben ser una lista.")
            else:
                self.__cursos_dictados = cursos_dictados
        self.__id = id
        self.__nombre = nombre
        self.__especialidad = especialidad

    def obtenerID(self):
        return self.__id
    def obtenerNombre(self):
        return self.__nombre
    def obtenerEspecialidad(self):
        return self.__especialidad
    def nuevaEspecialidad(self, nueva_especialidad:str):
        if not isinstance(nueva_especialidad, str) or nueva_especialidad.strip() == "":
            raise ValueError("La nueva especialidad debe ser una cadena no vacía.")
        self.__especialidad = nueva_especialidad
    def agregarCurso(self, nuevo_curso):
        if nuevo_curso in self.__cursos_dictados:
            raise ValueError("El curso ya está en la lista de cursos dictados.")
        self.__cursos_dictados.append(nuevo_curso)
    def __str__(self) -> str:
        return f"ID: {self.__id}\nNombre: {self.__nombre}\nEspecialidad: {self.__especialidad}\nCursos dictados: {len(self.__cursos_dictados)}"