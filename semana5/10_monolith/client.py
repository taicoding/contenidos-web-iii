import requests
url = "http://localhost:8000"
# GET /posts
response = requests.get(f"{url}/posts")
print(response.text)

# POST /post
data = {
    "title": "Mi experiencia como dev",
    "content": "[Inserte experiencia aquí]"
}
headers = {'Content-type': 'application/json'}
response = requests.post(f"{url}/posts", json=data, headers=headers)
print(response.json())

# PUT /post/1
edit = {
    "title": "Mi primera publicación editada",
    "content": "¡Hola, mundo! Editado"
}
headers = {'Content-type': 'application/json'}
response = requests.put(f"{url}/posts/1", json=edit, headers=headers)
print(response.text)

# DELETE /post/1
response = requests.delete(f"{url}/posts/1")
print(response.text)