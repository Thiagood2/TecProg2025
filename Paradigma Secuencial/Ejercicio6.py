#Escribe un programa que pida al usuario la velocidad promedio de un vehículo (en km/h) y el tiempo de viaje (en horas), y luego calcule la distancia total recorrida
velocidad_prom = float(input('Ingrese su velocidad promedio: '))
tiempo_viaje = int(input('Ingrese el tiempo del viaje: '))

distancia_recorrida = velocidad_prom*tiempo_viaje

print(f'Usted recorrio: {distancia_recorrida}km')