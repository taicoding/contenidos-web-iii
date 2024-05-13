from flask import Blueprint, request, jsonify
from models.animal_model import Animal
from views.animal_view import render_animal_list, render_animal_detail
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps

# Crear un blueprint para el controlador de animales
animal_bp = Blueprint("animal", __name__)


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 401

    return wrapper


# Ruta para obtener la lista de animales
@animal_bp.route("/animals", methods=["GET"])
@jwt_required
def get_animals():
    animals = Animal.get_all()
    return jsonify(render_animal_list(animals))


# Ruta para obtener un animal específico por su ID
@animal_bp.route("/animals/<int:id>", methods=["GET"])
@jwt_required
def get_animal(id):
    animal = Animal.get_by_id(id)
    if animal:
        return jsonify(render_animal_detail(animal))
    return jsonify({"error": "Animal no encontrado"}), 404


# Ruta para crear un nuevo animal
@animal_bp.route("/animals", methods=["POST"])
@jwt_required
def create_animal():
    data = request.json
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")

    # Validación simple de datos de entrada
    if not name or not species or age is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo animal y guardarlo en la base de datos
    animal = Animal(name=name, species=species, age=age)
    animal.save()

    return jsonify(render_animal_detail(animal)), 201


# Ruta para actualizar un animal existente
@animal_bp.route("/animals/<int:id>", methods=["PUT"])
@jwt_required
def update_animal(id):
    animal = Animal.get_by_id(id)

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    data = request.json
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")

    # Actualizar los datos del animal
    animal.update(name=name, species=species, age=age)

    return jsonify(render_animal_detail(animal))


# Ruta para eliminar un animal existente
@animal_bp.route("/animals/<int:id>", methods=["DELETE"])
@jwt_required
def delete_animal(id):
    animal = Animal.get_by_id(id)

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    # Eliminar el animal de la base de datos
    animal.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
