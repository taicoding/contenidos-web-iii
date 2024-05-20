from flask import render_template
from flask_login import current_user


# La función `list_animals` recibe una lista de
# animales y renderiza el template `animales.html`
def list_animals(animals):
    return render_template(
        "animals.html",
        animals=animals,
        title="Lista de animales",
        current_user=current_user,
    )


# La función `create_animal` renderiza el
# template `create_animal.html` o devuelve un JSON
# según la solicitud
def create_animal():
    return render_template(
        "create_animal.html", title="Crear Animal", current_user=current_user
    )


# La función `update_animal` recibe un animal
# y renderiza el template `update_animal.html`
def update_animal(animal):
    return render_template(
        "update_animal.html",
        title="Editar Animal",
        animal=animal,
        current_user=current_user,
    )
