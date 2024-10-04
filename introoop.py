
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}.")

    def saludar_a(self, otra_persona):
        print(f"{self.nombre}: ¡Hola, {otra_persona.nombre}! ¿Cómo estás?")

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

# Creando instancias de la clase Persona
persona1 = Persona("Juan", 25, "masculino")
persona2 = Persona("Victor", 10, "masculino")
persona3 = Persona("Brenda", 21, "femenino")

# Usando los métodos de las instancias
persona1.presentarse()         # Salida: Hola, mi nombre es Juan, tengo 25 años y soy masculino.
persona1.cumplir_anios()       # Salida: Juan ahora tiene 26 años.
persona1.cambiar_nombre("Carlos")  # Salida: Mi nuevo nombre es Carlos.
persona2.presentarse()         # Salida: Hola, mi nombre es Victor, tengo 10 años y soy masculino.
persona1.saludar_a(persona2)
persona3.presentarse()
persona2.saludar_a(persona3)
print(persona1.es_mayor_de_edad())
persona1.detalles()
