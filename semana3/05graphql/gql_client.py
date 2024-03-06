import requests

# Definir la consulta GraphQL
query = """
    {
        estudiante(id: 1, nombre: "Jose"){
            nombre
        }
    }
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)
