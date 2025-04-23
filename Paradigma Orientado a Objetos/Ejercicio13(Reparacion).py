"""
- Se viola el Principio Abierto Cerrado
- Mi solucion seria aplicar DIP (Principio de Inversion de Dependecias), donde Dispositivo sea abstracta e interactue con una clase ServicioReparacion

"""


"""class Dispositivo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

class Celular(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla

class Tablet(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, lapiz: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla
        self.lapiz = lapiz

class Smartwatch(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, gps: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla
        self.gps = gps

def contar_piezas_reparacion(dispositivos: list):
    for dispositivo in dispositivos:
        if isinstance(dispositivo, Celular):
            print(contar_piezas_celular(dispositivo))
        elif isinstance(dispositivo, Tablet):
            print(contar_piezas_tablet(dispositivo))
        elif isinstance(dispositivo, Smartwatch):
            print(contar_piezas_smartwatch(dispositivo))

# Funciones para contar piezas de repuesto específicas para cada tipo de dispositivo
def contar_piezas_celular(celular: Celular):
    return "Piezas requeridas para reparar el celular"

def contar_piezas_tablet(tablet: Tablet):
    return "Piezas requeridas para reparar la tablet"

def contar_piezas_smartwatch(smartwatch: Smartwatch):
    return "Piezas requeridas para reparar el smartwatch"
"""

#Solucion
from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, marca:str, modelo:str):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def contar_piezas(self) ->str:
        pass

class Celular(Dispositivo):
    def __init__(self, marca:str, modelo:str, pantalla:bool):
        super().__init__(marca,modelo)
        self.pantalla = pantalla
    
    def contar_piezas(self) ->str:
        return "Piezas requeridas para reparar celular"
    
class Tablet(Dispositivo):
    def __init__(self, marca:str, modelo:str, pantalla:bool, lapiz:bool):
        super().__init__(marca,modelo)
        self.pantalla = pantalla
        self.lapiz = lapiz
    
    def contar_piezas(self) ->str:
        return "Piezas requeridas para reparar Tablet"

class Smartwatch(Dispositivo):
    def __init__(self, marca:str, modelo:str, pantalla:bool, gps:bool):
        super().__init__(marca,modelo)
        self.pantalla = bool
        self.gps = bool
    
    def contar_piezas(self):
        return "Piezas requeridas para reparar Smartwatch"
    

class ServiceReparacion:
    def contar_piezas_reparacion(self, dispositivos: list [Dispositivo]):
        for dispositivo in dispositivos:
            print(dispositivo.contar_piezas())


#Ejemplo de Uso
if __name__ == "__main__":
    dispositivos = [
    Celular("Samsung", "Galaxy S20", True),
    Tablet("Apple", "iPad Pro", True, True),
    Smartwatch("Apple", "Watch Series 6", True, True)
]

ServiceReparacion().contar_piezas_reparacion(dispositivos)