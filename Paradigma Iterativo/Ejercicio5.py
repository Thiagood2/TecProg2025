#Realiza un programa que genere y muestre la tabla de multiplicar de un número N introducido por el usuario.
numero = float(input('Ingrese numero para calcular su tabla de multiplicar: '))

for i in range(1,10+1):
    print(f' Tabla del {i} es: {numero*i}')