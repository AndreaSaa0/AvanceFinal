class Responsable:
    def __init__(self, dni, nombre, apellido, email, telefono):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def mostrar_informacion(self):
        print(f"\n--- Información del Responsable ---")
        print(f"DNI: {self.dni}")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")