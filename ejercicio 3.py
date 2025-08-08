"""uml
class>>cuenta
atributos>> 
nombre:str
numero:int
saldo:float
metodo>>
depositar(cantidad):float
retirar(cantidad):float
consultar():float
"""
class cuenta:
    def __init__(self,nombre,):
        self.nombre=nombre
        self.numero=random.randint(1000,10000)
        self.saldo=0
    def despositar(self,cantidad):
        self.saldo=self.saldo+cantidad
        return self.saldo
    def retirar(self,cantidad):
        if cantidad<=self.saldo:
            self.saldo=self.saldo-cantidad
            return self.saldo
        else:
            return -1
    def consultar(self):
        self.saldo
listacuentas=[]

import random
print("bienvenido al sistema bancario")
while True:
    print("ingrese una opcion para continua1r")
    print("1.registrar cuenta")
    print("2.depositar")
    print("3.retirar")
    print("4.consultar saldo")
    print("5.salir")
    opcion=float(input())
    if opcion ==1:
        nombre=input("ingrese el nombre del titular de la cuenta")
        print("cuenta registrada exitosamente")
        nuevacuenta=cuenta(nombre)
        print("su numero de cuenta es:",nuevacuenta.numero)
        listacuentas.append(nuevacuenta)
    elif opcion ==2:
        numero_cuenta=input(int("ingrese el numero de cuenta"))
        existe=False
        for cuenta in listacuentas:
            if cuenta.numero==numero_cuenta:
                existe=True
                cantidad=float(input("ingrese la cantidad a ingresar"))
                nuevo_saldo=cuenta.despositar(cantidad)
                print("el nuevo saldo es:",nuevo_saldo)
            if existe==False:
                print("su cuenta no existe")
    elif opcion ==3:
        numero_cuenta=input(int("ingrese el numero de cuenta"))
        existe=False
        for cuenta in listacuentas:
            if cuenta.numero==numero_cuenta:
                existe=True
                cantidad=float(input("ingrese la cantidad a retirar"))
                nuevo_saldo=cuenta.retirar(cantidad)
                
                if nuevo_saldo>=0:
                    print("el nuevo saldo es:",nuevo_saldo)
        if existe==False:
                 print("su cuenta no existe")   
    elif opcion ==4:
        numero_cuenta=input(int("ingrese el numero de cuenta"))
        existe=False
        for cuenta in listacuentas:
            if cuenta.numero==numero_cuenta:
                existe=True
                print("el saldo es:",cuenta.consultar())
        if existe==False:
                print("su cuenta no existe")
    elif opcion==5:
        print("hasta luego")
        break
    else:
        print("opcion incorrecta")
        
