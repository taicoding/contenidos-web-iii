from app.database import db


# Define la clase `Animal` que hereda de `db.Model`
# `Animal` representa la tabla `animals` en la base de datos
class Animal(db.Model):
    __tablename__ = "animals"

    # Define las columnas de la tabla `animals`
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # Inicializa la clase `Animal`
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    # Guarda un animal en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Animal.query.all()

    # Obtiene un animal por su ID
    @staticmethod
    def get_by_id(id):
        return Animal.query.get(id)

    # Actualiza un animal en la base de datos
    def update(self, name=None, species=None, age=None):
        if name is not None:
            self.name = name
        if species is not None:
            self.species = species
        if age is not None:
            self.age = age
        db.session.commit()

    # Elimina un animal de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
