## Problema 4: HashingAgregue a la clase "Persona", creada en el Problema 2, un nuevo atributo que sea la clave personal o contraseña. Esta contraseña debe contener un string que se genere con la clave hasheada con SHA256. Por ejemplo, si la clave es "password", el atributo debe contener el valor "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8".Agregue una nueva funcionalidad a la clase "Persona" que valide la contraseña con un método que reciba como parámetro la contraseña a evaluar y la compare con el valor de la instancia. Este método debe devolver "Verdadero" si coincide y "Falso" en caso contrario.


import hashlib
def encode_string(value):
    return value.encode('ASCII')
class Persona:
    def __init__(self,name,apellido,fecha_nac, password:int):
        password_encriptada = hashlib.sha256(encode_string(password)).hexdigest()
        self.nombre = name
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.password = password_encriptada

    def validar_password (self,password):

        return self.password == hashlib.sha256(encode_string(password)).hexdigest()
    
if (__name__ == "__main__"):
    juan = Persona("Juan", "Perez", "1990-11-11","password")

    print(juan.validar_password("password"))
    print(juan.validar_password("incorrecto"))