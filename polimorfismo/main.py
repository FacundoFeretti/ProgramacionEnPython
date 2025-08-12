from polimorfismo.clases.vaca import Vaca
from polimorfismo.clases.gato import Gato
from polimorfismo.clases.perro import Perro


def hacer_sonido_de_animal(animal):
    print(animal.hacer_sonido())

perro = Perro('Firulais')
gato = Gato('Pelusa')
vaca = Vaca('Lechera')

hacer_sonido_de_animal(perro)
hacer_sonido_de_animal(gato)
hacer_sonido_de_animal(vaca)