# Patrón Factory: se encarga de crear objetos de tipo bebida
class Bebida:
    def preparar(self):
        pass

class Cafe(Bebida):
    def preparar(self):
        return "Café listo ☕"

class Te(Bebida):
    def preparar(self):
        return "Té listo 🍵"

class BebidaFactory:
    @staticmethod
    def crear_bebida(tipo):
        if tipo == "cafe":
            return Cafe()
        elif tipo == "te":
            return Te()
        else:
            return None

# Patrón Observer: los clientes esperan su pedido y son notificados
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def notificar(self, mensaje):
        print(f"{self.nombre} recibió notificación: {mensaje}")

class Cafeteria:
    def __init__(self):
        self.clientes = []

    def suscribir(self, cliente):
        self.clientes.append(cliente)

    def preparar_pedido(self, tipo):
        bebida = BebidaFactory.crear_bebida(tipo)
        if bebida:
            mensaje = bebida.preparar()
            self.notificar_clientes(mensaje)

    def notificar_clientes(self, mensaje):
        for cliente in self.clientes:
            cliente.notificar(mensaje)

# --- Simulación ---
cafeteria = Cafeteria()

# Se suscriben clientes a la notificación
cliente1 = Cliente("Ana")
cliente2 = Cliente("Luis")
cafeteria.suscribir(cliente1)
cafeteria.suscribir(cliente2)

# Se preparan pedidos
cafeteria.preparar_pedido("cafe")
cafeteria.preparar_pedido("te")
