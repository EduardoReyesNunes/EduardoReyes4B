import os

class Ticket:
    def __init__(self, id, tipo, prioridad, estado="pendiente"):
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = estado

    def ticket_imp(self):
        return (
            "----------------------------------\n"
            f"        TICKET #{self.id}\n"
            "----------------------------------\n"
            f"Tipo      : {self.tipo}\n"
            f"Prioridad : {self.prioridad}\n"
            f"Estado    : {self.estado}\n"
            "----------------------------------"
        )

class Empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def trabajar_en_ticket(self, ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")

class Desarrollador(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "software":
            ticket.estado = "resuelto"
            print(f"El desarrollador {self.nombre} ha resuelto el ticket {ticket.id}")
        else:
            print(f"El desarrollador {self.nombre} no puede resolver el ticket {ticket.id} de tipo {ticket.tipo}")

class Tester(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "prueba":
            ticket.estado = "resuelto"
            print(f"El tester {self.nombre} ha resuelto el ticket {ticket.id}")
        else:
            print(f"El tester {self.nombre} no puede resolver el ticket {ticket.id} de tipo {ticket.tipo}")

class ProjectManager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"El Project Manager {self.nombre} asigna el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)

def main():
    wait = True
    tickets = []
    empleados = []
    
    # Crear un PM por defecto para las asignaciones
    pm1 = ProjectManager("Ana", "PM")
    empleados.append(pm1)
    
    while wait:
        os.system('cls')
        opcion = input("Menu inicial\n1. Crear ticket\n2. Crear empleado\n3. Ver tickets\n4. Asignar ticket\n5. Salir\nSeleccione una opcion: ")
        
        match opcion:
            case "1":
                print("Creando ticket...")
                id = len(tickets) + 1
                tipo = input("Ingrese tipo del ticket (software/prueba): ").lower()
                while tipo not in ["software", "prueba"]:
                    print("Tipo inválido. Debe ser 'software' o 'prueba'")
                    tipo = input("Ingrese tipo del ticket (software/prueba): ").lower()
                
                prioridad = input("Ingrese prioridad del ticket (alta/media/baja): ").lower()
                while prioridad not in ["alta", "media", "baja"]:
                    print("Prioridad inválida. Debe ser 'alta', 'media' o 'baja'")
                    prioridad = input("Ingrese prioridad del ticket (alta/media/baja): ").lower()
                
                new_ticket = Ticket(id, tipo, prioridad)
                tickets.append(new_ticket)
                print("Ticket creado exitosamente!")
                input("Presione Enter para continuar...")
                
            case "2":
                print("Creando empleado...")
                nombre = input("Ingrese nombre del empleado: ")
                puesto = input("Ingrese puesto del empleado (Desarrollador/Tester/PM): ").lower()
                
                if puesto == "desarrollador":
                    new_empleado = Desarrollador(nombre, puesto)
                elif puesto == "tester":
                    new_empleado = Tester(nombre, puesto)
                elif puesto == "pm":
                    new_empleado = ProjectManager(nombre, puesto)
                else:
                    new_empleado = Empleado(nombre, puesto)
                
                empleados.append(new_empleado)
                print("Empleado creado exitosamente!")
                input("Presione Enter para continuar...")
                
            case "3":
                print("Mostrando tickets...")
                if not tickets:
                    print("No hay tickets creados.")
                else:
                    for ticket in tickets:
                        print(ticket.ticket_imp())
                        print()
                input("Presione Enter para continuar...")
                
            case "4":
                if not tickets:
                    print("No hay tickets para asignar.")
                    input("Presione Enter para continuar...")
                    continue
                    
                if len(empleados) <= 1:  # Solo está el PM por defecto
                    print("No hay empleados para asignar tickets.")
                    input("Presione Enter para continuar...")
                    continue
                    
                print("Asignando ticket...")
                print("Tickets disponibles:")
                for ticket in tickets:
                    print(ticket.ticket_imp())
                    print()

                try:
                    id_ticket = int(input("Ingrese ID del ticket a asignar: "))
                    ticket_asignar = None
                    for ticket in tickets:
                        if ticket.id == id_ticket:
                            ticket_asignar = ticket
                            break
                    
                    if ticket_asignar is None:
                        print("Ticket no encontrado.")
                        input("Presione Enter para continuar...")
                        continue
                    
                    print("\nEmpleados disponibles:")
                    for i, empleado in enumerate(empleados):
                        if empleado.puesto != "PM":  # No mostrar PMs para asignación
                            print(f"{i+1}. {empleado.nombre} - {empleado.puesto}")
                    
                    try:
                        opcion_empleado = int(input("Seleccione el número del empleado: ")) - 1
                        if 0 <= opcion_empleado < len(empleados) and empleados[opcion_empleado].puesto != "PM":
                            empleado_asignar = empleados[opcion_empleado]
                            pm1.asignar_ticket(ticket_asignar, empleado_asignar)
                        else:
                            print("Selección inválida.")
                    except (ValueError, IndexError):
                        print("Selección inválida.")
                        
                except ValueError:
                    print("ID debe ser un número.")
                
                input("Presione Enter para continuar...")
                
            case "5":
                print("Saliendo...")
                wait = False
                
            case _:
                print("Opción inválida. Intente nuevamente.")
                input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()