from flask import Blueprint, request, jsonify
from models.animal_model import Animal
from views.animal_view import render_animal_list, render_animal_detail
from utils.decorators import jwt_required, roles_required

# Crear un blueprint para el controlador de animales
animal_bp = Blueprint("animal", __name__)


# Ruta para obtener la lista de animales
@animal_bp.route("/animals", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_animals():
    animals = Animal.get_all()
    return jsonify(render_animal_list(animals))


# Ruta para obtener un animal específico por su ID
@animal_bp.route("/animals/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_animal(id):
    animal = Animal.get_by_id(id)
    if animal:
        return jsonify(render_animal_detail(animal))
    return jsonify({"error": "Animal no encontrado"}), 404


# Ruta para crear un nuevo animal
@animal_bp.route("/animals", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
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
@roles_required(roles=["admin"])
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
@roles_required(roles=["admin"])
def delete_animal(id):
    animal = Animal.get_by_id(id)

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    # Eliminar el animal de la base de datos
    animal.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
