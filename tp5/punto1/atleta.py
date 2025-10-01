class Atleta:
    __max_valor = 100
    __min_valor = 0
    def __init__(self, nombre:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena de caracteres no vacía.")
        self.__nombre = nombre
        self.__energia = Atleta.__max_valor
        self.__destreza = Atleta.__min_valor
        self.__entrenamiento_numero = 0
    #comandos
    def entrenar(self):
        if self.__energia >= 5:
            self.__energia -= 5
            self.__entrenamiento_numero += 1
            if self.__entrenamiento_numero % 5 == 0:
                if self.__destreza < Atleta.__max_valor:
                    self.__destreza += 1
    def descansar(self):
        if self.__energia <= Atleta.__max_valor - 20:
            self.__energia += 20
        elif self.__energia < Atleta.__max_valor:
            self.__energia = Atleta.__max_valor
    #consultas
    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerEnergia(self)->int:
        return self.__energia
    def obtenerDestreza(self)->int:
        return self.__destreza
    def mismaDestrezaQue(self, otro_atleta:"Atleta")->bool:
        if not isinstance(otro_atleta, Atleta):
            raise TypeError("El argumento debe ser una instancia de Atleta.")
        return self.__destreza == otro_atleta.obtenerDestreza()
    def mayorDestrezaQue(self, otro_atleta:"Atleta")->bool:
        if not isinstance(otro_atleta, Atleta):
            raise TypeError("El argumento debe ser una instancia de Atleta.")
        return self.__destreza > otro_atleta.obtenerDestreza()
    def __str__(self) -> str:
        return f"Atleta: {self.__nombre}, Energía: {self.__energia}, Destreza: {self.__destreza}"