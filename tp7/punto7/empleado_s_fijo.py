from personal import Personal

class EmpleadoSFijo(Personal):
    def __init__(self, dni:int, nombre:str, apellido:str, fecha_ingreso:str, sueldo_basico:float, anios_antiguedad:int = 0):
        super().__init__(dni, nombre, apellido, fecha_ingreso)
        if not isinstance(sueldo_basico, (int, float)) or sueldo_basico < 0:
            raise ValueError("El sueldo básico debe ser un número no negativo.")
        if not isinstance(anios_antiguedad, int) or anios_antiguedad < 0:
            raise ValueError("Los años de antigüedad deben ser un entero no negativo.")
        self.__sueldo_basico = sueldo_basico
        self.__anios_antiguedad = anios_antiguedad
    
    def obtenerSueldoBasico(self)->float:
        return self.__sueldo_basico
    def actualizarAniosAntiguedad(self, nuevos_anios:int):
        if not isinstance(nuevos_anios, int) or nuevos_anios < 0:
            raise ValueError("Los años de antigüedad deben ser un entero no negativo.")
        self.__anios_antiguedad = nuevos_anios
    def consultarSalario(self)->float:
        salario_esperado = self.__sueldo_basico
        if self.__anios_antiguedad >= 2 and self.__anios_antiguedad <= 5:
            salario_esperado += self.__sueldo_basico * 0.05
        elif self.__anios_antiguedad > 5:
            salario_esperado += self.__sueldo_basico * 0.1
        return salario_esperado
    def __str__(self)->str:
        return super().__str__() + f"\nSueldo Básico: {self.__sueldo_basico}\nAños de Antigüedad: {self.__anios_antiguedad}"
