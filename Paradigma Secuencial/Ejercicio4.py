#### Ejercicio 4: Cálculo del Índice de Masa Corporal (IMC)
# Crea un programa que solicite el peso en kilogramos y la altura en metros de una persona, calcule su IMC y lo clasifique según la tabla de IMC.

peso_kg = float(input('Ingrese su peso: '))
altura_m = float(input('Ingrese su altura: '))

imc = (peso_kg)/(altura_m * altura_m)

PESO_BAJO = 18.5
PESO_NORMAL = 25
SOBREPESO = 30
OBESIDAD = 35

if(imc < PESO_BAJO):
    print('Tienes un peso bajo')
else:
    if(imc < PESO_NORMAL):
        print('Tienes un peso normal')
    else:
        if(imc < SOBREPESO):
            print('Tienes sobrepeso')
        else:
            print('Tienes obesidad')