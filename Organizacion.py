from Proyecto import Proyecto
from Responsable import Responsable

class Organizacion:
    def __init__(self, nombre, responsable):
        self.nombre = nombre
        self.responsable = responsable
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
        print(f"Proyecto '{proyecto.nombre}' agregado a la organización.")

    def eliminar_proyecto(self, proyecto_id):
        proyecto = next((p for p in self.proyectos if p.id == proyecto_id), None)
        if proyecto:
            self.proyectos.remove(proyecto)
            print(f"Proyecto '{proyecto.nombre}' eliminado.")
        else:
            print(f"Proyecto con ID {proyecto_id} no encontrado.")

    def proyectos_completados(self):
        """Devuelve la cantidad de proyectos que están completos."""
        return sum(1 for p in self.proyectos if p.estado.lower() == 'completado')

    def ordenar_proyectos_por_emisiones(self):
        """Ordena los proyectos por la cantidad de emisiones reducidas en orden descendente."""
        self.proyectos.sort(key=lambda p: p.emisiones_reducidas, reverse=True)
        print("Proyectos ordenados por emisiones reducidas.")

    def calcular_total_emisiones(self):
        """Calcula la suma total de emisiones reducidas en todos los proyectos."""
        total_emisiones = sum(p.emisiones_reducidas for p in self.proyectos)
        print(f"Total de emisiones reducidas: {total_emisiones} toneladas.")

    def mostrar_informacion(self):
        """Muestra información general de la organización y sus proyectos."""
        print(f"Organización: {self.nombre}")
        print(f"Responsable: {self.responsable.nombre} {self.responsable.apellido}")
        print("Proyectos:")
        for p in self.proyectos:
            p.mostrar_informacion()

    def actualizar_estado_proyecto(self, proyecto_id, nuevo_estado):
        """Actualiza el estado de un proyecto por su ID."""
        proyecto = next((p for p in self.proyectos if p.id == proyecto_id), None)
        if proyecto:
            proyecto.cambiar_estado(nuevo_estado)
        else:
            print(f"Proyecto con ID {proyecto_id} no encontrado.")
