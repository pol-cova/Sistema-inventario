from datetime import datetime
from inventario import Product, Inventario
import os
import time

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    print("Bienvenido a Lagunitas")
    print("1) Registrar producto")
    print("2) Listar productos")
    print("3) Buscar producto")
    print("4) Modificar producto")
    print("5) Eliminar producto")
    print("6) Salir")

def registrar_producto(inventario):
    try:
        print("\n=== Registrar Producto ===")
        while True:
            id_producto = input("ID del producto: ")
            # Checar id si existe o no 
            try:
                inventario.get_product(id_producto)
                print("\nError: Este ID ya está registrado. Por favor, use otro ID.")
                continue
            except ValueError:
                break

        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        costo = float(input("Costo unitario: "))
        cantidad = int(input("Cantidad: "))
        comentarios = input("Comentarios: ")
        fecha = datetime.now().strftime("%Y-%m-%d")

        producto = Product(nombre, categoria, costo, cantidad, fecha, comentarios)
        inventario.add_product(id_producto, producto)
        print("\n¡Producto registrado exitosamente!")
    except ValueError as e:
        print(f"\nError: {e}")

def listar_productos(inventario):
    while True:
        print("\n=== Listar Productos ===")
        print("1) Por categoría")
        print("2) Por precio")
        print("3) Volver al menú principal")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1:
                categoria = input("\nIngrese la categoría: ")
                productos = inventario.get_all_products_by_category(categoria)
                if not productos:
                    print("\nNo hay productos en esta categoría")
                else:
                    print("\nProductos encontrados:")
                    for producto in productos:
                        print(f"\n{producto}")
            elif opcion == 2:
                productos = inventario.get_all_products_by_price()
                if not productos:
                    print("\nNo hay productos registrados")
                else:
                    print("\nProductos ordenados por precio:")
                    for producto in productos:
                        print(f"\n{producto}")
            elif opcion == 3:
                break
            else:
                print("\nOpción no válida")
        except ValueError:
            print("\nPor favor, ingrese un número válido")

def buscar_producto(inventario):
    try:
        print("\n=== Buscar Producto ===")
        id_producto = input("Ingrese el ID del producto: ")
        producto = inventario.get_product(id_producto)
        print("\nProducto encontrado:")
        print(producto)
    except ValueError as e:
        print(f"\nError: {e}")

def modificar_producto(inventario):
    try:
        print("\n=== Modificar Producto ===")
        id_producto = input("Ingrese el ID del producto: ")
        producto = inventario.get_product(id_producto)
        print("\nProducto actual:")
        print(producto)
        
        print("\nIngrese los nuevos datos (presione Enter para mantener el valor actual):")
        nombre = input("Nuevo nombre: ")
        categoria = input("Nueva categoría: ")
        costo = input("Nuevo costo unitario: ")
        cantidad = input("Nueva cantidad: ")

        inventario.update_product(
            id_producto,
            nombre if nombre else None,
            categoria if categoria else None,
            float(costo) if costo else None,
            int(cantidad) if cantidad else None
        )
        print("\n¡Producto actualizado exitosamente!")
    except ValueError as e:
        print(f"\nError: {e}")

def eliminar_producto(inventario):
    try:
        print("\n=== Eliminar Producto ===")
        id_producto = input("Ingrese el ID del producto: ")
        inventario.delete_product(id_producto)
        print("\n¡Producto eliminado exitosamente!")
    except ValueError as e:
        print(f"\nError: {e}")

def main():
    inventario = Inventario()
    while True:
        clear_screen()
        menu()
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1:
                registrar_producto(inventario)
            elif opcion == 2:
                listar_productos(inventario)
            elif opcion == 3:
                buscar_producto(inventario)
            elif opcion == 4:
                modificar_producto(inventario)
            elif opcion == 5:
                eliminar_producto(inventario)
            elif opcion == 6:
                print("\n¡Gracias por usar el sistema!")
                break
            else:
                print("\nOpción no válida")
            
            input("\nPresione Enter para continuar...")
        except ValueError:
            print("\nPor favor, ingrese un número válido")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
