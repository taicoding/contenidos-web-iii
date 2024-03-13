import requests

url = "http://localhost:8000/"

# GET /player
response = requests.request(method="GET", url=url + "player")
print(response.text)

# POST /player/damage
response = requests.request(
    method="POST", url=url + "player/damage", json={"damage": 10}
)
print(response.text)