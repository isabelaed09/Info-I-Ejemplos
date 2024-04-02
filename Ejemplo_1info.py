#Se definió diccionarios para los artículos disponibles
camisetas = {
    1: ["polo", "blanca", 15],
    2: ["polo", "azul", 15],
    3: ["polo", "roja", 15],
    4: ["polo", "amarilla", 15],
    5: ["cuello redondo", "gris", 12],
    6: ["cuello redondo", "negro", 12],
    7: ["cuello redondo", "verde", 12]}

jeans = {
    1: ["Azul", 20],
    2: ["verde", 20],
    3: ["cafe", 20],
    4: ["negro", 20],
    5: ["gris", 20]
}

zapatos = {
    1: ["botas", "cafe", 25],
    2: ["tenis", "azul", 20],
    3: ["botas", "negro", 25],
    4: ["tenis", "blanco", 20]
}
#Se creó una lista vacía para almacenar datos 
compras = []
#Se definió la función para capturar los datos del comprador 
def capturar_datos_comprador():
    while True:
        nombre_apellido = input("Ingrese su nombre y apellido: ")
        identificacion = input("Ingrese su número de identificación (solo números): ")
        telefono = input("Ingrese su número de teléfono (solo números): ")
        try:
            identificacion = int(identificacion)
            telefono = int(telefono)
            break
        except ValueError:
            print("Por favor, ingrese solo números para el número de identificación y teléfono.")
    direccion = input("Ingrese su dirección: ")
    return nombre_apellido, identificacion, direccion, telefono

#Se definió una función para seleccionar el tipo de artículo
def seleccionar_articulo(diccionario):
    while True:
        print("Artículos disponibles:")
    
        for clave, valor in diccionario.items():
            if len(valor) == 3:
                print(f"{clave}: {valor[0]} - {valor[1]} - ${valor[2]}")
            else: 
                print(f"{clave}: {valor[0]} - {valor[1]}")
        try:
            seleccion = int(input("Seleccione el número del artículo que desea comprar: "))
            if seleccion in diccionario:
                break
            else:
                print("Número de artículo no válido.")
        except ValueError:
            print("Por favor, ingrese solo números.")
    return diccionario[seleccion]

#Se definió una función para calcular el total de la compra
def calcular_total(compra):
    
    precios = []
    for item in compra:
        if len(item) == 3:
            precios.append(item[2])
        else: 
           precios.append(item[1])
    
    total = sum(precios)
    

    return total


def mostrar_factura(compra, datos_comprador):
    print("\nFactura:")
    print("Datos del comprador:")
    print("Nombre:", datos_comprador[0])
    print("Identificación:", datos_comprador[1])
    print("Dirección:", datos_comprador[2])
    print("Teléfono:", datos_comprador[3])
    print("Artículos comprados:")
    for item in compra:

        if len(item) == 3:
            print(f"{item[0]} - {item[1]} - ${item[2]}")
        else: 
            print(f"{item[0]} - {item[1]}")
    
    print("Total de la compra:", calcular_total(compra))


def main():
    while True:
        
        datos_comprador = capturar_datos_comprador()

        
        for i in range(3):
            
            try:
                tipo_articulo = (int(input("\nSeleccione el tipo de artículo \n1.camisetas\n2.jeans\n3.zapatos: ")))
                if tipo_articulo == 1:
                    articulo = seleccionar_articulo(camisetas)
                elif tipo_articulo == 2:
                    articulo = seleccionar_articulo(jeans)
                elif tipo_articulo == 3:
                    articulo = seleccionar_articulo(zapatos)
                else:
                    print("Tipo de artículo no válido.")
                    continue
            except ValueError:
                print("Por favor, ingrese solo números.")
                continue
            compras.append(articulo)

        
        mostrar_factura(compras, datos_comprador)

        
        otra_compra = input("\n¿Desea hacer otra compra? (sí/no): ")
        if otra_compra.lower() != "sí":
            break
        else:
            compras.clear()

if __name__ == "__main__":
    main()
