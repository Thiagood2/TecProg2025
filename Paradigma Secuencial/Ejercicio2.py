segundos = int(input('Introduce la cantidad de segundos: '))
horas = 0
minutos = int(segundos / 60)
segundos = int(segundos % 60)

if(minutos > 60):
    horas = int(minutos/60)
    i=0
    while(i<horas):
        minutos = minutos - 60
        i+=1

print(f'''Horas: {horas}, Minutos: {minutos}, Segundos: {segundos}''')