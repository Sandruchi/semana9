class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir un nuevo producto
    def añadir_producto(self, producto):
        # Verificar que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print(f"Producto {producto.get_nombre()} añadido al inventario.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(f"Producto {p.get_nombre()} eliminado del inventario.")
                return
        print("Error: Producto no encontrado.")

    # Actualizar cantidad o precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(f"Producto {p.get_nombre()} actualizado.")
                return
        print("Error: Producto no encontrado.")

    # Buscar producto(s) por nombre (pueden ser nombres similares)
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_todos(self):
        if self.productos:
            for p in self.productos:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("El inventario está vacío.")


def mostrar_menu():
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Entrada no válida.")

        elif opcion == "2":
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: Entrada no válida.")

        elif opcion == "3":
            try:
                id_producto = int(input("ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (dejar en blanco si no se desea actualizar): ")
                precio = input("Nuevo precio (dejar en blanco si no se desea actualizar): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Entrada no válida.")

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
