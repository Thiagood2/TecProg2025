#Dada la siguiente clase Persona: codifíquela en lenguaje Python. Agregue una nueva clase llamada "Principal" que tenga ejecución y demuestre el concepto de identidad de un objeto.

class Persona: 
    def __init__ (self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
    

class Principal:
    def __init__(self):
        pass

    def ejecutar(self):
        persona_1 = Persona("Thiago",21)
        persona_2 = Persona("Mateo",20)

        print(f'''Id_1: {id(persona_1)}, Id_2: {id(persona_2)}''')
        
        if(persona_1.nombre == persona_2.nombre) and (persona_1.edad == persona_2.edad):
            print('Los objetos son iguales')

if __name__ == "__main__":
    principal = Principal()
    principal.ejecutar()
