#Kata 5

#Ejercicio 1
primer_planeta = 149597870 
segundo_planeta = 778547200 

#operacion
distancia_km = segundo_planeta - primer_planeta 
print(distancia_km)

distancia_mi = distancia_km * 0.621
#print(distancia_mi)

from math import ceil

round_up = ceil(distancia_mi) 
print(round_up)


#Ejercicio 2
primerplaneta = input("Ingrese la distancia del sol para el primer planeta ")
segundoplaneta = input("Ingrese la distancia del sol para el segundo planeta ")

primerplaneta = int(primerplaneta)
segundoplaneta = int(segundoplaneta)

distanciakm = segundoplaneta - primerplaneta
print(distanciakm)

distanciami = distanciakm * 0.621
print(abs(distanciami))