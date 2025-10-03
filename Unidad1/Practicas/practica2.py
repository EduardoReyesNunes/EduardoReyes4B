#practica 2 atributos publicos y privados

class persona:
    def __init__(self, nombre, edad): #constructor de una clase
        self.nombre = nombre
        self.edad = edad
        self.__cuenta= None

    def presentarse(self):
        print(f"{self.nombre} tiene {self.edad} anios")
    
    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} anos")

    def asignar_cuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ha asignado una cuenta bancaria.")

    def consultar_saldo(self):
        if self.__cuenta:
            print(f"El saldo de la cuenta de {self.nombre} es: {self.__cuenta.saldo()}")
        else:
            print(f"{self.nombre} no tiene una cuenta bancaria asignada.")

class cuenta_bancaria:
    def __init__(self, numero_cuenta, saldo_inicial):
        self.numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Se han depositado {monto}. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto<= self.__saldo:
            self.__saldo -= monto
            print(f"Se han retirado {monto}. Nuevo saldo: {self.__saldo}")
        else:
            print("Monto invalido o saldo insuficiente.")

    def saldo(self):
        return self.__saldo

persona1 = persona("Genesis",18)
persona1.presentarse()
persona1.cumplir_anios()

cuenta1 = cuenta_bancaria("123456789", 1000)
persona1.asignar_cuenta(cuenta1)

persona1.consultar_saldo()

cuenta1.depositar(200)
cuenta1.retirar(150)

#class cuenta_bancaria:
   