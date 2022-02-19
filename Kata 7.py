#Kata 7

#Ejercicio 1 & ejercicio 2
new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet or done when done: ')

for planet in planets:
    print(planet)
