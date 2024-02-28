import requests

url = "http://localhost:8000/"
# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# GET elimina todos los estudiantes por la ruta /eliminar_estudiante
ruta_eliminar = url + "eliminar_estudiante"
eliminar_response = requests.request(method="GET"
                                , url=ruta_eliminar)
print(eliminar_response.text)

# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", 
                                url=ruta_post, 
                                json=nuevo_estudiante)
print(post_response.text)

# GET consulta a la ruta /buscar_estudiante_id/{id}
ruta_filtrar_nombre = url + "buscar_estudiante_id/1"
filtrar_nombre_response = requests.request(method="GET", 
                                url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)

# POST actualiza un estudiante por la ruta /actualizar_estudiante
ruta_actualizar = url + "actualizar_estudiante"
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
actualizar_response = requests.request(
    method="POST", url=ruta_actualizar, 
    json=estudiante_actualizado
)
print(actualizar_response.text)
