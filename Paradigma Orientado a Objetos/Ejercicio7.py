from abc import ABC, abstractmethod
import datetime
class Cliente:
    def __init__(self, apellido, nombre, telefono):
        self.apellido = apellido
        self.nombre = nombre
        self.telefono = telefono
        self.vehiculos_cargados =[]
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos_cargados.append(vehiculo)

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido




class Tipo:

   
    def __init__(self,tipo_vehiculo, pais = None, costo_impuesto = None):
        self.tipo = tipo_vehiculo
        self.pais = pais
        self.costo_impuesto = costo_impuesto

    def get_tipovehiculo(self):
        return self.tipo

    def get_pais(self):
        return self.pais

    def get_costoimpuesto(self):
        return self.costo_impuesto

class Vehiculo(ABC):


    def __init__(self,marca,modelo,patente,kilometraje,precio_base, propietario=None):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.precio_base = precio_base
        self.kilometraje = kilometraje
        self.propietario = propietario

        if(propietario != None):
            self.propietario.agregar_vehiculo(self)

    @abstractmethod
    def obtener_precio_venta(self) -> float:
        pass
    def get_modelo(self):
        return self.modelo
    def get_marca(self):
        return self.marca

    def obtener_duenio(self):
        return self.propietario


class Auto(Vehiculo):
    def __init__(self,marca,modelo,patente,kilometraje, precio_base, tipo: Tipo, cliente = None):
        super().__init__(marca,modelo,patente,kilometraje,precio_base,cliente)
        self.tipo = tipo

    def obtener_precio_venta(self) ->float:
        precio_venta = self.__calcular_precio()
        return precio_venta

    def __calcular_precio(self):
        resultado = self.precio_base
        if self.tipo.get_tipovehiculo() == 'Nacional':
            return resultado
        else:
            resultado+= self.tipo.get_costoimpuesto()

        return resultado



class Venta:
    def __init__(self,comprador: Cliente, vehiculo: Vehiculo,fecha_venta:datetime):

        self.comprador = comprador
        self.fecha_venta = fecha_venta
        self.vehiculo_vendido = vehiculo

        comprador.agregar_vehiculo(vehiculo)

    def get_precioventa(self):
        return self.vehiculo_vendido.obtener_precio_venta()

    def get_comprador(self):
        return self.comprador

    def venta_usado(self)->bool:
        return self.vehiculo_vendido.obtener_duenio()


    def get_fechaventa(self):
        return self.fecha_venta




if __name__ == '__main__':
    nacional = Tipo('Nacional')
    importado = Tipo('Importado','USA',2340)

    propietario = Cliente('Perez','Roberto',543459340)

    auto1 = Auto('Chevrolet','Spin-Activ','AA-234-BC',195000,34500,nacional,propietario)
    auto2 = Auto('Toyota','Corolla','AB-345-CD',24000,35000,importado)
    auto3 = Auto('Nissan','March','PPQ203',240000,15000,importado,propietario)


    Comprador = Cliente('Liniers','Mateo',5354650340)
    Comprador_2 = Cliente('Ceballos','Pedro',5354650450)

    Venta_1 = Venta(Comprador,auto1,datetime.datetime.now())
    Venta_2 = Venta(Comprador,auto2,datetime.date(2024,12,11))
    Venta_3 = Venta(Comprador_2,auto3,datetime.date(2024,4,5))

    Ventas = [Venta_1,Venta_2,Venta_3]

    total_generado = 0
    for v in Ventas:
        if v.venta_usado():
            total_generado+=v.get_precioventa()

    print(f'Total generado en autos USADOS: ${total_generado}')

