productos_str = input("Introduce los productos de la cesta de compra separados por comas: ")

productos = productos_str.split(',')

for producto in productos:
    print(producto.strip()) 