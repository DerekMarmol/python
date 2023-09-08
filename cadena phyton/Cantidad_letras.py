nombre_usuario = input("Introduzca su nombre")
cantidad_letras = 0

for letra in nombre_usuario:
    if letra.isalpha():
        cantidad_letras += 1

print("Tu nombre es:",nombre_usuario, "y tiene la cantidad de:", cantidad_letras, "letras")
