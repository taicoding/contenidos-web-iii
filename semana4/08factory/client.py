import requests
url = "http://localhost:8000/"
headers = {"Content-Type": "application/json"}

package = {"weight": 2, "destination": "123 Calle Principal"}
vehicle_type = "motorcycle"
data = {"vehicle_type": vehicle_type, "package": package}
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print("Delivery successfully scheduled.")
else:
    print("Error scheduling delivery:", response.text)
    
package = {"weight": 0.5, "destination": "456 Calle Secundaria"}
vehicle_type = "drone"
data = {"vehicle_type": vehicle_type, "package": package}
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print("Delivery successfully scheduled.")
else:
    print("Error scheduling delivery:", response.text)
