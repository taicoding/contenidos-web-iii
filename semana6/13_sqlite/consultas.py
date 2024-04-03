# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("institutos.db")

# Insertamos nuevos estudiantes y carreras

conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('Carlos', 'Gomez', '2001-02-10')
    """
)

conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Licenciatura en Contabilidad', 4)
    """
)

# Consultar datos de matriculación INNER JOIN
print("\nMATRICULAS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULAS.fecha 
    FROM MATRICULAS
    JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULAS.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)

# MATRICULAS:
# ('Juan', 'Perez', 'Ingeniería en Informática', '2024-01-15')
# ('María', 'Lopez', 'Licenciatura en Administración', '2024-01-30')

# Consultar datos de matriculación LEFT JOIN
print("\nMATRICULAS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT CARRERAS.nombre, ESTUDIANTES.nombre
    FROM CARRERAS
    LEFT JOIN MATRICULAS ON CARRERAS.id = MATRICULAS.carrera_id
    LEFT JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id;
    """
)
for row in cursor:
    print(row)

# MATRICULAS:
# ('Ingeniería en Informática', 'Juan')
# ('Licenciatura en Administración', 'María')
# ('Licenciatura en Contabilidad', None)

# Consultar datos de matriculación RIGHT JOIN
print("\nMATRICULAS RIGHT JOIN:")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, CARRERAS.nombre
    FROM ESTUDIANTES
    RIGHT JOIN MATRICULAS ON ESTUDIANTES.id = MATRICULAS.estudiante_id
    RIGHT JOIN CARRERAS ON MATRICULAS.carrera_id = CARRERAS.id;
    """
)
for row in cursor:
    print(row)

# MATRICULAS:
# ('Juan', 'Ingeniería en Informática')
# ('María', 'Licenciatura en Administración')
# (None, 'Licenciatura en Contabilidad')