# =============================================
# SISTEMA DE CONTROL DE VENTAS - EL SALVADOR
# Incluye 3 versiones diferentes en un solo archivo
# =============================================

# -------------------------
# VERSIÓN 1: LISTAS + DICCIONARIOS
# -------------------------
def version1():
    # Función para registrar las ventas en una lista de diccionarios
    def registrar_ventas():
        ventas = []
        n = int(input("¿Cuántos productos deseas registrar hoy? "))
        for i in range(n):
            nombre = input(f"Producto {i+1}: ")       # Nombre del producto
            precio = float(input("Precio: "))         # Precio del producto
            cantidad = int(input("Cantidad vendida: ")) # Cantidad vendida
            # Guardamos cada producto en un diccionario
            ventas.append({"producto": nombre, "precio": precio, "cantidad": cantidad})
        return ventas

    # Calcula los ingresos totales y por producto
    def calcular_ingresos(ventas):
        ingresos_totales = 0
        ingresos_por_producto = {}
        for v in ventas:
            ingreso = v["precio"] * v["cantidad"]   # Ingreso por producto
            ingresos_totales += ingreso             # Se acumula al total
            # Se suman los ingresos por producto
            ingresos_por_producto[v["producto"]] = ingresos_por_producto.get(v["producto"], 0) + ingreso
        return ingresos_totales, ingresos_por_producto

    # Muestra el reporte ordenado por mayor ingreso
    def mostrar_reporte(ingresos_totales, ingresos_por_producto):
        print("\n=== REPORTE DE VENTAS (Versión 1) ===")
        print(f"Ingreso total: ${ingresos_totales:.2f}")
        print("\nIngresos por producto (ordenados):")
        for prod, ingreso in sorted(ingresos_por_producto.items(), key=lambda x: x[1], reverse=True):
            print(f"{prod}: ${ingreso:.2f}")

    # Ejecución de esta versión
    ventas_registradas = registrar_ventas()
    total, ingresos = calcular_ingresos(ventas_registradas)
    mostrar_reporte(total, ingresos)


# -------------------------
# VERSIÓN 2: CLASES Y OBJETOS
# -------------------------
def version2():
    # Clase que representa una venta
    class Venta:
        def __init__(self, producto, precio, cantidad):
            self.producto = producto
            self.precio = precio
            self.cantidad = cantidad
        
        # Método que calcula el ingreso de esa venta
        def ingreso(self):
            return self.precio * self.cantidad

    # Función para registrar ventas como objetos de la clase Venta
    def registrar_ventas():
        lista = []
        n = int(input("Número de productos vendidos: "))
        for i in range(n):
            prod = input(f"Producto {i+1}: ")
            precio = float(input("Precio: "))
            cant = int(input("Cantidad: "))
            lista.append(Venta(prod, precio, cant))  # Guardamos el objeto en la lista
        return lista

    # Calcula ingresos totales y por producto
    def calcular_ingresos(ventas):
        total = 0
        ingresos = {}
        for v in ventas:
            ingreso = v.ingreso()
            total += ingreso
            ingresos[v.producto] = ingresos.get(v.producto, 0) + ingreso
        return total, ingresos

    # Muestra reporte en pantalla ordenado
    def mostrar(ingresos_totales, ingresos):
        print("\n--- REPORTE (Versión 2) ---")
        print(f"Ingreso total: ${ingresos_totales:.2f}")
        print("Por producto (más a menos):")
        for prod, ing in sorted(ingresos.items(), key=lambda x: x[1], reverse=True):
            print(f"{prod}: ${ing:.2f}")

    # Ejecución de esta versión
    datos = registrar_ventas()
    total, ingresos = calcular_ingresos(datos)
    mostrar(total, ingresos)


# -------------------------
# VERSIÓN 3: DICCIONARIOS ANIDADOS
# -------------------------
def version3():
    # Registra productos en un diccionario anidado
    def registrar():
        productos = {}
        n = int(input("¿Cuántos productos quieres ingresar? "))
        for i in range(n):
            nombre = input(f"Producto {i+1}: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad vendida: "))
            # Si el producto ya existe, se acumula la cantidad
            if nombre in productos:
                productos[nombre]["cantidad"] += cantidad
            else:
                productos[nombre] = {"precio": precio, "cantidad": cantidad}
        return productos

    # Calcula ingresos totales y por producto
    def calcular(productos):
        total = 0
        ingresos = {}
        for nombre, datos in productos.items():
            ingreso = datos["precio"] * datos["cantidad"]
            ingresos[nombre] = ingreso
            total += ingreso
        return total, ingresos

    # Muestra el reporte final
    def reporte(total, ingresos):
        print("\n+++ REPORTE FINAL (Versión 3) +++")
        print(f"Ingreso total: ${total:.2f}")
        print("\nIngresos por producto (ordenados):")
        for prod, ing in sorted(ingresos.items(), key=lambda x: x[1], reverse=True):
            print(f"{prod}: ${ing:.2f}")

    # Ejecución de esta versión
    productos = registrar()
    total, ingresos = calcular(productos)
    reporte(total, ingresos)


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------
if __name__ == "__main__":
    print("=== SISTEMA DE CONTROL DE VENTAS ===")
    print("1. Versión 1 (Listas + Diccionarios)")
    print("2. Versión 2 (Clases y Objetos)")
    print("3. Versión 3 (Diccionarios anidados)")
    
    # El usuario elige qué versión ejecutar
    opcion = input("Selecciona una versión (1/2/3): ")

    if opcion == "1":
        version1()
    elif opcion == "2":
        version2()
    elif opcion == "3":
        version3()
    else:
        print("Opción no válida")
