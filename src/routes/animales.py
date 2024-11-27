from flask import Blueprint, jsonify
from src.models.gato import Gato
from src.models.perro import Perro
from src.models.huron import Huron
from src.models.boa import BoaConstrictor

animales_bp = Blueprint('animales', __name__)

# Instanciar los animales
gato = Gato("Whiskers", 3, "Siames")
perro = Perro("Rex", 5, "Labrador")
huron = Huron("Slinky", 2, "Blanco")
boa = BoaConstrictor("Squeezy", 2.5, 15)

@animales_bp.route('/como_hace/<animal>', methods=['GET'])
def como_hace(animal):
    # Crear un diccionario de animales
    animales = {
        "gato": gato.hacer(),
        "perro": perro.hacer(),
        "huron": huron.hacer(),
        "boa": boa.hacer(),
    }

    # Verificar si el animal existe en el diccionario (insensible a mayúsculas)
    resultado = animales.get(animal.lower())
    if resultado:
        return jsonify({"mensaje": resultado})
    else:
        return jsonify({"error": "Animal no encontrado"}), 404
