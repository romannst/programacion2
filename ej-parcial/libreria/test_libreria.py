from tienda import Tienda
from libroFisico import LibroFisico
from libroDigital import LibroDigital
from platLibro import PlatLibro
from autor import Autor
from venta import Venta

class TestLibreria:
    @staticmethod
    def run():
        tienda = Tienda("Librería Central", "Calle Falsa 123")
        print(tienda)
        autor1 = Autor(1, "F. Scott Fitzgerald", "Autor estadounidense conocido por sus novelas y cuentos.")
        autor2 = Autor(2, "George Orwell", "Autor británico conocido por sus novelas distópicas.")
        libro1 = LibroFisico(123456789, "El Gran Gatsby", autor1, "Ficción", "1925-04-10", "Una novela sobre el sueño americano.", 180, 5, 10.99)
        libro2 = LibroDigital(987654321, "1984", autor2, "Distopía", "1949-06-08", "Una novela sobre un futuro totalitario.", 328, PlatLibro.KINDLE, 1.5, 6.99)
        print(libro1)
        print(libro2)
        print("-"*40)
        libro1.establecerDescr("Una novela clásica sobre la decadencia y el exceso en la década de 1920.")
        libro2.establecerDescr("Una novela que explora los peligros del totalitarismo.")
        print(libro1.obtenerDescr())
        print(libro2.obtenerDescr())
        print("-"*40)
        tienda.actualizarStock(libro1, 3)
        tienda.actualizarStock(libro2, 5)
        print(tienda)
        print("-"*40)
        venta1 = Venta([libro1, libro2], "2023-10-01", 17.98)
        tienda.venta(venta1)
        print(tienda)
        print(venta1)
        print("-"*40)
        print(venta1.mostrarProductos())

if __name__ == "__main__":
    TestLibreria.run()