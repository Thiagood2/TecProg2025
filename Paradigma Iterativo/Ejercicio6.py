#Escribe un programa que calcule la suma de todos los números pares hasta un número N.

n_numeros = int(input('Ingrese cuantos numeros quiere sumar: '))
sum = 0
for i in range(1, n_numeros+1):
    numero = int(input(f'Ingrese el numero {i}: '))
    if(numero%2 == 0):
        sum+=numero

print(f'La cantidad de numeros pares suman: {sum}')