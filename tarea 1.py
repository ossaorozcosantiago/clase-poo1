class Producto_vendido:
    def __init__(self, nombre, precio, cantidad,codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo=codigo

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            print(f'Se vendieron {cantidad_vendida} unidades de {self.nombre}')
        else:
            print(f'No hay unidades de {self.nombre} Quedan: {self.cantidad}')

    def mostrar_stock(self):
        print(f'Producto: {self.nombre}  Precio: {self.precio}  Stock disponible: {self.cantidad} unidades')

lista_productos=[]
print("bienvenido al sistema de ventas")

while True:
    print("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES")
    print("1.AGREGAR PRODUCTO")
    print("2.VENDER PRODUCTO")
    print("3.MOSTRAR INVENTARIO")
    print("salir")
    opcion=int(input())

    if opcion==1:
        nombre=input("ingrese el nombre del producto")
        precio=float(input("ingrese el valor del producto"))
        cantidad=int("ingrese la cantidad")
        codigo=int(input("ingrese su codigo"))

        nuevo_producto=Producto_vendido(nombre,precio,cantidad,codigo)
        lista_productos.append(nuevo_producto)
    elif opcion==2:
        codigo_producto=int(input("ingrese el codigo del producto")) 
        for producto_vendido in lista_productos:
            if producto_vendido.codigo==codigo_producto:
                cantidad_vendida=int(input("ingrese la cantidad"))
                producto_vendido.vender(cantidad_vendida)
                existe=True
        if existe==False:
            print("el prodcuto no existe")