#Escribe un programa que pida al usuario N números y encuentre el máximo de ellos.

n_numeros = int(input('Ingrese la cantidad de numeros a comparar: '))

max_num = 0
for i in range(1,n_numeros+1):
    numero = float(input(f'Ingrese el numero {i}: '))
    if(numero > max_num):
        max_num = numero

print(f'El numero mayor ingresado es: {max_num}')