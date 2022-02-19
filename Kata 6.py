#Kata 6

#Ejercicio 1
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print('Hay', len(planets), 'planetas')

planets.append('Pluto')
print(planets[-1], 'es el ultimo planeta')
print('Ahora hay', len(planets), 'planetas')


#Ejercicio 2
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

nombre = input("Ingrese el nombre de un planeta (con mayucula la primera letra) ")

nombre_index = planets.index(nombre)
print('Los planetas mas cercanos a ' + nombre)
print(planets[0:nombre_index])

print('Los planetas mas lejanos a ' + nombre)
print(planets[nombre_index + 1:])