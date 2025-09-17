from vinoteca import Vinoteca

class TestVinoteca:
    @staticmethod
    def run():
        vinoteca1 = Vinoteca()
        vinoteca2 = Vinoteca()
        print("Vinoteca 1")
        print("Stock inicial:")
        print(f"Jugos: {vinoteca1.obtenerCantidadJugos()}")
        print(f"Vinos blancos: {vinoteca1.obtenerCantidadVinosBlancos()}")
        print(f"Tintos jóvenes: {vinoteca1.obtenerCantidadVinosTintosJovenes()}")
        print(f"Tintos añejados: {vinoteca1.obtenerCantidadVinosTintosAnejados()}")
        print("Vinoteca 2")
        print("Stock inicial:")
        print(f"Jugos: {vinoteca2.obtenerCantidadJugos()}")
        print(f"Vinos blancos: {vinoteca2.obtenerCantidadVinosBlancos()}")
        print(f"Tintos jóvenes: {vinoteca2.obtenerCantidadVinosTintosJovenes()}")
        print(f"Tintos añejados: {vinoteca2.obtenerCantidadVinosTintosAnejados()}")

        error = True
        while error:
            try:
                vinoteca1.venderJugos(int(input("Ingrese la cantidad de jugos a vender para Vinoteca 1: ")))
                vinoteca2.venderJugos(int(input("Ingrese la cantidad de jugos a vender para Vinoteca 2: ")))
                error = False
            except ValueError:
                print("Error: Ingrese un número válido.")
        print(f"Vinoteca 1 - Cantidad Jugos: {vinoteca1.obtenerCantidadJugos()}")
        print(f"Vinoteca 2 - Cantidad Jugos: {vinoteca2.obtenerCantidadJugos()}")
        vinoteca1.reponerJugos()
        vinoteca2.reponerJugos()
        print(f"Vinoteca 1 - Cantidad Jugos: {vinoteca1.obtenerCantidadJugos()}")
        print(f"Vinoteca 2 - Cantidad Jugos: {vinoteca2.obtenerCantidadJugos()}")
        error = True
        while error:
            try:
                vinoteca1.venderVinosBlancos(int(input("Ingrese la cantidad de vinos blancos a vender para Vinoteca 1: ")))
                vinoteca2.venderVinosBlancos(int(input("Ingrese la cantidad de vinos blancos a vender para Vinoteca 2: ")))
                error = False
            except ValueError:
                print("Error: Ingrese un número válido.")
        print(f"Vinoteca 1 - Cantidad Vinos Blancos: {vinoteca1.obtenerCantidadVinosBlancos()}")
        print(f"Vinoteca 2 - Cantidad Vinos Blancos: {vinoteca2.obtenerCantidadVinosBlancos()}")
        vinoteca1.reponerVinosBlancos()
        vinoteca2.reponerVinosBlancos()
        print(f"Vinoteca 1 - Cantidad Vinos Blancos: {vinoteca1.obtenerCantidadVinosBlancos()}")
        print(f"Vinoteca 2 - Cantidad Vinos Blancos: {vinoteca2.obtenerCantidadVinosBlancos()}")
        error = True
        while error:
            try:
                vinoteca1.venderVinosTintosJovenes(int(input("Ingrese la cantidad de vinos tintos jóvenes a vender para Vinoteca 1: ")))
                vinoteca2.venderVinosTintosJovenes(int(input("Ingrese la cantidad de vinos tintos jóvenes a vender para Vinoteca 2: ")))
                error = False
            except ValueError:
                print("Error: Ingrese un número válido.")
        print(f"Vinoteca 1 - Cantidad Vinos Tintos Jóvenes: {vinoteca1.obtenerCantidadVinosTintosJovenes()}")
        print(f"Vinoteca 2 - Cantidad Vinos Tintos Jóvenes: {vinoteca2.obtenerCantidadVinosTintosJovenes()}")
        vinoteca1.reponerVinosTintoJoven()
        vinoteca2.reponerVinosTintoJoven()
        print(f"Vinoteca 1 - Cantidad Vinos Tintos Jóvenes: {vinoteca1.obtenerCantidadVinosTintosJovenes()}")
        print(f"Vinoteca 2 - Cantidad Vinos Tintos Jóvenes: {vinoteca2.obtenerCantidadVinosTintosJovenes()}")
        error = True
        while error:
            try:
                vinoteca1.venderVinosTintosAnejados(int(input("Ingrese la cantidad de vinos tintos añejados a vender para Vinoteca 1: ")))
                vinoteca2.venderVinosTintosAnejados(int(input("Ingrese la cantidad de vinos tintos añejados a vender para Vinoteca 2: ")))
                error = False
            except ValueError:
                print("Error: Ingrese un número válido.")
        print(f"Vinoteca 1 - Cantidad Vinos Tintos Añejados: {vinoteca1.obtenerCantidadVinosTintosAnejados()}")
        print(f"Vinoteca 2 - Cantidad Vinos Tintos Añejados: {vinoteca2.obtenerCantidadVinosTintosAnejados()}")
        vinoteca1.reponerVinosTintoAnejado()
        vinoteca2.reponerVinosTintoAnejado()
        print(f"Vinoteca 1 - Cantidad Vinos Tintos Añejados: {vinoteca1.obtenerCantidadVinosTintosAnejados()}")
        print(f"Vinoteca 2 - Cantidad Vinos Tintos Añejados: {vinoteca2.obtenerCantidadVinosTintosAnejados()}")

if __name__ == "__main__":
    TestVinoteca.run()