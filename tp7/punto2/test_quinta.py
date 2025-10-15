from quinta import Quinta
from propietario import Propietario

class TestQuinta:
    @staticmethod
    def run():
        #testear servicios de la clase Quinta
        propietario = Propietario(87654321, "Maria Gomez", 123456789)
        quinta = Quinta(2, "Calle Real 456", propietario, 300, 6, 150)
        print("------- Quinta creada -------")
        print(quinta)
        # Test costoAlquiler
        costo_alquiler = quinta.costoAlquiler(250)
        print(f"------- Costo de Alquiler -------")
        print(f"Costo de Alquiler: {costo_alquiler:.2f}")
        print("-----------------------------------")
        # Test precioVenta
        precio_venta = quinta.precioVenta(3000)
        print(f"------- Precio de Venta -------")
        print(f"Precio de Venta: {precio_venta:.2f}")
        print("-----------------------------------")
        print("-----------------------------------")
        # Test establecerEstado
        quinta.establecerEstado(8)
        print("------- Estado actualizado -------")
        print(quinta)
        print("-----------------------------------")
        # Test costoAlquiler
        costo_alquiler = quinta.costoAlquiler(250)
        print(f"------- Costo de Alquiler -------")
        print(f"Costo de Alquiler: {costo_alquiler:.2f}")
        print("-----------------------------------")
        # Test precioVenta
        precio_venta = quinta.precioVenta(3000)
        print(f"------- Precio de Venta -------")
        print(f"Precio de Venta: {precio_venta:.2f}")
        print("-----------------------------------")

if __name__ == "__main__":
    TestQuinta.run()