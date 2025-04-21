""" 
-   Se rompe el Principio de Responsabilidad Unica(SRP) puesto que la clase Empleado solo debe manejar
la informacion de Empleado, no realizar tareas que exceden a su clase
-   A su vez, tarifa por hora no es una informacion de un empleado, se deberia manejar de otra manera
-   Para el reporte, se podria realizar una interfaz que maneje todo tipo de reporte (PDF,WORD,EXCEL..etc)"""

from abc import ABC, abstractmethod
class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        # self.tarifa_por_hora = tarifa_por_hora 

    #def calcular_salario(self):
        #return self.horas_trabajadas * self.tarifa_por_hora

    def horas_trabajadas(self):
        return self.horas_trabajadas

    def generar_reporte_desempenio(self):
        pass

class GestionEmpleado:
    def calcular_salario(self, empleado:Empleado, tarifa_por_hora):
        salario = empleado.horas_trabajadas * tarifa_por_hora
        return salario

class IGestionReporte(ABC):
    @abstractmethod
    def generar_reporte_desempenio(self, empleado:Empleado):
        pass

