class persona:
    def __init__(self,nombre,cedula,ti):
        self.nombre=nombre
        self.__cedula=cedula
        self.__ti=ti
    def obetener_documento(self):
        if self.__cedula is not None:
            return self.__cedula
        else:
            return self.__ti
        
persona1=persona("juan",11122,None)
persona2=persona("juanito",15633)

print("el nombre de la persona es",persona1.nombre)

print("el nombre de la segunda persona es",persona2.nombre)

print("el documento de la segunda persona es",persona2.cedula)