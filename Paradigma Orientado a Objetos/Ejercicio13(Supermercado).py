"""
- Se rompe el Principio Abierto Cerrado, puesto que si extendemos las categorias el calcular descuento se tendria que modificar
- Lo primero seria abstraer las categorias y crear una clase por cada clasificacion, para poder obtener el descuento por cada categoria
- Luego, crear una funcion 'carrito' que te muestre los descuentos de los productos seleccionados
"""


"""class Producto:
    def __init__(self, nombre: str, categoria: str):
        self.nombre = nombre
        self.categoria = categoria

class Carrito:
    def __init__(self, productos: list):
        self.productos = productos

def calcular_descuento(productos: list):
    for producto in productos:
        if producto.categoria == 'alimentos':
            print(f"Descuento del 10% en {producto.nombre}")
        elif producto.categoria == 'limpieza':
            print(f"Descuento del 5% en {producto.nombre}")
        # Añadir más condiciones para nuevos tipos de productos y descuentos

productos = [
    Producto('manzanas', 'alimentos'),
    Producto('jabón', 'limpieza')
]

carrito = Carrito(productos)
calcular_descuento(carrito.productos)"""

class Producto:
    def __init__(self,nombre:str, categoria):
        self.nombre = nombre
        self.categoria = categoria
    def obtener_categoria(self):
        return self.categoria
    def obtener_nombre(self):
        return self.nombre
    

from abc import ABC,abstractmethod

class Categoria(ABC): #No es una interfaz, es una clase abstracta
    def __init__(self, nombre_categoria:str):
        self.nombre_categoria = nombre_categoria
    def obtener_nombre(self):
        return self.nombre_categoria
    @abstractmethod
    def obtener_descuento(self):
        pass

class Limpieza(Categoria):
    def __init__(self, nombre_categoria:str):
        super().__init__(nombre_categoria)
    
    def obtener_descuento(self):
        return f'5%'

class Alimentos(Categoria):
    def __init__(self,nombre_categoria:str):
        super().__init__(nombre_categoria)
    
    def obtener_descuento(self):
        return f'10%'
    
class Electrodomesticos(Categoria):
    def __init__(self,nombre_categoria:str):
        super().__init__(nombre_categoria)
    
    def obtener_descuento(self):
        return f'20%'

def carrito(productos : list[Producto]):
    for producto in productos:
        print(f'El producto {producto.obtener_nombre()} de la categoria: [{producto.obtener_categoria().obtener_nombre()}] tiene un descuento de: {producto.obtener_categoria().obtener_descuento()}')


if __name__ == "__main__":
    limpieza = Limpieza("Limpieza")
    alimentos = Alimentos('Alimentos')
    electrodomesticos = Electrodomesticos('Electrodomesticos')

    productos = [
        Producto('Manzana',alimentos),
        Producto('Escoba',limpieza),
        Producto('Lavarropas',electrodomesticos)
    ]
    carrito(productos)