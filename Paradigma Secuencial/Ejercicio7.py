#Desarrolla un programa que solicite al usuario el costo por día de alquiler de un vehículo, el número de días de alquiler y el presupuesto para combustible, y luego calcule el costo total del viaje


costo_dia_alquiler = float(input('Ingrese el alquiler por dia del vehiculo: '))
numero_dias = int(input('Ingrese la cantidad de dias del alquiler: '))
presupuesto_combustible = float(input('Ingrese el presupuesto que tiene para el combustible: '))

costo_total = (costo_dia_alquiler*numero_dias) + presupuesto_combustible

print(f'Debera garpar de su bolsillo: ${costo_total}')