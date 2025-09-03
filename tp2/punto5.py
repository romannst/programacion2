alumnos_notas = dict()
cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))
for i in range(cant_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
    alumnos_notas[nombre] = nota

# lista_resultados = ["Aprobado" if nota >= 40 else "Desaprobado" for nota in alumnos_notas.values()]
# i_nota = 0
# for alumno, nota in alumnos_notas.items():
#     print(f"{alumno}", end="  ")
#     print(f"{nota:.0f}", end="  ")
#     print(f"{lista_resultados[i_nota]}", end="\n")
#     i_nota += 1

print("\nALUMNOS\t\tPARCIAL\tRESULTADO")
for alumno, nota in alumnos_notas.items():
    resultado = "Aprobado" if nota >= 40 else "Desaprobado"
    print(f"{alumno:15}\t{int(nota):7}\t{resultado}")