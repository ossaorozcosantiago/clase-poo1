#crear lista
milista=[0]*10
print(milista)

import random
for i in range(0,100):
    listarandom=[random.randint(1,100)]*10 #random.randint me permite numeros aleatorios entre rango x1 y x2----random.randint(x1,x2)
print(listarandom)

listarandom2=[random.randint(1,100) for _ in range(10)] #random.randint me permite numeros aleatorios y con for establece el numero de posiciones 
print(listarandom2)

listaejemplo=[i for i in range(0,10)] #generar una lista en i que recorra un i de rango desde 1 hasta 9

print(listaejemplo)
listaejemplo[1] = 0  #cambiar valores en la posicion[x] en la lista que se genera
listaejemplo[4] = 2
print(listaejemplo)

listaejemplo.remove(7) #eliminar el valor en la lista
print(listaejemplo)

del listaejemplo[2] #elimina posicion 2 en la lista
print(listaejemplo)

listaejemplo=[elemento for elemento in listaejemplo if elemento!=1] #para solo dejar elementos diferentes de 1
print(listaejemplo)

listaejemplo.reverse() #ubicar las posiciones alrevez
print(listaejemplo)

listaejemplo.sort() #ordena de menor a mayor segun su valor
print(listaejemplo) 

listaejemplo.sort(reverse=True) #ordena de mayor a menor segun su valor


#ejercio de practica 
#crear clase de persona que permita tener el nombre y una lista de numeros por persona, los numeros se generan aleatoriamente

print("bienvenido al sistema de rifas")
class personas:
    def __init__(self,nombre):
        self.nombre=nombre
        self.numeros=[random.randint(100,999) for _ in range(6)]
    
    
listapersonas=[]
while True:
    import random
    print("seleccione una opcion para cpntinuar")
    print("1-inscribirme")
    print("2-conocer los numeros")
    print("0-salir")
    opcion=int(input())
    if opcion==1:
        nombre=input("ingrese el nombre")
        print("inscripcion exitosa")
        nuevapersona=personas(nombre)
        print("sus numeros son",personas.numeros)
        listapersonas.append(nuevapersona)
    
