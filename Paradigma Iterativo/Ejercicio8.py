#Escribe un programa que convierta un número entero N a binario.

numero = int(input('Ingrese el numero decimal para convertir a binario: '))
num_binario = []
num_aux = numero

while(num_aux >=1):
    residuo = int(num_aux % 2)
    num_binario.append(residuo)
    num_aux = num_aux/2

num_binario.reverse()
print(f'El numero binario de {numero} es: {num_binario}')