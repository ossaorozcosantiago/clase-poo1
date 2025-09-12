class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def hacer_sonido(self):
        print(f'{self.nombre} hace un sonido')
    def todos_orinan(self):
        print(f'{self.nombre} esta orinando')


class perro(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} hace guau guau')
    def salir_a_pasear(self):
        print(f'{self.nombre} esta paseando')

class gato(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} hace miau miau')


animal=perro("mia")
animal.hacer_sonido()
animal.salir_a_pasear()

animal1=gato("simba")
animal1.hacer_sonido()
animal1.todos_orinan()

#SI TENGO ISINTANCE(A,B) ENTONCES ME SIRVE PARA VEIRIFICAR SI A ES HIJO DE B,esto me permite verificar si un objeto pertenece a una clase o es hijo de una
print(isinstance(animal,perro))
print(isinstance(animal,Animal))
print(isinstance(animal1,perro))
print(isinstance(animal1,Animal))

#ejercicio
#crea una clase persona y una clase estudiante que herede de persona

class persona:
    def __init__(self,nombre):
        self.nombre=nombre
    def soy_padre(self,respuesta):
        self.respuesta=respuesta 
        print(f'{self.respuesta} soy padre')

class estudiante(persona):
    def __init__(self,nombre,nombre_padre):
        super().__init__(nombre)
        self.nombre=nombre_padre
    def mi_padre(self):
        print(f'{self.nombre} y mi padre es {self.nombre_padre}')

persona1=persona("raul")
persona1.soy_padre("si")
persona2=estudiante("camila")
persona2.mi_padre()
