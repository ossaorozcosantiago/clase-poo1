
class estudiantes:
    def __init__(self,nombre,edad,nota1,nota12,nota3):
        self.nombre=nombre 
        self.edad=edad
        self.nota1=nota1  
        self.nota2=nota2  
        self.nota3=nota3    
    def mostrar_datos(self):
        print("nombre",self.nombre)
        print("edad",self.edad)
        print("nota1",self.nota1)
        print("nota2",self.nota2)
        print("nota3",self.nota3)
    def calcular_promedio(self):
        promedio=(self.nota1,self.nota2,self.nota3)/3
        return promedio
    
"""
nombre=input(print("ingrese el nombre del estudiante"))
edad=float(input(print("ingrese la edad del estudiante")))
nota1=float(input(print("ingrese la primera nota del estudiante")))
nota2=float(input(print("ingrese la segunda nota del estudiante")))
nota3=float(input(print("ingrese la tercera nota del estudiante")))
"""






print("bienvenido al sistema de gestion de estudiantes")
lista_de_estudiantes=[]

while true:
    print("seleccione la opcion deseada")
    print("1.Agregar estudiante")
    print("2.mostrar informacion estudiante")
    print("0.salir")
    opcion=float(input())
    if opcion==1:
        nombre=input(print("ingrese el nombre del estudiante"))
        edad=input(float(print("ingrese la edad del estudiante")))
        nota1=input(float(print("ingrese la primera nota del estudiante")))
        nota2=input(float(print("ingrese la segunda nota del estudiante")))
        nota3=input(float(print("ingrese la tercera nota del estudiante")))
        estudiante =estudiante(nombre,edad,nota1,nota2,nota3)
        lista_de_estudiantes.append(estudiante)
    elif opcion==2:
        numero_estudiantes=len(lista_de_estudiantes)
        print("el numero de estudiantes es",numero_estudiantes)
        promedio_estudiantes=estudiantes.calcular_promedio()
        for estudiante in lista_de_estudiantes:
            print("el nombre del estudiante es:", estudiante.nombre
            print("el no")


        

        

