# Dado el siguiente diagrama de UML, se implementó el comportamiento que cuenta la cantidad de egresados y muestra el promediode cada uno de ellos. Teniendo en cuenta las reglas del buen diseño, evalúe el siguiente código y modifíquelo si fuera necesario. Justifique cada una de las modificaciones
from typing import List
import datetime

from abc import ABC, abstractmethod
class Carrera:
    def __init__(self):
        self.c_alumnos: List[Alumno] = []

    def listar_egresados(self):
        evaluador = EvaluadorAlumno()
        alumnos_egresados = self.verificar_egresados()

        print(f'Cantidad de egresados: {len(alumnos_egresados)}')

        for alumno in alumnos_egresados:
            evaluador.calcular_promedio(alumno)
            print(f'{alumno.get_nombre()} - Promedio: {evaluador.get_promedio()}')

    def verificar_egresados(self):
        alumnos_egresados = []

        for alumno in self.c_alumnos:
            if alumno.get_fecha_egreso() is  not None:
                alumnos_egresados.append(alumno)
        return alumnos_egresados


class Examen:
        def __init__(self, nota: float):
            self.nota = nota
        def get_nota(self):
            return self.nota

class Alumno:
    def __init__(self, nombre: str, fecha_egreso: datetime, examenes: List['Examen']):
        self.nombre = nombre
        self.fecha_egreso = fecha_egreso
        self.examenes = examenes

    def get_nombre(self):
        return self.nombre

    def get_fecha_egreso(self):
        return self.fecha_egreso

    def get_examenes(self):
        return self.examenes

class EvaluadorAlumno:
    def __init__(self):
        self.promedio = 0

    def calcular_promedio(self,alumno:Alumno):
        notas =0
        promedio = 0

        for examen in alumno.get_examenes():
            notas+=examen.get_nota()
        if len(alumno.get_examenes())>0:
            promedio = int(notas/len(alumno.get_examenes()))

        self.promedio = promedio

    def get_promedio(self):
        return self.promedio


# Ejemplo de uso
if __name__ == "__main__":
    alumno1 = Alumno("Juan", datetime.datetime(2024,12,15), [Examen(7), Examen(8), Examen(5)])
    alumno3 = Alumno('Jorge',datetime.datetime(2023,3,25),[Examen(7), Examen(10), Examen(5)])
    alumno2 = Alumno("María", None, [Examen(6), Examen(7), Examen(6)])
    carrera = Carrera()
    carrera.c_alumnos = [alumno1, alumno2,alumno3]
    carrera.listar_egresados()
