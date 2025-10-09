class TipoEntrada:
    def __init__(self, nombre:str, precio:float):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número no negativo.")
        self.__nombre = nombre if nombre.lower() == "general" or nombre.lower() == "vip" else "General"
        self.__precio = 250 if self.__nombre.lower() == "general" or self.__nombre.lower() == "gral" else 500 if self.__nombre.lower() == "vip" else precio
        
    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerPrecio(self)->float:
        return self.__precio
    def __str__(self):
        return f"Tipo de entrada: {self.__nombre}\n Precio: ${self.__precio}"
    