class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def hacer(self):
        return f"El perro {self.nombre} dice 'guau guau' y mueve la cola."
