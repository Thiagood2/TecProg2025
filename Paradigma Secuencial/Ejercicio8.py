#Crea un programa que calcule el volumen de un cilindro después de pedir al usuario el radio de la base y la altura del cilindro.


import math

radio = float(input('Ingrese el radio del cilindro: '))
altura = float(input('Ingrese la altura del cilindro: '))

volumen_cilindro = math.pi*(radio**2)*altura

print(f'El volumen del cilindro es: {volumen_cilindro} m^3')