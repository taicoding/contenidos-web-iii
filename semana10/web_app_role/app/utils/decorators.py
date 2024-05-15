from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user


def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or not current_user.has_role(role):
                flash("No tienes permisos para acceder a esta página.", "error")
                # Redirige a la misma página
                return redirect(url_for("user.profile", id=current_user.id))
            return f(*args, **kwargs)

        return decorated_function

    return decorator
