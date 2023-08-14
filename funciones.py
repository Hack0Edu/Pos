
import json
import os

def load_json(ruta):
    with open(ruta) as content_file:
        data = json.load(content_file)
    return data

def buscar_producto(datos, termino):
    resultados = []
    for item in datos:
        if item["nombre"].lower() == termino.lower():
            resultados.append(item)
    if resultados:
        for resultado in resultados:
            print("Información del producto:")
            print(f"""
Código: {resultado["codigo"]}
Nombre: {resultado["nombre"]}
Stock Máximo: {resultado["StockMaximo"]}
Stock Mínimo: {resultado["StockMinimo"]}
Estado: {resultado["Estado"]}
Proveedor: {resultado["Proveedor"]}""")
    else:
        print("No se encontraron productos con el término de búsqueda especificado.")

def mostrar_inventario(datos):
    for item in datos:
        print(f"""
Código: {item["codigo"]}
Nombre: {item["nombre"]}
Stock Máximo: {item["StockMaximo"]}
Stock Mínimo: {item["StockMinimo"]}
Estado: {item["Estado"]}
Proveedor: {item["Proveedor"]}""")
        
def menu():
    print("""
          Bienvenido a Ferreterías El Perico
          ¿Qué desea revisar?
          -> Inventario
          -> Ventas 
          -> Compras            
          """)
    eleccion = input("Ingrese su elección: ")
    if eleccion.lower() == "inventario":
        menu_Inventario()
    elif eleccion.lower() == "compras":
        menu_Compras()
    elif eleccion.lower() == "ventas":
        menu_Ventas()
    else:
        os.system("cls")
        input("opcion invalidad regresando al menu...")
        os.system("cls")
        menu()
def menu_Inventario():
    ruta = 'Base_Inventario.json'
    datos = load_json(ruta)
    os.system("cls")
    menu_inventario = input(""" Hola ¿que es lo que deseas hacer?
1.- Buscar por termino
2.- Ver todo el inventario """)
    if menu_inventario == "1":
        os.system("cls")
        termino_busqueda = input("Ingrese el nombre del producto a buscar: ")
        buscar_producto(datos, termino_busqueda)
    elif menu_inventario == "2":
        os.system("cls")
        mostrar_inventario(datos)
    else:
        os.system("cls")
        input("opcion invalidad regresando al menu...")
        os.system("cls")
        menu_Inventario()
def menu_Compras():
    with open("Base_Compras") as archivo:
        datos = json.load(archivo)
    
    termino_busqueda = input("Ingrese el término por el cual desea buscar (numero_documento, fecha_compra, valor_compra, cantidad_comprada): ")

    if termino_busqueda == "numero_documento":
        numero_documento = input("Ingrese el número de documento de compra: ")
        productos_encontrados = [producto for producto in datos if producto["numero_documento_compra"] == numero_documento]
        return productos_encontrados

    elif termino_busqueda == "fecha_compra":
        fecha_compra = input("Ingrese la fecha de compra: ")
        productos_encontrados = [producto for producto in datos if producto["fecha_compra"] == fecha_compra]
        return productos_encontrados

    elif termino_busqueda == "valor_compra":
        valor_compra = float(input("Ingrese el valor de compra: "))
        productos_encontrados = [producto for producto in datos if producto["valor_compra"] == valor_compra]
        return productos_encontrados

    elif termino_busqueda == "cantidad_comprada":
        cantidad_comprada = int(input("Ingrese la cantidad comprada: "))
        productos_encontrados = [producto for producto in datos if producto["cantidad_comprada"] == cantidad_comprada]
        return productos_encontrados

    else:
        print("Término de búsqueda inválido.")
    
    return []

def menu_Ventas():
    print("ventas")