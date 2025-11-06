from ciudad import Ciudad
from hotel import Hotel
from tipoViaje import TipoViaje
from tipoTransporte import TipoTransporte

class PaqueteGrupal:
    @classmethod
    def fromDict(cls, data:dict)->"PaqueteGrupal":
        if not isinstance(data, dict):
            raise TypeError("El dato debe ser un diccionario")
        return cls(
            numero=data["numero"],
            ciudad=Ciudad.fromDict(data["ciudad"]),
            hotel=Hotel.fromDict(data["hotel"]),
            fecha_ida=data["fecha_ida"],
            fecha_vuelta=data["fecha_vuelta"],
            descr=data["descr"],
            viaje=TipoViaje[data["viaje"]],
            transporte=TipoTransporte[data["transporte"]],
            precio=data["precio"],
            cupo_actual=data["cupo_actual"],
            cupo_max=data["cupo_max"]
        )

    def __init__(self, numero:int, ciudad:Ciudad, hotel:Hotel, fecha_ida:str, fecha_vuelta:str, descr:str, viaje:TipoViaje, transporte:TipoTransporte, precio:float, cupo_actual:int, cupo_max:int):
        if not isinstance(numero, int) or numero < 0:
            raise TypeError("El numero debe ser un entero")
        if not isinstance(ciudad, Ciudad):
            raise TypeError("La ciudad debe ser una instancia de Ciudad")
        if not isinstance(hotel, Hotel):
            raise TypeError("El hotel debe ser una instancia de Hotel")
        if fecha_ida.strip() == "":
            raise ValueError("La fecha de ida no puede estar vacia")
        if fecha_vuelta.strip() == "":
            raise ValueError("La fecha de vuelta no puede estar vacia")
        if descr.strip() == "":
            raise ValueError("La descripcion no puede estar vacia")
        if not isinstance(viaje, TipoViaje):
            raise TypeError("El tipo de viaje debe ser una instancia de TipoViaje")
        if not isinstance(transporte, TipoTransporte):
            raise TypeError("El tipo de transporte debe ser una instancia de TipoTransporte")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise TypeError("El precio debe ser un numero positivo")
        if not isinstance(cupo_actual, int) or cupo_actual < 0:
            raise TypeError("El cupo actual debe ser un entero positivo")
        if not isinstance(cupo_max, int) or cupo_max <= 0:
            raise TypeError("El cupo maximo debe ser un entero positivo mayor que cero")
        if cupo_actual > cupo_max:
            raise ValueError("El cupo actual no puede ser mayor que el cupo maximo")
        self.__numero = numero
        self.__ciudad = ciudad
        self.__hotel = hotel
        self.__fecha_ida = fecha_ida
        self.__fecha_vuelta = fecha_vuelta
        self.__descr = descr
        self.__viaje = viaje
        self.__transporte = transporte
        self.__precio = precio
        self.__cupo_actual = cupo_actual
        self.__cupo_max = cupo_max

    def toDict(self)->dict:
        return {
            "numero": self.__numero,
            "ciudad": self.__ciudad.toDict(),
            "hotel": self.__hotel.toDict(),
            "fecha_ida": self.__fecha_ida,
            "fecha_vuelta": self.__fecha_vuelta,
            "descr": self.__descr,
            "viaje": self.__viaje.name,
            "transporte": self.__transporte.name,
            "precio": self.__precio,
            "cupo_actual": self.__cupo_actual,
            "cupo_max": self.__cupo_max
        }
    def actualizarCupo(self, nuevos_participantes:int):
        if not isinstance(nuevos_participantes, int) or nuevos_participantes < 0:
            raise TypeError("El numero de nuevos participantes debe ser un entero positivo")
        if self.__cupo_actual + nuevos_participantes > self.__cupo_max:
            raise ValueError("No hay suficiente cupo para los nuevos participantes")
        self.__cupo_actual += nuevos_participantes
    def __str__(self)->str:
        return f"------ Paquete Grupal ------\nNumero: {self.__numero}\nDescripción: {self.__descr} \n{self.__ciudad.__str__()}\nFechas: Del {self.__fecha_ida} al {self.__fecha_vuelta}\n{self.__hotel.__str__()}\nPrecio: ${self.__precio}\nCupo: {self.__cupo_actual}/{self.__cupo_max}"