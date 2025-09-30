from mascota_virtual import MascotaVirtual

class TestMascotaVirtual:
    @staticmethod
    def run():
        m = MascotaVirtual("Firulais")
        print("Nombre:", m.obtenerNombre())
        print("Energía:", m.obtenerEnergia())
        print("Diversión:", m.obtenerDiversion())
        print("Higiene:", m.obtenerHigiene())
        print("Está dormido:", m.estaDormido())
        print("Está vivo:", m.estaVivo())
        print("Humor inicial:", m.obtenerHumor())
        
        # Realiza acciones
        m.jugar()
        print("\nDespués de jugar:")
        print("Energía:", m.obtenerEnergia())
        print("Diversión:", m.obtenerDiversion())
        print("Higiene:", m.obtenerHigiene())
        print("Humor:", m.obtenerHumor())

        m.comer()
        print("\nDespués de comer:")
        print("Energía:", m.obtenerEnergia())
        print("Humor:", m.obtenerHumor())

        m.banar()
        print("\nDespués de bañarse:")
        print("Higiene:", m.obtenerHigiene())
        print("Humor:", m.obtenerHumor())

        m.dormir()
        print("\nDespués de dormir:")
        print("Está dormido:", m.estaDormido())
        print("Energía:", m.obtenerEnergia())

        m.despertar()
        print("\nDespués de despertar:")
        print("Está dormido:", m.estaDormido())

if __name__ == "__main__":
    TestMascotaVirtual.run()