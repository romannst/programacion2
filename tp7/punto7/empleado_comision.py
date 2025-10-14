from personal import Personal

class EmpleadoComision(Personal):
    def __init__(self, dni:int, nombre:str, apellido:str, fecha_ingreso:str, salario_min:float, clientes_captados:int = 0, monto_cliente:float = 0):
        super().__init__(dni, nombre, apellido, fecha_ingreso)
        if not isinstance(salario_min, (int, float)) or salario_min < 0:
            raise ValueError("El salario mínimo debe ser un número no negativo.")
        if not isinstance(clientes_captados, int) or clientes_captados < 0:
            raise ValueError("La cantidad de clientes captados debe ser un entero no negativo.")
        if not isinstance(monto_cliente, (int, float)) or monto_cliente < 0:
            raise ValueError("El monto por cliente debe ser un número no negativo.")
        self.__salario_min = salario_min
        self.__clientes_captados = clientes_captados
        self.__monto_cliente = monto_cliente
    
    def agregarClienteCaptado(self, cantidad:int = 1):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad de clientes a agregar debe ser un entero positivo.")
        self.__clientes_captados += cantidad
    def obtenerClientesCaptados(self)->int:
        return self.__clientes_captados
    def obtenerMontoPorCliente(self)->float:
        return self.__monto_cliente
    def consultarSalario(self)->float:
        salario_esperado = self.__clientes_captados * self.__monto_cliente
        return salario_esperado if salario_esperado > self.__salario_min else self.__salario_min
    def __str__(self)->str:
        return super().__str__() + f"\nSalario Mínimo: {self.__salario_min}\nClientes Captados: {self.__clientes_captados}\nMonto por Cliente: {self.__monto_cliente}"