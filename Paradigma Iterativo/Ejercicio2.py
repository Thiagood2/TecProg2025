#Desarrolla un programa que solicite al usuario N números y calcule su suma.

n_numeros = int(input('Cuantos numeros deseas sumar: '))

sum = 0

for i in range(1,n_numeros+1):
    numero = float(input(f'Ingrese el numero {i}: '))   
    sum+=numero

print(f'La sumatoria total de los {n_numeros} numeros da: {sum}')