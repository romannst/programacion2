class CuentaBancaria:
    def __init__(self, tasa_interes_anual:float, valor_comision_mensual:float, saldo:float = 0):
        if not isinstance(saldo, (int, float)) or saldo < 0:
            raise ValueError("El saldo debe ser un número no negativo.")
        if not isinstance(tasa_interes_anual, (int, float)) or tasa_interes_anual < 0:
            raise ValueError("La tasa de interés anual debe ser un número no negativo.")
        if not isinstance(valor_comision_mensual, (int, float)) or valor_comision_mensual < 0:
            raise ValueError("El valor de la comisión mensual debe ser un número no negativo.")
        self._saldo = saldo
        self._tasa_interes_anual = tasa_interes_anual
        self._valor_comision_mensual = valor_comision_mensual
        self._cant_extracciones = 0
        self._cant_depositos = 0
    
    def depositar(self, monto:float):
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto a depositar debe ser un número positivo.")
        self._saldo += monto
        self._cant_depositos += 1
        print(f"✅ Depósito de ${monto:,.2f} realizado. Saldo actual: ${self._saldo:,.2f}")
    def extraer(self, monto:float):
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto a extraer debe ser un número positivo.")
        if monto < self._saldo:
            self._saldo -= monto
            self._cant_extracciones += 1
            print(f"✅ Extracción de ${monto:,.2f} realizada. Saldo actual: ${self._saldo:,.2f}")
        else:
            print("Error: No hay saldo suficiente para realizar la extracción.")
    def extractoMensual(self)->str:
        self._saldo -= self._valor_comision_mensual
        self._saldo += self.calcularInteresMensual()
        return f"Saldo: ${self._saldo:,.2f}\nDepósitos: {self._cant_depositos}\nExtracciones: {self._cant_extracciones}\nComisión mensual: ${self._valor_comision_mensual:,.2f}\nInterés mensual: ${self.calcularInteresMensual():,.2f}"
    def calcularInteresMensual(self)->float:
        interes_mensual = (self._tasa_interes_anual / 12) / 100
        return self._saldo * interes_mensual