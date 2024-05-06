from flask import Blueprint, request, redirect, url_for

# Importamos la vista de usuarios
from views import user_view

# Importamos el modelo de usuario
from models.user_model import User

# Un Blueprint es un objeto que agrupa
# rutas y vistas
user_bp = Blueprint("user", __name__)


# Ruta de la página raíz redirige a la vista de usuarios
@user_bp.route("/")
def index():
    return redirect(url_for("user.list_users"))


@user_bp.route("/users")
def list_users():
    # Obtenemos todos los usuarios
    users = User.get_all()
    # Llamamos a la vista de usuarios
    return user_view.usuarios(users)


# Definimos la ruta "/users" asociada a la función registro
# que nos devuelve la vista de registro
@user_bp.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        # Obtenemos los datos del formulario
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        # Creamos un nuevo usuario
        user = User(first_name, last_name)
        # Guardamos el usuario
        user.save()
        return redirect(url_for("user.list_users"))
    # Llamamos a la vista de registro
    return user_view.registro()


# Actualizamos la información del usuario por su id
# Ya estamos en la vista de actualizar
# por lo que obtenemos los datos del formulario
# y actualizamos la información del usuario
@user_bp.route("/users/<int:id>/update", methods=["GET", "POST"])
def update_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    if request.method == "POST":
        # Obtenemos los datos del formulario
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        # Actualizamos los datos del usuario
        user.first_name = first_name
        user.last_name = last_name
        # Guardamos los cambios
        user.update()
        return redirect(url_for("user.list_users"))
    return user_view.actualizar(user)


@user_bp.route("/users/<int:id>/delete")
def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    user.delete()
    return redirect(url_for("user.list_users"))
