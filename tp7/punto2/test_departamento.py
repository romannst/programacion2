from departamento import Departamento
from propietario import Propietario

class TestDepartamento:
    @staticmethod
    def run():
        #testear servicios de la clase Departamento
        propietario = Propietario(12345678, "Juan Perez", 987654321)
        departamento = Departamento(1, "Av. Siempre Viva 742", propietario, 50, 8, 5000, True)
        print("------- Departamento creado -------")
        print(departamento)
        # Test costoAlquiler
        costo_alquiler = departamento.costoAlquiler(100)
        print(f"------- Costo de Alquiler -------")
        print(f"Costo de Alquiler: {costo_alquiler:.2f}")
        print("-----------------------------------")
        # Test precioVenta
        precio_venta = departamento.precioVenta(2000)
        print(f"------- Precio de Venta -------")
        print(f"Precio de Venta: {precio_venta:.2f}")
        print("-----------------------------------")
        print("-----------------------------------")
        # Test establecerEstado
        departamento.establecerEstado(9)
        print("------- Estado actualizado -------")
        print(departamento)
        print("-----------------------------------")
        # Test costoAlquiler
        costo_alquiler = departamento.costoAlquiler(100)
        print(f"------- Costo de Alquiler -------")
        print(f"Costo de Alquiler: {costo_alquiler:.2f}")
        print("-----------------------------------")
        # Test precioVenta
        precio_venta = departamento.precioVenta(2000)
        print(f"------- Precio de Venta -------")
        print(f"Precio de Venta: {precio_venta:.2f}")
        print("-----------------------------------")

if __name__ == "__main__":
    TestDepartamento.run()