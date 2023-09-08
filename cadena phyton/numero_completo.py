numero_completo = input("Ingrese su número con las siguientes caracteristicas: prefijo-numero-extensión, ejemplo: +34-913724710-56: ")

numero_divido = numero_completo.split("-")

numero = numero_divido[1]

print("El número ingresado sin el prefijo y la extensión es: ",numero)