class Proyecto:
    def __init__(self, id, nombre, tipo, ubicacion, responsable, emisiones_reducidas, energia_generada, estado):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.responsable = responsable
        self.emisiones_iniciales = emisiones_reducidas
        self.energia_generada = energia_generada
        self.estado = estado
        self.emisiones_finales = None

    def actualizar_emisiones(self, nuevas_emisiones):
        self.emisiones_iniciales = nuevas_emisiones
        print(f"Emisiones actualizadas a {nuevas_emisiones} toneladas.")

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"Estado del proyecto {self.nombre} actualizado a {nuevo_estado}.")

    def mostrar_informacion(self):
        print(f"Proyecto ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo de Energía: {self.tipo}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Responsable: {self.responsable.nombre} {self.responsable.apellido}")
        print(f"Emisiones Iniciales: {self.emisiones_iniciales} toneladas")
        if self.emisiones_finales is not None:
            print(f"Emisiones Finales: {self.emisiones_finales} toneladas")
        print(f"Energía Generada: {self.energia_generada} kWh")
        print(f"Estado: {self.estado}")