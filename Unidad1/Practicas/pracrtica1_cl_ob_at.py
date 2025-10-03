# Practica 1 Clase Objetos y Atributos

#una clase es una plantilla o un molde
#que define como sera un objeto

class persona:
    def __init__(self, nombre, edad): #constructor de una clase
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"{self.nombre} tiene {self.edad} anios")
    
    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} anos")
# un objeto es un aistancia creada a partir de una clase

estudiante1 = persona("eduardo", 19) #creacion de un objeto
estudiante2 = persona("Genesis",18)

estudiante1.presentarse()
estudiante2.presentarse()

# paso 1    agregar metodo cumplir anios

estudiante1.cumplir_anios()
estudiante2.cumplir_anios()

#INSTANCIA

#cada objeto creado de una clase es una instancia de esa clase
#podemos crear vacias instancias  que coexistasn con sus propios datos
# objeto = instancia de la clase
# cada ves que se crea un objeto con clase() se obtiene una instancia independiente
#cada instancia tiene sus prios datos aunqye vengan de la misma clase

#ABSTARCCION

#Es representar solo lo inportante del mundo real, ocultando detalles inecesarios.

class automovil:
    def __init__(self, marca):
        self.marca= marca
        
    def arrancar(self):
        print(f"{self.marca} arranco")

auto1= automovil("ssc")

auto1.arrancar()


    # Crear una clase mascotas
    # 1. crear clase
    # 2. agregar minimo 4 atributos
    # 3. definir al menos 4 metodos diferentes
    # 4. crear 2 instancias de la clase 
    # 5. llamar los metodos y aplicar la abstraccion

    # Clase Autos Deportivos
class AutoDeportivo:
    def __init__(self, marca, modelo, potencia, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.velocidad_maxima = velocidad_maxima
    
    def acelerar(self):
        print(f"{self.marca} {self.modelo} está acelerando")
    

    def frenar(self):
        print(f"{self.marca} {self.modelo} está frenando")
    

    def mostrar_info(self):
        print(f"Auto: {self.marca} {self.modelo}")
        print(f"Potencia: {self.potencia} HP")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
    
   
    def encender(self):
        encender= input("deseas encender el carro? (s/n)")
        if encender=="s":
            print(f"{self.marca} {self.modelo} encendido")
        else:
            print(f"No se encendio el vehiculo {self.modelo}")

#instancias
auto1 = AutoDeportivo("Ferrari", "F8", 720, 340)
auto2 = AutoDeportivo("Lamborghini", "Huracan", 640, 325)


print("Ferrari")
auto1.mostrar_info()
auto1.encender()
auto1.acelerar()
auto1.frenar()

print("\n\nLamborgini")
auto2.mostrar_info()
auto2.encender()
auto2.acelerar()
auto2.frenar()

