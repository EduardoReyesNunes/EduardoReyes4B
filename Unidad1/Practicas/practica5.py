# practica 5 patrones de diseño

class logger:
# creamos un atributo de clase donde se guardara la instancia
    _instance = None
     
    def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__new__(cls) #creamos una instancia de logger agregando un atributo archivo que apunte
                #a un archivo fisico
                cls._instance.archivo = open("app.log", "a")
            return cls._instance
    
    def log(self, mensaje):
        self.archivo.write(mensaje)
        self.archivo.flush() #para que se guarde inmediatamente en el archivo
logger1 = logger()
logger2 = logger()

logger1.log("inicio de secion en la aplicacion\n")
logger2.log("El usuario se autentico correctamente")
print(logger1 is logger2) #true, ambas variables apuntan a la misma instancia

class presidente:
    _instance = None
    
    def __new__(cls, nombre):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nombre = nombre
            cls._instance.historial = []
        return cls._instance
    
    def accion(self, evento):
        evento = f"{self.nombre} {evento}"
        self.historial.append(evento)
        print(evento)
                

p1 = presidente("AMLO")
p2 = presidente("EPN") 
p3 = presidente("fox")

p1.accion("gano las elecciones")
p2.accion("firmo un acuerdo")
p3.accion("declaro la guerra")

print("historial del presidente")
print(p1.historial)

print(p1 is p2 is p3) #true, todas las variables apuntan a la misma instancia

# Cerramos el archivo de log para liberar el recurso
logger1.archivo.close()

#1 Que pasaria si eliminamos la verificacion if cls._instance is None: en el metodo new
# R= Se crearian nuevas instancias cada vez que se llame a la clase, perdiendo el comportamiento singleton
#2 Que significa el true en p1 is p2 is p3 en el contexto del patron singleton
# R= Significa que todas las variables apuntan a la misma instancia de la clase presidente
#3 Es buena idea usar el metodo singelton para todo lo que sea global? menciona ejemplos donde sea recomendable y donde no
# R= No es buena idea usar singleton para todo lo que sea global, ya que puede generar dependencias innecesarias y dificultar las pruebas unitarias.