#Crea un programa que lea N números del usuario y calcule su media.

n_numeros = int(input('Ingrese la cantidad de numeros a promediar: '))
sum = 0
for i in range(1, n_numeros+1):
    numero = float(input(f'Ingrese el numero {i}: '))
    sum+=numero

promedio = sum / n_numeros
print(f'La media de los numeros ingresados es: {promedio}')