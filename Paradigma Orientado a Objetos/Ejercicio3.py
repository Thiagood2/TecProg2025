import datetime

class Facultad: 
    def __init__(self, nombre):
        self.nombre = nombre
        self.carreras = []
    
    def agregar_carrera (self,carrera):
        self.carreras.append(carrera)

    def mostrar_carreras_alumnos(self):

        print(f'Facultad: {self.nombre}')

        for carrera in self.carreras:
            print(f'Carrera: {carrera.nombre_carrera}')
            print('Alumnos: ')
            for inscripcion in carrera.inscripciones:
                inscripcion.mostrar_datos()


class Carrera: 
    def __init__(self, nombre_carrera):
        self.nombre_carrera = nombre_carrera
        self.inscripciones = []
    
    def agregar_inscripcion (self, inscripcion):
        self.inscripciones.append(inscripcion)



class Alumno:
    def __init__(self, nombre_alumno, dni, fecha_nacimiento):
        self.nombre_alumno = nombre_alumno
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento

    def _calcular_edad(self)->  int:
        fecha_actual = datetime.datetime.now()
        edad_actual = fecha_actual.year - self.fecha_nacimiento.year

        if (fecha_actual.month < 7):
            edad_actual-=1
        
        return edad_actual
    
    

class Inscripcion: 
    def __init__(self, carrera, alumno_inscripto, fecha_inscripcion):
        self.nombre_carrera = carrera
        self.alumno_inscripto = alumno_inscripto
        self.fecha_inscripcion = fecha_inscripcion
        
        carrera.agregar_inscripcion(self)

    def mostrar_datos (self):
        print(f'- {self.alumno_inscripto.nombre_alumno} - {self.fecha_inscripcion.date()}')



if (__name__ == "__main__"):
    Facultad = Facultad("FICH")
    informatica = Carrera("Ingenieria Informatica")
    hidricas = Carrera("Ingenieria en Recursos Hidricos")

    alumno1 = Alumno("Alumno1","11.111.111",datetime.datetime(2003,9,16))
    alumno2 = Alumno("Alumno2","22.222.222",datetime.datetime(2004,12,16))

    inscripcion1 = Inscripcion(informatica,alumno1,datetime.datetime(2008,12,10))
    inscripcion2 = Inscripcion(informatica,alumno2,datetime.datetime(2008,12,11))

    Facultad.agregar_carrera(informatica)
    Facultad.agregar_carrera(hidricas)


    Facultad.mostrar_carreras_alumnos()



        


