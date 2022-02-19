#Kata 3

#Ejercicio 1
vel_asteroide = 49

if vel_asteroide > 25:
    print("¡Advertencia! El asteroide se acerca con una velocidad superior a 25 km/s ")
else:
    print("No hay ninguna advertencia")


#Ejercicio 2
vel_asteroide2 = 19

if vel_asteroide2 > 20:
    print("¡Hey! Busca el asteroide en el cielo")
elif vel_asteroide2 == 20:
    print("¡Hey! Busca el asteroide en el cielo")
else: 
    print("No hay nada de que preocuparse")


#Ejercicio 3
velocidad_asteroide = 25
tamaño_asteroide = 40

if velocidad_asteroide > 25 and tamaño_asteroide > 25:
    print("¡Advertencia! El asteroide que se acerca causará mucho daño ")
elif velocidad_asteroide >= 20:
    print("¡Hey! Busca el rayo de luz en el cielo")
elif tamaño_asteroide < 25:
    print("No hay de que preocuparse")
else: 
    print("No hay nada de que preocuparse")
