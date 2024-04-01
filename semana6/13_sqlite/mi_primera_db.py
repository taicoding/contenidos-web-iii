# Importar módulo sqlite3
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("instituto.db")

# Crear tablas
conn.execute(
    """CREATE TABLE Carreras
                (id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                duracion INTEGER NOT NULL);"""
)

conn.execute(
    """CREATE TABLE Estudiantes
                (id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                fecha_nacimiento DATE NOT NULL);"""
)

conn.execute(
    """CREATE TABLE Matriculacion
                (id INTEGER PRIMARY KEY,
                estudiante_id INTEGER NOT NULL,
                carrera_id INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                FOREIGN KEY (estudiante_id) REFERENCES Estudiantes(id),
                FOREIGN KEY (carrera_id) REFERENCES Carreras(id));"""
)

# Insertar datos de carreras
conn.execute(
    "INSERT INTO Carreras (nombre, duracion) VALUES ('Ingeniería en Informática', 5)"
)
conn.execute(
    "INSERT INTO Carreras (nombre, duracion) VALUES ('Licenciatura en Administración', 4)"
)

# Insertar datos de estudiantes
conn.execute(
    "INSERT INTO Estudiantes (nombre, fecha_nacimiento) VALUES ('Juan', '2000-05-15')"
)
conn.execute(
    "INSERT INTO Estudiantes (nombre, fecha_nacimiento) VALUES ('María', '1999-08-20')"
)

# Insertar datos de matriculación
conn.execute(
    "INSERT INTO Matriculacion (estudiante_id, carrera_id, fecha) VALUES (1, 1, '2024-01-15')"
)
conn.execute(
    "INSERT INTO Matriculacion (estudiante_id, carrera_id, fecha) VALUES (2, 2, '2024-01-20')"
)

# Consultar datos
print("Carreras:")
cursor = conn.execute("SELECT * FROM Carreras")
for row in cursor:
    print(row)

print("\nEstudiantes:")
cursor = conn.execute("SELECT * FROM Estudiantes")
for row in cursor:
    print(row)

print("\nMatriculación:")
cursor = conn.execute(
    """SELECT Estudiantes.nombre, Carreras.nombre, Matriculacion.fecha 
    FROM Matriculacion 
    JOIN Estudiantes ON Matriculacion.estudiante_id = Estudiantes.id 
    JOIN Carreras ON Matriculacion.carrera_id = Carreras.id"""
)
for row in cursor:
    print(row)

# Cerrar conexión
conn.close()
