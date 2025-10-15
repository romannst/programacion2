from cuenta_bancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, saldo:float, tasa_interes_anual:float, valor_comision_mensual:float, limite_descubierto:float = 0):
        super().__init__(saldo, tasa_interes_anual, valor_comision_mensual)
        self.__limite_descubierto = limite_descubierto
        self.__penalizaciones = 0
    
    def depositar(self, monto: float):
        if self._saldo < 0:
            penalizacion = self._saldo * 0.02  # 2% de penalización
            monto -= penalizacion
            self.__penalizaciones += penalizacion
            print(f"⚠️ Se aplicó una penalización de ${-penalizacion:,.2f} por saldo negativo.")
        super().depositar(monto)
    def extraer(self, monto: float):
        if self._saldo + self.__limite_descubierto >= monto:
            super().extraer(monto)
        else:
            print(f"❌ Límite de descubierto excedido. Disponible: ${self._saldo + self.__limite_descubierto:,.2f}")
    def extractoMensual(self) -> str:
        return super().extractoMensual() + f"\nPenalizaciones: ${self.__penalizaciones:,.2f}"
