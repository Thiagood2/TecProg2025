"""
- Primeramente, se viola el Principio Abierto Cerrado (OCP), puesto que la clase Notificadora no esta adaptada
para la extension, solo puede recibir un tipo de envio de mensajes que es por Correo Electronico
- Segundo, lo que haria es realizar una Interfaz que maneje distintos tipos de Envio de mensajes, y la clase Notificador la haria un metodo generico
- Algo a tener en cuenta, es que los parametros tendrian que variar dependiendo del tipo de Envio, no lo voy a hacer pero se realizaria con **kwargs (permite tener parametros adicionales)
"""


"""class CorreoElectronico:
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        # Lógica para enviar notificación por correo electrónico
        print(f"Correo electrónico enviado a {destinatario}: {mensaje}")

class Notificador:
    def __init__(self, correo_electronico: CorreoElectronico):
        self.correo_electronico = correo_electronico

    def enviar_notificacion(self, destinatario: str, mensaje: str):
        self.correo_electronico.enviar_notificacion(destinatario, mensaje)"""

#Solucion
from abc import ABC, abstractmethod

class IMedioComunicacion(ABC):
    @abstractmethod
    def enviar_notificacion(self,destinatario:str, mensaje:str):
        pass

class CorreoElectronico(IMedioComunicacion):
    def enviar_notificacion(self, destinatario, mensaje):
        super().enviar_notificacion(destinatario, mensaje)
        print(f'Enviando "{mensaje}" a ({destinatario}) a traves de CorreoElectronico')

class SMS(IMedioComunicacion):
    def enviar_notificacion(self,destinatario,mensaje):
        super().enviar_notificacion(destinatario,mensaje)
        print(f'Enviando "{mensaje}" a ({destinatario}) a traves de SMS')

def notificador(tipo_comunicacion: IMedioComunicacion,destinatario,mensaje):
    tipo_comunicacion.enviar_notificacion(destinatario,mensaje)

# Uso del código actual
if __name__ == "__main__":
    correo_electronico = CorreoElectronico()
    sms = SMS()

    notificador(sms,'Lucas','Hola bestia')
    notificador(correo_electronico,'Mateo','Hola maquina')
