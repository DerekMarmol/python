fecha_nacimiento_str = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

dia, mes, anio = fecha_nacimiento_str.split('/')

if len(dia) == 1:
    dia = '0' + dia
if len(mes) == 1:
    mes = '0' + mes

print(f"Tu fecha de nacimiento es: {dia}/{mes}/{anio}")