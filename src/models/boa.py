class BoaConstrictor:
    def __init__(self, nombre, longitud, peso):
        self.nombre = nombre
        self.longitud = longitud
        self.peso = peso

    def hacer(self):
        return f"La boa constrictor {self.nombre} se desliza silenciosamente y se enrolla para cazar."
