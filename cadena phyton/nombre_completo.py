nombre_completo = input("Por favor, introduzca su nombre completo")

nombre_minusculas = nombre_completo.lower()
print("Nombre en minúsculas:", nombre_minusculas)

nombre_mayusculas = nombre_completo.upper()
print("Nombre en mayúsculas:", nombre_mayusculas)

palabras = nombre_completo.split()

iniciales = [palabra[0].upper() + palabra[1:] for palabra in palabras]
nombre_iniciales = " ".join(iniciales)
print("Iniciales en mayúsculas:", nombre_iniciales)