# Importamos la biblioteca requests para hacer peticiones HTTP
import requests

# Definimos la URL del servicio al que vamos a hacer la petición
url = "http://localhost:8000/delivery"

# Definimos los encabezados HTTP que vamos a enviar con la petición
headers = {"Content-Type": "application/json"}

# Definimos el tipo de vehículo como "motorcycle"
vehicle_type = "motorcycle"
data = {"vehicle_type": vehicle_type}

# Hacemos una petición POST a la URL con los datos y encabezados definidos
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print("Error scheduling delivery:", response.text)

# Cambiamos el tipo de vehículo a "drone"
vehicle_type = "drone"
data = {"vehicle_type": vehicle_type}

# Hacemos otra petición POST a la URL con los nuevos datos y los mismos encabezados
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print("Error scheduling delivery:", response.text)