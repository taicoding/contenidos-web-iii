import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Crear un nuevo animal
url = f"{BASE_URL}/animals"
nuevo_animal = {"name": "León", "species": "Felino", "age": 5}
response = requests.post(url, json=nuevo_animal, headers=headers)
print("Creando un nuevo animal:")
print(response.json())

# Crear el segundo animal
animal_2 = {"name": "Cocodrilo", "species": "Reptil", "age": 8}
response = requests.post(url, json=animal_2, headers=headers)
print("\nCreando el segundo animal:")
print(response.json())

# Obtener la lista de todos los animales
url = f"{BASE_URL}/animals"
response = requests.get(url, headers=headers)
print("\nLista de animales:")
print(response.json())

# Obtener un animal específico por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/animals/1"
response = requests.get(url, headers=headers)
print("\nDetalles del animal con ID 1:")
print(response.json())

# Actualizar un animal existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/animals/1"
datos_actualizacion = {"name": "Tigre", "species": "Felino", "age": 4}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando el animal con ID 1:")
print(response.json())

# Eliminar un animal existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/animals/1"
response = requests.delete(url, headers=headers)
print("\nEliminando el animal con ID 1:")
if response.status_code == 204:
    print(f"Animal con ID 1 eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")
