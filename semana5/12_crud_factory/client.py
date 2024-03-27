import requests
import json

url = "http://localhost:8000/deliveries"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_vehicle_data = {
    "vehicle_type": "drone",
    "plate_number": "ABC-123",
    "capacity": 10
}
response = requests.post(url=url, json=new_vehicle_data, headers=headers)
print(response.json())

new_vehicle_data = {
    "vehicle_type": "motorcycle",
    "plate_number": "ZTE-204",
    "capacity": 25
}
response = requests.post(url=url, json=new_vehicle_data, headers=headers)
print(response.json())


# GET /deliveries
response = requests.get(url=url)
print(response.json())

# PUT /deliveries/{vehicle_id}
vehicle_id_to_update = 1
updated_vehicle_data = {
    "plate_number": "XYZ789"
}
response = requests.put(f"{url}/{vehicle_id_to_update}", json=updated_vehicle_data)
print("Vehículo actualizado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())

# DELETE /deliveries/{vehicle_id}
vehicle_id_to_delete = 1
response = requests.delete(f"{url}/{vehicle_id_to_delete}")
print("Vehículo eliminado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())