# render_template() es una función de Flask
# que renderiza un template de Jinja2.
from flask import render_template


# La función `usuarios` recibe una lista de
# usuarios y renderiza el template `usuarios.html`
def usuarios(users):
    return render_template("usuarios.html", users=users)


# La función `registro` renderiza el
# template `registro.html`
def registro():
    return render_template("registro.html")
