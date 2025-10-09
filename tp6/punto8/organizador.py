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

    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerCorreo(self)->str:
        return self.__correo_e
    def obtenerEspecialidad(self)->str:
        return self.__especialidad
        
    def __str__(self)->str:
        return f"{self.__nombre}\n Correo: {self.__correo_e}\n Especialidad: {self.__especialidad}"