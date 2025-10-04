class Especie:
    def __init__(self, nombre: str):
        if not isinstance(nombre, str) or nombre.strip() =="":
            raise TypeError("El nombre debe ser un texto válido")
        self.__nombre = nombre
        self.__ritmo = 0.0
        self.__hembras = 0
        self.__machos = 0

    def establecerHembras(self, cantidad:int):
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un numero entero positivo")
        if cantidad > 0:
            self.__hembras = cantidad

    def establecerMachos(self, cantidad:int):
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un numero entero positivo")
        if cantidad > 0:
            self.__machos = cantidad

    def establecerRitmo(self, valor:float):
        if not isinstance(valor, (int, float)):
            raise TypeError("El valor del ritmo de crecimiento debe ser un numero válido")
        self.__ritmo = valor
    
    def actualizarHembras(self, cantidad:int):
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un numero entero")
        if (self.__hembras + cantidad) >= 0:
            self.__hembras += cantidad

    def actualizarMachos(self, cantidad:int):
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un numero entero")
        if (self.__machos + cantidad) >= 0:
            self.__machos += cantidad
        
    def actualizarRitmo(self, valor:float):
        if not isinstance(valor, (int, float)):
            raise TypeError("El valor de variación del ritmo de crecimiento debe ser un numero válido")
        self.__ritmo += valor

    #consultas
    def poblacionActual(self)->int:
        return self.__hembras + self.__machos
    
    def poblacionEstimada(self, anios:int)->int:
        """Estima la cantidad de poblacion dentro de una cantidad de años recibida por parametro"""
        if not isinstance(anios, int) or anios < 0:
            raise TypeError("El valor de años debe ser un numero entero positivo")
        poblacionActual = self.poblacionActual()
        #para cada año de 'anios' poblacionActual = poblacionActual * ritmo
        for i in range(anios): #[0..anios-1]        
            if self.__ritmo < 0:
                poblacionActual = poblacionActual - (poblacionActual * (self.__ritmo * -1))
            else:
                poblacionActual = poblacionActual + poblacionActual * self.__ritmo
            # ritmo > 0 : 10 + 10*0.2
            # ritmo = 0: no pasa nada 10 + 10*0
            # ritmo < 0: -10 + -10*(-2)

        # valores posibles ej: 0 | -1254.2366 | 12356.35432
        if poblacionActual < 0:
            poblacionActual = 0

        return int(poblacionActual)
    
    def poblacionEstimadaConWhile(self, anios:int)->int:
        """Estima la cantidad de poblacion dentro de una cantidad de años recibida por parametro"""
        if not isinstance(anios, int) or anios < 0:
            raise TypeError("El valor de años debe ser un numero entero positivo")
        poblacionActual = self.poblacionActual()
        i = 0
        while poblacionActual > 0 and i < anios:
            if self.__ritmo < 0:
                poblacionActual = poblacionActual - (poblacionActual * (self.__ritmo * -1))
            else:
                poblacionActual = poblacionActual + poblacionActual * self.__ritmo
        
        if poblacionActual < 0:
            poblacionActual = 0

        return int(poblacionActual)
    
    def aniosParaPoblacion(self, poblacionObjetivo:int)-> int:
        """Devuelve la cantidad de años necesaria para llegar a la poblacion objetivo.
        Si no se puede llegar a la poblacion objetivo devuelve -1."""
        if not isinstance(poblacionObjetivo, int) or poblacionObjetivo<0:
            raise TypeError("La poblacion objetivo debe ser un numero entero mayor o igual a cero")
        # Problema: si poblacion actual < a poblacion objetivo y ritmo negativo
        # Problema: si poblacion actual > a poblacion objetivo y ritmo positivo
        poblacionActual = self.poblacionActual()
        if (self.__ritmo > 0 and poblacionActual > poblacionObjetivo) or (self.__ritmo < 0 and poblacionActual < poblacionObjetivo) or self.__ritmo == 0:
            anios = -1
        else:
            anios = 0

            if self.__ritmo > 0:
                # ok                
                while poblacionActual < poblacionObjetivo:
                    anios += 1
                    poblacionActual = poblacionActual + poblacionActual * self.__ritmo

            else:
                #ok                
                while poblacionActual > poblacionObjetivo:
                    anios += 1
                    poblacionActual = int(poblacionActual - (poblacionActual * (self.__ritmo * -1)))
        return anios
    
    def riesgo(self)-> str:
        if self.__ritmo > 0:
            return "verde"
        elif self.__ritmo < 0:
            return "rojo"
        else:
            return "amarillo"
        
    def masHembras(self)->bool:
        return self.__hembras > self.__machos
    
    def obtenerRitmo(self)-> float:
        return self.__ritmo

    def mayorRitmo(self, otraEspecie: "Especie")-> "Especie":
        """retorna la referencia al objeto con mayor ritmo de crecimiento"""
        if not isinstance(otraEspecie, Especie):
            raise TypeError("La especie debe ser un objeto de clase Especie")
        if self.__ritmo > otraEspecie.obtenerRitmo():
            return self
        else:
            return otraEspecie
        
    def clonar(self)->"Especie":
        clon = Especie(self.__nombre)
        clon.establecerHembras(self.__hembras)
        clon.establecerMachos(self.__machos)
        clon.establecerRitmo(self.__ritmo)
        return clon
    
    def __str__(self):
        return f"\t- Nombre: {self.__nombre}\n\t- Cant. hembras: {self.__hembras}\n\t- Cant. machos: {self.__machos}\n\t- Ritmo: {self.__ritmo}\n\t- Riesgo: {self.riesgo()}"