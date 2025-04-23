"""
- Se viola el Principio de Segregacion de Interfaces, porque la clase Estudiante depende de funcionalidades innecesarias.
- Se tendrian que crear 2 interfaces, Una general y otra que solo utilice Profesor.
"""

"""from abc import ABC, abstractmethod
class IUsuario(ABC):
    @abstractmethod
    def solicitar_prestamo_libro(self):
        pass

    @abstractmethod
    def devolver_libro(self):
        pass

    @abstractmethod
    def buscar_libro(self):
        pass

    @abstractmethod
    def solicitar_reserva_sala_estudio(self):
        pass

class Estudiante(IUsuario):
    def solicitar_prestamo_libro(self):
        print("Estudiante solicitando préstamo de libro.")

    def devolver_libro(self):
        print("Estudiante devolviendo libro.")

    def buscar_libro(self):
        print("Estudiante buscando libro en el catálogo.")

    def solicitar_reserva_sala_estudio(self):
        raise NotImplementedError("Los estudiantes no pueden reservar salas de estudio.")

class Profesor(IUsuario):
    def solicitar_prestamo_libro(self):
        print("Profesor solicitando préstamo de libro.")

    def devolver_libro(self):
        print("Profesor devolviendo libro.")

    def buscar_libro(self):
        print("Profesor buscando libro en el catálogo.")

    def solicitar_reserva_sala_estudio(self):
        print("Profesor solicitando reserva de sala de estudio.")"""

# Solucion
from abc import ABC,abstractmethod

class IUsuario(ABC):
    @abstractmethod
    def solicitar_prestamo_libro(self):
        pass
    
    @abstractmethod
    def devolver_libro(self):
        pass
    
    @abstractmethod
    def buscar_libro(self):
        pass

class IProfesor(ABC):
    @abstractmethod
    def solicitar_reserva_sala_estudio(self):
        pass

class Estudiante(IUsuario):
    def solicitar_prestamo_libro(self):
        print("Estudiante solicitando préstamo de libro.")

    def devolver_libro(self):
        print("Estudiante devolviendo libro.")

    def buscar_libro(self):
        print("Estudiante buscando libro en el catálogo.")

class Profesor(IUsuario,IProfesor):
    def solicitar_prestamo_libro(self):
        print("Profesor solicitando préstamo de libro.")

    def devolver_libro(self):
        print("Profesor devolviendo libro.")

    def buscar_libro(self):
        print("Profesor buscando libro en el catálogo.")

    def solicitar_reserva_sala_estudio(self):
        print("Profesor solicitando reserva de sala de estudio.")


#Ejemplo de Uso

if __name__ == "__main__":
    estudiante = Estudiante()
    profesor = Profesor()

    estudiante.solicitar_prestamo_libro()
    estudiante.devolver_libro()
    estudiante.buscar_libro()

    profesor.solicitar_prestamo_libro()
    profesor.devolver_libro()
    profesor.buscar_libro()
    profesor.solicitar_reserva_sala_estudio()