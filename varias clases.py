class estudiantes:
    def __init__(self,nombre,edad,nota):
        self.nombre=nombre
        self.edad=edad
        self.nota=nota

class Profesor:
    def __init__(self,nombre,edad,experiencia):
        self.nombre=nombre
        self.edad=edad
        self.experiencia=experiencia
        

class asignatura:
    def  __init__(self,nombre,horario,codigo,profesor):
        self.nombre=nombre
        self.horario=horario
        self.profesor=profesor
        self.estudiantes=[]
        self.codigo=codigo
    def promedio(self):
        acumulador=0
        for estudiante in self.estudiantes:
            acumulador=acumulador+estudiante.nota
        promedio=acumulador/len(self.estudiantes)
        return promedio
    def agregarestudiantes(self,estudiante):
        self.estudiantes.append(estudiante)
        print("estudiante agregado exitosamente")
    def mostrarnombres(self):
        for estudiantes in self.estudiantes:
            print(estudiantes.nombre)
    

profesor=Profesor("juan esteban",35,5)
poo=asignatura("programacion orientada a objetos","M-V 10-12",62,profesor)
estudiante1=estudiantes("estaban diaz",17,5)
estudiante2=estudiantes("luis",20,2.5)
estudiante3=estudiantes("elverga",21,3)

poo.agregarestudiantes(estudiante1)
poo.agregarestudiantes(estudiante2)
poo.agregarestudiantes(estudiante3)
print(poo.promedio())
poo.mostrarnombres()





