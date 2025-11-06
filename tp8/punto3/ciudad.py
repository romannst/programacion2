class Ciudad:
    @classmethod
    def fromDict(cls, data:dict)->"Ciudad":
        if not isinstance(data, dict):
            raise TypeError("El dato debe ser un diccionario")
        return cls(
            nombre=data["nombre"],
            provincia=data["provincia"],
            puntos_turisticos=data["puntos_turisticos"]
        )

    def __init__(self, nombre:str, provincia:str, puntos_turisticos:str):
        if nombre.strip() == "":
            raise ValueError("El nombre de la ciudad no puede estar vacio")
        if provincia.strip() == "":
            raise ValueError("La provincia no puede estar vacia")
        if puntos_turisticos.strip() == "":
            raise ValueError("Los puntos turisticos no pueden estar vacios")
        self.__nombre = nombre
        self.__provincia = provincia
        self.__puntos_turisticos = puntos_turisticos

    def toDict(self)->dict:
        return {
            "nombre": self.__nombre,
            "provincia": self.__provincia,
            "puntos_turisticos": self.__puntos_turisticos
        }
        
    def __str__(self)->str:
        return f"------ Ciudad ------\nNombre: {self.__nombre}\nProvincia: {self.__provincia}\nPuntos Turisticos:\n{self.__puntos_turisticos}"