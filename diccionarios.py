"""#diccionario: clave- valor
ejemplo: clave=1--valor"juan esteban"

#creamos la agenda con 3 contactos
agenda={
    "ana":"3000000000",
    "bruno":"310365226",
    "carla":"454664646544",
}

nombre=input("ingrese el nombre")

if nombre in agenda:
    print("el numero de telefono de"+nombre,agenda[nombre])
else:
    print("no esta")

#agg un nuevo contacto
agenda["juan"]="3052606500"

#eliminar contacto
del agenda["ana"]

#mostrar todos los valores del diccionario
print("diccionario contenido",agenda)

estudiantes={
    "lucia":[4.5,3.8,4.2],
    "mateo":[4.5,3.8,4],
    "sofia":[5.0,1,5],
}

promedios={}
for nombre,notas in estudiantes.items():
    prom=sum(notas)/len(notas)

"""

#ejercicio de repaso

print("bienvenido al sistema de ventas escolar")
while True:
    inventario={
    "cuaderno":15,
    "lapiz":40,
    "borrador":0,
    "marcador":10,
    "regla":5,
}
    print("ingrese un numero para continuar")
    print("1-agregar producto---2-añadir cantidad----3-vender---4-salir")
    opcion=int(input())
    if opcion==1:
        productonuevo=input("ingrese el nombre del producto")
        cantidad=int(input("ingrese la cantidad"))
        inventario[productonuevo]=cantidad
        print("agregado exitosamente")
    elif opcion==2:
        producto=input("ingrese el producto a buscar")
        if producto in inventario:
            cantidad=int(input("añada la cantidad"))
            inventario[producto]+=cantidad
        else:
            print("el producto no existe")
    elif opcion==3:
        producto=input("ingrese el producto a buscar")
        if producto in inventario:
            cantidad=input("añada la cantidad a vender")
            inventario[producto]-=cantidad
        else:
            print("el producto no existe")
    elif opcion==4:
        print("hasta luego")
        break
    else:
        print("opcion incorrecta")

