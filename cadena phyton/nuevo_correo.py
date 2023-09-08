correo = input("Ingrese su correo electronico: ")

correo_partes = correo.split("@")

parte1 = correo_partes[0]

nuevo_correo = parte1 + "@ceu.es"

print("Su nuevo correo es:",nuevo_correo)