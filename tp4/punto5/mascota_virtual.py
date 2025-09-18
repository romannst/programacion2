class MascotaVirtual:
    __MAX_VALOR = 100
    __MIN_VALOR = 0

    def __init__(self, nombre:str, energia:int=__MAX_VALOR, diversion:int=__MAX_VALOR, higiene:int=__MAX_VALOR, dormido:bool=False, cantActividadesDesgaste:int=3):
        self.__nombre = nombre
        self.__energia = energia
        self.__diversion = diversion
        self.__higiene = higiene
        self.__dormido = dormido
        self.__cantActividadesDesgaste = cantActividadesDesgaste
    #comandos

    #consultas
    def obtenerNombre(self)-> str:
        return self.__nombre
    def obtenerEnergia(self)-> int:
        return self.__energia
    def obtenerDiversion(self)-> int:
        return self.__diversion
    def obtenerHigiene(self)-> int:
        return self.__higiene
    def estaDormido(self)-> bool:
        return self.__dormido
    def obtenerHumor(self)-> str:
        if self.__energia > 70 and self.__diversion > 70 and self.__higiene > 70:
            return "Humor Feliz"
        elif self.__energia >50 and self.__energia <70 and self.__diversion >50 and self.__diversion <70:
            return "Humor Alegre"
        elif self.__energia >50 and self.__energia <70 and self.__higiene >50 and self.__higiene <70:
            return "Humor Alegre"
        elif self.__diversion >50 and self.__diversion <70 and self.__higiene >50 and self.__higiene <70:
            return "Humor Alegre"
        elif self.__energia >30 and self.__energia <50 and self.__diversion >30 and self.__diversion <50:
            return "Humor Neutral"
        elif self.__energia >30 and self.__energia <50 and self.__higiene >30 and self.__higiene <50:
            return "Humor Neutral"
        elif self.__diversion >30 and self.__diversion <50 and self.__higiene >30 and self.__higiene <50:
            return "Humor Neutral"
        elif self.__energia >10 and self.__energia <30 and self.__diversion >10 and self.__diversion <30:
            return "Humor Triste"
        elif self.__energia >10 and self.__energia <30 and self.__higiene >10 and self.__higiene <30:
            return "Humor Triste"
        elif self.__diversion >10 and self.__diversion <30 and self.__higiene >10 and self.__higiene <30:
            return "Humor Triste"
        else:
            return "Humor Muy Triste"
    def estaVivo(self)-> bool:
        return self.__energia > 0