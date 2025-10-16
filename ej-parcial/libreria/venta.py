class Venta:
    def __init__(self, productos:list, fecha:str, monto:float):
        if not isinstance(productos, list) or len(productos) == 0:
            raise ValueError("La lista de productos no puede estar vacía y debe ser una lista de instancias de la clase Libro.")
        if not isinstance(fecha, str):
            raise ValueError("La fecha de la venta debe ser una cadena en formato 'YYYY-MM-DD'.")
        self.__productos = productos
        self.__fecha = fecha
        self.__monto = monto
    
    def productos(self)->list:
        return self.__productos
    def mostrarProductos(self)->str:
        productos_str = "Productos vendidos:\n"
        for producto in self.__productos:
            productos_str += f"- {producto}\n"
        return productos_str
    def __str__(self)->str:
        return f"Venta: {self.__fecha}\nProductos: {len(self.__productos)}\nMonto total: {self.__monto}"