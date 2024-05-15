from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from flask_jwt_extended import get_jwt_header
import json


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 401

    return wrapper


def roles_required(roles=[]):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                verify_jwt_in_request()
                current_user = get_jwt_identity()
                print(current_user)
                user_roles = json.loads(current_user.get("roles", []))
                print(user_roles)
                if not set(roles).intersection(user_roles):
                    return jsonify({"error": "Acceso no autorizado para este rol"}), 403
                return fn(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 401

        return wrapper

    return decorator


def get_current_user_roles():
    claims = get_jwt_header()
    if claims and "roles" in claims:
        print(claims)
        return claims["roles"]
    else:
        return None
