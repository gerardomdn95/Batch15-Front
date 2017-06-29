#herencia hijo

from Animal import Animal

class Cat(Animal):  #herencia el utilizacion de codigo
#super es palabra reservada oara llamar al constructor padre

    def __init__(self,color,numero_vidas=1): #por que cambio de posicion
        super(Cat,self).__init__(nombre="Gatito",genero="Macho",raza="Felino")
        self.numero_vidas = numero_vidas
        self.color = color

if __name__ == '__main__':
    print(__name__)
    gato = Cat("Cafe")
    print(gato.decirNombre())
    print(gato.decirRaza())