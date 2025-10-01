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
        self.__cantActividadesDesgaste = 0

    def _puede_realizar_actividad(self):
        # Si está dormido, solo puede despertar
        return not self.__dormido and self.estaVivo()

    def _actividad_desgaste(self):
        self.cantActividadesDesgaste += 1
        if self.__cantActividadesDesgaste > 3:
            self.dormir()
            return False
        return True

    # Comandos
    def comer(self):
        if not self.estaVivo() or self.__dormido:
            return
        self.__energia = self._ajustar_rango(self.__energia + 20)
        self._resetear_actividades_desgaste()

    def beber(self):
        if not self.estaVivo() or self.__dormido:
            return
        self.__energia = self._ajustar_rango(self.__energia + 10)
        self._resetear_actividades_desgaste()

    def dormir(self):
        if not self.estaVivo():
            return
        if not self.__dormido:
            self.__energia = self._ajustar_rango(self.__energia + 20)
            self.__diversion = self._ajustar_rango(self.__diversion - 10)
            self.__dormido = True
            self._resetear_actividades_desgaste()

    def despertar(self):
        if not self.estaVivo():
            return
        self.__dormido = False

    def jugar(self):
        if not self._puede_realizar_actividad():
            return
        if not self._actividad_desgaste():
            return
        self.__diversion = self._ajustar_rango(self.__diversion + 40)
        self.__energia = self._ajustar_rango(self.__energia - 20)
        self.__higiene = self._ajustar_rango(self.__higiene - 15)
        if not self.estaVivo():
            self.__dormido = False

    def caminar(self):
        if not self._puede_realizar_actividad():
            return
        if not self._actividad_desgaste():
            return
        self.__diversion = self._ajustar_rango(self.__diversion + 20)
        self.__energia = self._ajustar_rango(self.__energia - 10)
        self.__higiene = self._ajustar_rango(self.__higiene - 8)
        if not self.estaVivo():
            self.__dormido = False

    def saltar(self):
        if not self._puede_realizar_actividad():
            return
        if not self._actividad_desgaste():
            return
        self.__diversion = self._ajustar_rango(self.__diversion + 10)
        self.__energia = self._ajustar_rango(self.__energia - 15)
        self.__higiene = self._ajustar_rango(self.__higiene - 10)
        if not self.estaVivo():
            self.__dormido = False

    def banar(self):
        if not self.estaVivo() or self.__dormido:
            return
        self.__higiene = self._ajustar_rango(self.__higiene + 40)
        self.__diversion = self._ajustar_rango(self.__diversion - 10)
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