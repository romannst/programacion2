from cliente import Cliente
from formaPago import FormaPago
from estadoCompra import EstadoCompra

class Venta:
    def __init__(self, comprador:Cliente, fecha:str, productos:list, forma_pago:FormaPago, estado:EstadoCompra):
        if not isinstance(comprador, Cliente):
            raise ValueError("El comprador debe ser una instancia de Cliente.")
        if not isinstance(fecha, str) or fecha.strip() == "":
            raise ValueError("La fecha debe ser una cadena no vacía.")
        if not isinstance(productos, list):
            raise ValueError("Los productos deben ser una lista de cadenas no vacías.")
        if not isinstance(forma_pago, FormaPago):
            raise ValueError("La forma de pago debe ser una instancia de FormaPago.")
        if not isinstance(estado, EstadoCompra):
            raise ValueError("El estado debe ser una instancia de EstadoCompra.")
        self.__comprador = comprador
        self.__fecha = fecha
        self.__productos = productos
        self.__forma_pago = forma_pago
        self.__estado = estado
    
    def actualizarEstado(self, nuevo_estado:EstadoCompra):
        if not isinstance(nuevo_estado, EstadoCompra):
            raise ValueError("El nuevo estado debe ser una instancia de EstadoCompra.")
        self.__estado = nuevo_estado
    def __str__(self)->str:
        return f"Comprador: {self.__comprador}\nFecha: {self.__fecha}\nProductos: {len(self.__productos)}\nForma de Pago: {self.__forma_pago}\nEstado: {self.__estado}"