# A la clase Persona agréguele un atributo del tipo datetime.date para representar la fecha de nacimiento. Modifique el constructor de la clase teniendo en cuenta el nuevo atributo y agregue un método privado llamado calcular_edad() que devuelva la #edad de la persona y otro método mostrar() que muestre en la salida estándar o consola: apellido, nombre: edad → "Juan, Perez: 22 años." + Día del cumpleaños en el año en curso.

import datetime
class Persona: 
    def __init__ (self,nombre,apellido,fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
    
    def _calcular_edad(self):
        tiempo_actual = datetime.datetime.now()
        edad_actual =  tiempo_actual.year - self.fecha_nacimiento.year

        aux_fecha = datetime.datetime(tiempo_actual.year, self.fecha_nacimiento.month, self.fecha_nacimiento.day )
        dif_dias = abs(tiempo_actual - aux_fecha).days

        if tiempo_actual.month < 7:
            edad_actual-=1
        
        return edad_actual,dif_dias
    
    def mostrar(self):
        edad, diferencia_dias = self._calcular_edad()

        print(f'{self.nombre}, {self.apellido}: {edad} anios -> Faltan {diferencia_dias} dias para su cumple')
        
        

if __name__ == "__main__":
    persona = Persona("Thiago","Martinez", datetime.datetime(2003,9,16))
    persona.mostrar()






