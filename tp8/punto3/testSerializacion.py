from paqueteGrupal import PaqueteGrupal
from ciudad import Ciudad
from hotel import Hotel
from tipoPension import TipoPension
from tipoTransporte import TipoTransporte
from tipoViaje import TipoViaje
import json

class TestSerializacion:
    @staticmethod
    def run():
        print("\nComenzando pruebas de serializacion...\n")
        #prueba de serializacion y deserializacion
        # parametros de un objeto ciudad( nombre, provincia, puntos_turisticos: str )
        ciudad1 = Ciudad("Buenos Aires", "Buenos Aires", "Obelisco, Casa Rosada")
        hotel1 = Hotel("Hotel Central", ciudad1, "Hotel en el centro de la ciudad", 4, TipoPension.MEDIA_PENSION)
        paquete1 = PaqueteGrupal(1, ciudad1, hotel1, "2024-12-01", "2024-12-10", "Paquete turistico a Buenos Aires", TipoViaje.TURISMO, TipoTransporte.AVION, 1500.0, 10, 20)
        #crea varios objetos de cada clase
        ciudad2 = Ciudad("Cordoba", "Cordoba", "Catedral, Parque Sarmiento")
        hotel2 = Hotel("Hotel Cordoba", ciudad2, "Hotel en el centro de Cordoba", 3, TipoPension.PENSION_COMPLETA)
        paquete2 = PaqueteGrupal(2, ciudad2, hotel2, "2024-11-15", "2024-11-25", "Paquete turistico a Cordoba", TipoViaje.AVENTURA, TipoTransporte.COLECTIVO, 1200.0, 5, 15)
        ciudad3 = Ciudad("Mendoza", "Mendoza", "Parque General San Martin, Bodega Catena Zapata")
        hotel3 = Hotel("Hotel Mendoza", ciudad3, "Hotel en el centro de Mendoza", 5, TipoPension.PENSION_COMPLETA)
        paquete3 = PaqueteGrupal(3, ciudad3, hotel3, "2024-10-05", "2024-10-15", "Paquete turistico a Mendoza", TipoViaje.TURISMO, TipoTransporte.COLECTIVO, 2000.0, 8, 12)
        with open("./tp8/punto3/paquetes.json", "w") as file:
            dicc_paquetes = [paquete1.toDict(), paquete2.toDict(), paquete3.toDict()]
            json.dump(dicc_paquetes, file, ensure_ascii=False, indent=4)
        print("...")
        print("Serializacion completada!\n")

if __name__ == "__main__":
    TestSerializacion.run()