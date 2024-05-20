# render_template() es una función de Flask
# que renderiza un template de Jinja2.
from flask import render_template
from flask_login import current_user


# La función `usuarios` recibe una lista de
# usuarios y renderiza el template `usuarios.html`
def usuarios(users):
    return render_template(
        "usuarios.html",
        users=users,
        title="Lista de usuarios",
        current_user=current_user,
    )


# La función `registro` renderiza el
# template `registro.html`
def registro():
    return render_template(
        "registro.html", title="Registro de usuarios", current_user=current_user
    )


# La función `actualizar` recibe un usuario
# y renderiza el template `actualizar.html`
def actualizar(user):
    return render_template(
        "actualizar.html",
        title="Actualizar usuario",
        user=user,
        current_user=current_user,
    )


# La función `login` renderiza el template `login.html`
def login():
    return render_template(
        "login.html", title="Inicio de sesión", current_user=current_user
    )


# La función `perfil` renderiza el template `perfil.html`
def perfil(user):
    return render_template(
        "profile.html", title="Perfil de usuario", current_user=current_user, user=user
    )
