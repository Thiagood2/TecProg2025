class Empleado: 
    def __init__(self,nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    def get_horas(self):
        return self.horas_trabajadas
    
    def get_tarifa (self):
        return self.tarifa_por_hora

    # Viola el principio de Responsabilidad Unica (Implementado en la clase GestionEmpleado)
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora
    

class GestionEmpleado:
    def __init__(self):
        pass

    def calcular_salario(self,empleado):
        salario = empleado.get_horas()  * empleado.get_tarifa()
        return salario

