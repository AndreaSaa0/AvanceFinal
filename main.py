# main.py
from Responsable import Responsable
from Proyecto import Proyecto
from Organizacion import Organizacion

def mostrar_menu():
    print("\n---- Bienvenido a GreenTech Global -----")
    print("\n---- Sistema de Gestión y Monitoreo ----")
    print("\n----------- ¡MENÚ PRINCIPAL! -----------")
    print("1. Crear un nuevo proyecto")
    print("2. Mostrar información de un proyecto")
    print("3. Actualizar el estado de un proyecto")
    print("4. Eliminar un proyecto de la organización")
    print("5. Ordenar proyectos por impacto (emisiones reducidas)")
    print("6. Calcular total de emisiones reducidas")
    print("7. Determinar proyectos completados")
    print("8. Mostrar información del responsable")
    print("9. Salir")

def crear_nuevo_proyecto(organizacion):
    id = int(input("Introduce el ID del proyecto: "))
    nombre = input("Introduce el nombre del proyecto: ")
    tipo = input("Introduce el tipo de energía: ")
    ubicacion = input("Introduce la ubicación del proyecto: ")
    
    # Crear el responsable dentro de esta función
    responsable_nombre = input("Introduce el nombre del responsable: ")
    responsable_apellido = input("Introduce el apellido del responsable: ")
    responsable_dni = input("Introduce el DNI del responsable: ")
    responsable_email = input("Introduce el email del responsable: ")
    responsable_telefono = input("Introduce el teléfono del responsable: ")
    
    responsable = Responsable(responsable_dni, responsable_nombre, responsable_apellido, responsable_email, responsable_telefono)
    
    emisiones_reducidas = float(input("Introduce las emisiones reducidas (toneladas): "))
    energia_generada = float(input("Introduce la energía generada (kWh): "))
    estado = input("Introduce el estado del proyecto (En proceso, Completado, etc.): ")

    nuevo_proyecto = Proyecto(id, nombre, tipo, ubicacion, responsable, emisiones_reducidas, energia_generada, estado)
    organizacion.agregar_proyecto(nuevo_proyecto)

def mostrar_informacion_proyecto(organizacion):
    proyecto_id = int(input("Introduce el ID del proyecto para mostrar información: "))
    proyecto = next((p for p in organizacion.proyectos if p.id == proyecto_id), None)
    if proyecto:
        proyecto.mostrar_informacion()
    else:
        print(f"Proyecto con ID {proyecto_id} no encontrado.")

def actualizar_estado_proyecto(organizacion):
    proyecto_id = int(input("Introduce el ID del proyecto: "))
    nuevo_estado = input("Introduce el nuevo estado del proyecto (En proceso, Completado, etc.): ")
    organizacion.actualizar_estado_proyecto(proyecto_id, nuevo_estado)

def mostrar_info_responsable(organizacion):
    print("\n--- Información del Responsable ---")
    print(f"Nombre del responsable: {organizacion.responsable.nombre} {organizacion.responsable.apellido}")
    organizacion.responsable.mostrar_informacion()

def ejecutar_menu():
    # Crear responsable y organización
    responsable1 = Responsable('12345678A', 'Andrea', 'Saa', 'andrea@gmail.com', '1234567890')
    organizacion = Organizacion('Eco Energía', responsable1)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-9): ")

        if opcion == '1':
            crear_nuevo_proyecto(organizacion)
        elif opcion == '2':
            mostrar_informacion_proyecto(organizacion)
        elif opcion == '3':
            actualizar_estado_proyecto(organizacion)
        elif opcion == '4':
            proyecto_id = int(input("Introduce el ID del proyecto a eliminar: "))
            organizacion.eliminar_proyecto(proyecto_id)
        elif opcion == '5':
            organizacion.ordenar_proyectos_por_emisiones()
        elif opcion == '6':
            organizacion.calcular_total_emisiones()
        elif opcion == '7':
            print(f"Proyectos completados: {organizacion.proyectos_completados()}")
        elif opcion == '8':
            mostrar_info_responsable(organizacion)
        elif opcion == '9':
            print("¡Gracias por usar nuestro Sistema de Gestión y Monitoreo!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 9.")

# Ejecutar el programa
if __name__ == "__main__":
    ejecutar_menu()