from abc import ABC, abstractmethod

class Personal(ABC):
    def __init__(self, dni:int, nombre:str, apellido:str, fecha_ingreso:str):
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("El DNI debe ser un número entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(apellido, str) or apellido.strip() == "":
            raise ValueError("El apellido debe ser una cadena no vacía.")
        if not isinstance(fecha_ingreso, str) or fecha_ingreso.strip() == "":
            raise ValueError("La fecha de ingreso debe ser una cadena no vacía.")
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_ingreso = fecha_ingreso
    
    def obtenerDNI(self)->int:
        return self._dni
    def obtenerNombreCompleto(self)->str:
        return f"{self._nombre} {self._apellido}"
    def obtenerFechaIngreso(self)->str:
        return self._fecha_ingreso
    @abstractmethod
    def consultarSalario(self)->float:
        pass
    def __str__(self)->str:
        return f"Empleado: {self.obtenerNombreCompleto()}\nDNI: {self.obtenerDNI()}\nFecha de Ingreso: {self.obtenerFechaIngreso()}"