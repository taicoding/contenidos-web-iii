from flask import Flask
from flask_login import LoginManager

# Importamos el controlador de usuarios
from controllers import user_controller

# Importamos el controlador de animales
from controllers import animal_controller

# Importamos la base de datos
from database import db
from models.user_model import User

# Inicializa la aplicación Flask
app = Flask(__name__)
# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zoo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "clave-secreta"
# Configuración de Flask-Login
login_manager = LoginManager()
# Especifica la ruta de inicio de sesión
login_manager.login_view = "user.login"
login_manager.init_app(app)


# Función para cargar un usuario basado en su ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Inicializa `db` con la aplicación Flask
db.init_app(app)
# Registra el Blueprint de usuarios
app.register_blueprint(user_controller.user_bp)
app.register_blueprint(animal_controller.animal_bp)

if __name__ == "__main__":
    # Crea las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True)
