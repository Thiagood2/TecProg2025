'''Se requiere desarrollar un sistema de nómina para los trabajadores de una empresa. Los datos personales de los trabajadores incluyen Nombre y Apellidos, Dirección y DNI. Existen diferentes tipos de trabajadores:
Mensualizados: Estos empleados reciben una cantidad fija cada mes, basada en la categoría que tienen.
Jornalizados: Estos empleados reciben un pago por cada hora trabajada durante el mes. El precio es fijo para las primeras 40 horas y diferente para las horas restantes.
Jefe: Estos empleados tienen un salario fijo, que es un acuerdo personal con la empresa.
Cada empleado tiene obligatoriamente un jefe, excepto los jefes que no tienen ninguno. El sistema debe ser capaz de calcular las remuneraciones de cada trabajador en un período dado.'''

from abc import ABC, abstractmethod

class Empresa:
    def __init__(self, nombre_empresa):
        self.nombre = nombre_empresa
        self.empleados = []
        self.categorias = []

    def agregar_empleado(self,empleado):
        self.empleados.append(empleado)

    def agregar_categoria(self,categoria):
        self.categorias.append(categoria)

    def listar_empleados(self):
        for empleado in self.empleados:
            print(f'''Empleado: {empleado.obtener_nombre()}_{empleado.obtener_apellido()}   
        DNI:{empleado.obtener_dni()} 
        SUELDO: ${empleado.obtener_sueldo()}''')


class Empleado (ABC):
    def __init__(self, nombre, apellido, direccion, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.dni = dni

    def obtener_nombre(self):
        return self.nombre
    def obtener_apellido(self):
        return self.apellido
    def obtener_direccion(self):
        return self.direccion
    def obtener_dni(self):
        return self.dni
    def obtener_sueldo(self):
        return self.calcular_sueldo()
    @abstractmethod
    def calcular_sueldo(self):
        pass


class Mensualizado(Empleado):

    def __init__(self, nombre, apellido, direccion, dni, jefe, categoria):
        super().__init__(nombre,apellido,direccion,dni)
        jefe.agregar_empleado(self)
        categoria.agregar_empleado(self)
        self.categoria = categoria


    def calcular_sueldo(self):
       return self.categoria.obtener_sueldo()



class Jornalizado(Empleado):
    def __init__(self, nombre, apellido, direccion, dni, jefe, horas_trabajadas, tarifa_normal,  tarifa_extra):

        super().__init__(nombre,apellido,direccion,dni)
        jefe.agregar_empleado(self)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_normal = tarifa_normal
        self.tarifa_extra = tarifa_extra

    def calcular_sueldo(self):
        sueldo_base = self.horas_trabajadas * self.tarifa_normal

        if(self.horas_trabajadas <40):
            return sueldo_base
        else:
            horas_extras = 40 - self.horas_trabajadas
            sueldo_base += horas_extras * self.tarifa_extra

        return sueldo_base


class Jefe(Empleado):
    def __init__(self,nombre,apellido,direccion,dni,sueldo_base):
        super().__init__(nombre,apellido,direccion,dni)
        self.empleados_pertenecientes = []
        self.sueldo_base = sueldo_base

    def agregar_empleado(self,empleado):
        self.empleados_pertenecientes.append(empleado)

    def calcular_sueldo(self):
        return self.sueldo_base

class Categoria:
    def __init__(self, nombre_categoria, sueldo_base):
        self.empleados = []
        self.nombre_categoria = nombre_categoria
        self.sueldo_base = sueldo_base

    def agregar_empleado(self,empleado):
        self.empleados.append(empleado)

    def obtener_sueldo(self):
        return self.sueldo_base


if __name__ == '__main__':
    print('Probando el programa')

    mi_empresa = Empresa('mi_empresa')
    categoria_1 = Categoria('categoria_1',1500)
    mi_empresa.agregar_categoria(categoria_1)

    empleado_jefe = Jefe('empleado','jefe','ramirez',15203450,3500)
    empleado_mensualizado = Mensualizado('empleado','mensualizado','ramirez',20456734,empleado_jefe,categoria_1)
    empleado_jornalizado = Jornalizado('empleado','jornalizado','ramirez',35230456,empleado_jefe,45,5,7)

    mi_empresa.agregar_empleado(empleado_jefe)
    mi_empresa.agregar_empleado(empleado_mensualizado)
    mi_empresa.agregar_empleado(empleado_jornalizado)

    mi_empresa.listar_empleados()