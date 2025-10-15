from cuenta_bancaria import CuentaBancaria

class CuentaAhorros(CuentaBancaria):
    def __init__(self, saldo:float, tasa_interes_anual:float, valor_comision_mensual:float):
        super().__init__(saldo, tasa_interes_anual, valor_comision_mensual)
        self.__cuenta_activa = saldo >= 0
    
    def depositar(self, monto:float):
        if self.__cuenta_activa:
            super().depositar(monto)
        else:
            print("❌ La cuenta está inactiva. No se pueden realizar depósitos.")
    def extraer(self, monto:float):
        if self.__cuenta_activa
            super().extraer(monto)
        else:
            print("❌ La cuenta está inactiva. No se pueden realizar extracciones.")
    def extractoMensual(self)->str:
        if self._cant_extracciones > 4:
            self.comision_mensual += (self._cant_extracciones - 4) * 1000
        resultado = super().extractoMensual()
        self.__cuenta_activa = self._saldo >= 0
        return resultado + f"\nEstado de la cuenta: {'Activa' if self.__cuenta_activa else 'Inactiva'}"