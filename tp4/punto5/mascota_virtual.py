class MascotaVirtual:
    __MAX_VALOR = 100
    __MIN_VALOR = 0

    def __init__(self, nombre:str):
        self.__nombre = nombre
        self.__energia = MascotaVirtual.__MAX_VALOR
        self.__diversion = MascotaVirtual.__MAX_VALOR
        self.__higiene = MascotaVirtual.__MAX_VALOR
        self.__dormido = False
        self.__cantActividadesDesgaste = 0
    #comandos
    def _ajustar_rango(self, valor):
        return max(MascotaVirtual.__MIN_VALOR, min(MascotaVirtual.__MAX_VALOR, valor))

    def _resetear_actividades_desgaste(self):
        self.cantActividadesDesgaste = 0

    def _puede_realizar_actividad(self):
        # Si está dormido, solo puede despertar
        return not self.dormido and self.estaVivo()

    def _actividad_desgaste(self):
        self.cantActividadesDesgaste += 1
        if self.cantActividadesDesgaste > 3:
            self.dormir()
            return False
        return True

    # Comandos
    def comer(self):
        if not self.estaVivo() or self.dormido:
            return
        self.energia = self._ajustar_rango(self.energia + 20)
        self._resetear_actividades_desgaste()

    def beber(self):
        if not self.estaVivo() or self.dormido:
            return
        self.energia = self._ajustar_rango(self.energia + 10)
        self._resetear_actividades_desgaste()

    def dormir(self):
        if not self.estaVivo():
            return
        if not self.dormido:
            self.energia = self._ajustar_rango(self.energia + 20)
            self.diversion = self._ajustar_rango(self.diversion - 10)
            self.dormido = True
            self._resetear_actividades_desgaste()

    def despertar(self):
        if not self.estaVivo():
            return
        self.dormido = False

    def jugar(self):
        if not self._puede_realizar_actividad():
            return
        if not self._actividad_desgaste():
            return
        self.diversion = self._ajustar_rango(self.diversion + 40)
        self.energia = self._ajustar_rango(self.energia - 20)
        self.higiene = self._ajustar_rango(self.higiene - 15)
        if not self.estaVivo():
            self.dormido = False

    def caminar(self):
        if not self._puede_realizar_actividad():
            return
        if not self._actividad_desgaste():
            return
        self.diversion = self._ajustar_rango(self.diversion + 20)
        self.energia = self._ajustar_rango(self.energia - 10)
        self.higiene = self._ajustar_rango(self.higiene - 8)
        if not self.estaVivo():
            self.dormido = False

    def saltar(self):
        if not self._puede_realizar_actividad():
            return
        if not self._actividad_desgaste():
            return
        self.diversion = self._ajustar_rango(self.diversion + 10)
        self.energia = self._ajustar_rango(self.energia - 15)
        self.higiene = self._ajustar_rango(self.higiene - 10)
        if not self.estaVivo():
            self.dormido = False

    def banar(self):
        if not self.estaVivo() or self.dormido:
            return
        self.higiene = self._ajustar_rango(self.higiene + 40)
        self.diversion = self._ajustar_rango(self.diversion - 10)
        self._resetear_actividades_desgaste()
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