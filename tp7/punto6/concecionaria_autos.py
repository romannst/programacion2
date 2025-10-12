from abc import ABC, abstractmethod
from enum import Enum

# Enum para el tipo de combustible
class TipoCombustible(Enum):
    NAFTA = "Nafta"
    DIESEL = "Diésel"
    ELECTRICO = "Eléctrico"

# Clase abstracta Vehiculo
class Vehiculo(ABC):
    def __init__(self, marca, modelo, patente, color, año, precio, kilometraje, tipo_combustible):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.color = color
        self.año = año
        self.precio = precio
        self.kilometraje = kilometraje
        self.tipo_combustible = tipo_combustible
    
    # Método abstracto para calcular el precio del vehículo
    @abstractmethod
    def calcularPrecio(self):
        pass


# Clase Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, patente, color, año, precio, kilometraje, tipo_combustible, puertas, aire_acondicionado):
        super().__init__(marca, modelo, patente, color, año, precio, kilometraje, tipo_combustible)
        self.puertas = puertas
        self.aire_acondicionado = aire_acondicionado

    def __str__(self):
        aire = "Sí" if self.aire_acondicionado else "No"
        return f"{self.marca} {self.modelo} ({self.año}), {self.color}, {self.tipo_combustible.value}, ${self.precio}, {self.kilometraje} km - {self.puertas} puertas, Aire Acondicionado: {aire}"
    # Implementación del método calcularPrecio para Auto
    def calcularPrecio(self):
        # Precio base ajustado por año, kilometraje, aire acondicionado y cantidad de puertas
        precio_base = self.precio
        if self.año < 2015:
            precio_base *= 0.9  # Descuento del 10% si el año es anterior a 2015
        if self.kilometraje > 100000:
            precio_base *= 0.85  # Descuento del 15% si el kilometraje es mayor a 100,000 km
        if self.aire_acondicionado:
            precio_base *= 1.05  # Aumento del 5% si tiene aire acondicionado
        # Ajuste por cantidad de puertas
        if self.puertas > 4:
            precio_base *= 1.05  # Aumento del 5% si tiene más de 4 puertas (modelo más grande)
        elif self.puertas == 2:
            precio_base *= 0.95  # Descuento del 5% si tiene 2 puertas (modelo deportivo)
        return precio_base


# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, patente, color, año, precio, kilometraje, tipo_combustible, ancho_manillar, cilindrada):
        super().__init__(marca, modelo, patente, color, año, precio, kilometraje, tipo_combustible)
        self.ancho_manillar = ancho_manillar
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año}), {self.color}, {self.tipo_combustible.value}, ${self.precio}, {self.kilometraje} km - Ancho Manillar: {self.ancho_manillar} cm, Cilindrada: {self.cilindrada} cc"
    # Implementación del método calcularPrecio para Moto
    def calcularPrecio(self):
        # Precio base ajustado por cilindrada, kilometraje y tipo de combustible
        precio_base = self.precio
        if self.cilindrada > 500:
            precio_base *= 1.1  # Aumento del 10% si la cilindrada es mayor a 500cc
        if self.kilometraje > 50000:
            precio_base *= 0.85  # Descuento del 15% si el kilometraje es mayor a 50,000 km
        if self.tipo_combustible == TipoCombustible.ELECTRICO:
            precio_base *= 1.2  # Aumento del 20% si es eléctrico
        return precio_base