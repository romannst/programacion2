from suscripcion import Suscripcion

class SuscripcionGratuita(Suscripcion):
    def __init__(self, nombre:str, email:str, telefono:str, tiempo_sin_publicidad:int, tiempo_reproducido:int):
        super().__init__(nombre, email, telefono)
        if not isinstance(tiempo_sin_publicidad, int) or tiempo_sin_publicidad < 0:
            raise ValueError("El tiempo sin publicidad debe ser un entero no negativo.")
        if not isinstance(tiempo_reproducido, int) or tiempo_reproducido < 0:
            raise ValueError("El tiempo reproducido debe ser un entero no negativo.")
        self.__tiempo_sin_publicidad = tiempo_sin_publicidad
        self.__tiempo_reproducido = tiempo_reproducido
    
    def reproducirMusica(self):
        if self.__tiempo_reproducido >= self.__tiempo_sin_publicidad:
            print("Tiempo sin publicidad agotado.")
            self.interrumpirConPublicidad()
        else:
            print("Reproduciendo música...")
            print(f"Tiempo reproducido: {self.__tiempo_reproducido} minutos.")
    def interrumpirConPublicidad(self):
        print("Reproduciendo anuncio...")
        print("Anuncio reproducido.")