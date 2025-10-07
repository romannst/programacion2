from mascota import Mascota

class Cuidador:
    def __init__(self, nombre:str, direccion:str, telefono:int):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(direccion, str) or direccion.strip() == "":
            raise ValueError("La dirección debe ser una cadena no vacía.")
        if not isinstance(telefono, int) or telefono < 0:
            raise ValueError("El teléfono debe ser un entero no negativo.")
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__mascotas = list()  # Lista para almacenar las mascotas asignadas al cuidador

    def obtenerNombre(self):
        return self.__nombre
    def obtenerTelefono(self):
        return self.__telefono
    def asignarMascota(self, mascota:Mascota):
        if not isinstance(mascota, Mascota):
            raise ValueError("La mascota debe ser una instancia de la clase Mascota.")
        self.__mascotas.append(mascota)
        mascota.asignarCuidador(self)
    def obtenerMascotas(self):
        if len(self.__mascotas) == 0:
            print("El cuidador no tiene mascotas asignadas.")
        return self.__mascotas
    def __str__(self) -> str:
        return f"Cuidador: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}, Mascotas a cargo: {len(self.__mascotas)}"