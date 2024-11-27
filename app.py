from flask import Flask
from src.routes.animales import animales_bp

app = Flask(__name__)

# Registrar el blueprint
app.register_blueprint(animales_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Bienvenido a la API de Animales. Usa /api/como_hace/<animal> para consultar cómo hacen los animales."

# Imprimir el mapa de rutas
print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
