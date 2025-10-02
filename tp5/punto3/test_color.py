from color import Color

class TestColor:
    @staticmethod
    def run():
        color1 = Color(50, 50, 50)
        color2 = Color()
        print(f"Color1: {color1}")
        print(f"Color2: {color2}")
        color2 = color2.complemento()
        print(f"Complemento de Color2: {color2}")
        if color1.esGris():
            print("Color1 es gris.")
        color2.variar(-100)
        print(f"Color2 después de variar: {color2}")
        if color2.esNegro():
            print("Color2 es negro.")
        color1.variarVerde(120)
        print(f"Color1 después de variar: {color1}")
        if color1.esIgualQue(color2):
            print(f"Color1 es igual que Color2")
        else:
            print(f"Color1 es diferente de Color2")
        color2.variar(50)
        print(f"Color2 después de variar: {color2}")
        color_clon = color2.clonar()
        print(f"Color clon de Color2: (R: {color_clon.obtenerRojo()},G: {color_clon.obtenerVerde()},B: {color_clon.obtenerAzul()})")
if __name__ == "__main__":
    TestColor.run()