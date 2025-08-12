from clases.perro import Perro
# ------------------------------------------

perro1 = Perro('Firulais', 3)
perro2 = Perro("Luna", 5)

#----------------------------

print(f"{perro1.nombre} tiene {perro1.edad} anos y dice {perro1.ladrar()}")
print(f"{perro2.nombre} tiene {perro2.edad} anos y dice {perro2.ladrar()}")