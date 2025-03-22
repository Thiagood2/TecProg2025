#Desarrolla un programa que cuente el número de dígitos de un número entero N.
numero = float(input('Ingrese un numero: '))

count = 0
while(numero >=1):
    numero = numero/10
    count+=1

print(f'La cantidad de digitos que posee el numero ingresado es de: {count}')