precio_str = input("introduce el precio de un producto y sus decimales: ")

precio = float(precio_str)

euros = int(precio)

centimos = int((precio - euros) * 100)

print("el precio en euros es de",euros, "y sus centimos son de",centimos)