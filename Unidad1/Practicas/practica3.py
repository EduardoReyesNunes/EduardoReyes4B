import os
os.system("cls")
#Practica 3 intriduccion al pilomosfirsmo
# simula un sistema de cobro con multiples opciones de pago
class pago_tarjeta:
    def procesar_pago(self,cantidad):
        return f"procesando el pago de {cantidad} con tarjeta"
    
class transferencia:
    def procesar_pago(self,cantidad):
        return f"procesando pago por metodo de transferencia de la cantidad {cantidad}"
class deposito:
    def procesar_pago(self,cantidad):
        return f"procesando pago por metodo de deposito de la cantidad {cantidad}"
class paypal:
    def procesar_pago(self,cantidad):
        return f"procesando pago de {cantidad} pesos mediante paypal"
    
#INstancias

metodos_de_pago = [pago_tarjeta(),transferencia(),deposito(),paypal()]

pago1=pago_tarjeta()
pago2=transferencia()
pago3=deposito()
pago4=paypal()

print(pago1.procesar_pago(100))
print(pago2.procesar_pago(500))
print(pago3.procesar_pago(45))
print(pago4.procesar_pago(2000))

#parte 2 


class NotificacionEmail:
    def enviar_notificacion(self, mensaje):
        return f"Enviando notificación por Email: '{mensaje}'"

class NotificacionSMS:
    def enviar_notificacion(self, mensaje):
        return f"Enviando notificación por SMS: '{mensaje}'"

class NotificacionPush:
    def enviar_notificacion(self, mensaje):
        return f"Enviando notificación Push: '{mensaje}'"

# ---

# Instancias de las clases de notificación
tipos_de_notificacion = [NotificacionEmail(), NotificacionSMS(), NotificacionPush()]

# Mensajes de ejemplo
mensaje_ejemplo_1 = "Su pedido ha sido enviado."
mensaje_ejemplo_2 = "Recordatorio: Tienes una reunión en 15 minutos."
mensaje_ejemplo_3 = "¡Oferta especial solo para ti!"

notificacion1 = NotificacionEmail()
notificacion2 = NotificacionSMS()
notificacion3 = NotificacionPush()

print(notificacion1.enviar_notificacion(mensaje_ejemplo_1))
print(notificacion2.enviar_notificacion(mensaje_ejemplo_2)) 
print(notificacion3.enviar_notificacion(mensaje_ejemplo_3))
