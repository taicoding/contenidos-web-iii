from flask import Flask
from controllers.animal_controller import animal_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database import db

app = Flask(__name__)

# Configura la URL de la documentación OpenAPI
SWAGGER_URL = "/api/docs"  # Ruta para servir Swagger UI
API_URL = "/static/openapi.yaml"  # Ruta de tu archivo OpenAPI/Swagger
# Inicializa el Blueprint de Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Zoológico API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zoo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa la base de datos
db.init_app(app)

# Registra el blueprint de animales en la aplicación
app.register_blueprint(animal_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
    db.create_all()

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run(debug=True)
