#Kata 4

#Ejercicio 1
#Division del texto
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""


oraciones = text.split('. ')
print(oraciones)

#Busqueda palabras clave. Define las palabras pista: average, temperature y distance 
palabras_clave = ["average", "temperature", "distance"]

#Ciclo for
for sentence in oraciones:
    for palabras_clave in palabras_clave:
        if palabras_clave in sentence:
            print(sentence.replace(' C', ' Celsius')) #Cambiar C a Celsius
            break

#Ejercicio  2
# Datos 
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

titulo = f'Gravity Facts about {name} and {planet}'

hechos = f"""{'-'*80}
Nombre del planeta: {planet}
Gravedad en {name}: {gravity * 1000} m/s2
"""

template = f"""{titulo.title()}
{hechos}
"""
#print(hechos)

#Comprobar
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

#print(hechos)
new_template = """
Datos de gravedad sobre: {nombre}
---------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))
