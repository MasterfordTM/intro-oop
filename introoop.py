class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"Hola, perro infiel  mi nombre es  {self.nombre}, tengo {self.edad} años y soy {self.genero}.")

    def pasarsaludo(self, sal , lol ):
        print(f"oooo oli,{self.nombre}")

    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años.")

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print(f"Mi nuevo nombre es {self.nombre}.")

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def detalles(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}")

# Creando una instancia de la clase Persona
persona1 = Persona("Juan", 25, "masculino")
persona2 = Persona("vitor",10,"hombre")
persona3 = Persona("brenda",21 ,"femenino")

# Usando los métodos de la instancia
persona1.presentarse()         # Salida: Hola, soy Juan, tengo 25 años y soy masculino.
persona1.cumplir_anios()       # Salida: Juan ahora tiene 26 años.
persona1.cambiar_nombre("Carlos")  # Salida: Mi nuevo nombre es Carlos.
persona2.presentarse()
persona1.pasarsaludo("victor","brenda")
persona3.presentarse()
print(persona1.es_mayor_de_edad())  # Salida: True
persona1.detalles()            # Salida: Nombre: Carlos, Edad: 26, Género: masculino
