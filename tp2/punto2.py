def esBisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    return False
año = input("Ingrese un año: ")
mes = input("Ingrese un mes (1-12): ")
dia = input("Ingrese un día: ")
try:
    año = int(año)
    mes = int(mes)
    dia = int(dia)
except:
    print("Entrada inválida. Por favor, ingrese números enteros.")
    exit()
if esBisiesto(año):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")

def fechaValida(año, mes, dia):
    if año < 0:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if mes == 2:
        if esBisiesto(año):
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False
    if mes in [4, 6, 9, 11]:
        if dia > 30:
            return False
    return True
if fechaValida(año, mes, dia):
    print(f"La fecha {dia:02}/{mes:02}/{año} es válida")
else:
    print(f"La fecha {dia:02}/{mes:02}/{año} no es válida")

# 1. Enero: 31 días
# 2. Febrero: 28 días (29 en año bisiesto)
# 3. Marzo: 31 días
# 4. Abril: 30 días
# 5. Mayo: 31 días
# 6. Junio: 30 días
# 7. Julio: 31 días
# 8. Agosto: 31 días
# 9. Septiembre: 30 días
# 10. Octubre: 31 días
# 11. Noviembre: 30 días
# 12. Diciembre: 31 días