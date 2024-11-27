class Gato:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def hacer(self):
        return f"El gato {self.nombre} dice 'miau' y le gusta ronronear."
