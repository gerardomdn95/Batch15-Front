#herencia padre

class Animal:

    def __init__(self,nombre,genero,raza):

        self.nombre = nombre
        self.genero = genero
        self.raza = raza


    def decirNombre(self): #este es un get porque te trae informacion
        print("Mi nombre es:"+self.nombre)

    def decirRaza(self):
        print("Mi raza es:"+self.raza)