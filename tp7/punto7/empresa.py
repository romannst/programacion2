from personal import Personal
from empleado_comision import EmpleadoComision

class Empresa:
    def __init__(self, nombre:str, empleados:list = None):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre de la empresa debe ser una cadena no vacía.")
        self.__nombre = nombre
        if empleados != None:
            self.__empleados = empleados
        else:
            self.__empleados = list()
    
    def agregarEmpleado(self, nuevo_e:Personal):
        if not isinstance(nuevo_e, Personal):
            raise TypeError("El empleado debe ser una instancia de la clase Personal.")
        if nuevo_e.obtenerDNI() in [e.obtenerDNI() for e in self.__empleados if isinstance(e, Personal)]:
            print("Error: Ya existe un empleado con ese DNI en la empresa.")
        else:
            self.__empleados.append(nuevo_e)
    def eliminarEmpleado(self, e_despedido:Personal):
        if not isinstance(e_despedido, Personal):
            raise TypeError("El empleado debe ser una instancia de la clase Personal.")
        if e_despedido in self.__empleados:
            self.__empleados.remove(e_despedido)
        else:
            print("Error: El empleado no se encuentra en la empresa.")
    def consultarSalarios(self)->list:
        lista_salarios = list()
        for empleado in self.__empleados:
            if isinstance(empleado, Personal):
                lista_salarios.append(empleado.consultarSalario())
        return lista_salarios
    def empleadoConMasClientesCaptados(self)->EmpleadoComision:
        empleado_top = None
        max_clientes = -1
        for empleado in self.__empleados:
            if isinstance(empleado, EmpleadoComision):
                if empleado.obtenerClientesCaptados() > max_clientes:
                    max_clientes = empleado.obtenerClientesCaptados()
                    empleado_top = empleado
        if empleado_top is None:
            raise ValueError("No hay empleados de tipo EmpleadoComision en la empresa.")
        return empleado_top