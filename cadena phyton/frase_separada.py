frase = input("Ingrese una frase: ")
vocal = input("Ingrese la vocal que desea ver en mayuscula: ")

frase_modificada = frase.replace(vocal.lower(), vocal.upper())

print("Frase modificada:", frase_modificada)

