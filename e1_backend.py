import requests
import time

"""
Prueba APIS
Ejercicio 3:

La página https://petstore.swagger.io/ proporciona la documentación sobre apis de una "PetStore".

Utilizando un software para pruebas de servicios REST realizar las siguientes pruebas, identificando las entradas, capturando las salidas, test, variables, etc, en cada uno de los siguientes casos:

Crear un usuario
Buscar el usuario creado
Actualizar el nombre y el correo del usuario
Buscar el usuario actualizado
Eliminar el usuario
"""


#---------------
# URL base de la API
base_url = "https://petstore.swagger.io/v2"

# Función para manejar la respuesta y mostrar el código de error
def handle_response(response):
    if response.status_code == 200:
        return response.json(), True, response.status_code
    else:
        return response.text, False, response.status_code

# Función para crear usuario
def create_user():
    create_user_data = [
        {
            "id": 0,
            "username": "john_doe",
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "phone": "123456789",
            "userStatus": 1
        }
    ]
    response = requests.post(f"{base_url}/user/createWithList", json=create_user_data)
    return handle_response(response)

# 1. Crear Usuario
print("1. Crear Usuario :")
data, success, status_code = create_user()
print("Respuesta:", data, "\nÉxito:", success, "\nCódigo de Estado:", status_code)
print("-" * 50)

# Función para obtener usuario
def get_user(username):
    response = requests.get(f"{base_url}/user/{username}")
    return handle_response(response)

# 2. Buscar Usuario Existente (Prueba Exitosa)
print("2. Buscar Usuario Existente (Prueba Exitosa):")
data, success, status_code = get_user("john_doe")
print("Respuesta:", data, "\nÉxito:", success, "\nCódigo de Estado:", status_code)
print("-" * 50)

# 3. Buscar Usuario Inexistente (Prueba de Error)
print("3. Buscar Usuario Inexistente (Prueba de Error):")
data, success, status_code = get_user("nonexistent_user")
print("Respuesta:", data, "\nÉxito:", success, "\nCódigo de Estado:", status_code)
print("-" * 50)

# Función para actualizar usuario
def update_user(username):
    update_user_data = {
        "id": 0,
        "username": username,
        "firstName": "Johnathan",
        "lastName": "Doe",
        "email": "johnathan.doe@example.com",
        "password": "password123",
        "phone": "123456789",
        "userStatus": 1
    }
    response = requests.put(f"{base_url}/user/{username}", json=update_user_data)
    return handle_response(response)

# 4. Actualizar Usuario Existente
print("4. Actualizar Usuario Existente:")
data, success, status_code = update_user("john_doe")
print("Respuesta:", data, "\nÉxito:", success, "\nCódigo de Estado:", status_code)
print("-" * 50)

time.sleep(2)  

# 5. Buscar Usuario Actualizado
print("5. Buscar Usuario Actualizado:")
data, success, status_code = get_user("john_doe")
print("Respuesta:", data, "\nÉxito:", success, "\nCódigo de Estado:", status_code)
print("-" * 50)

# Función para eliminar usuario
def delete_user(username):
    response = requests.delete(f"{base_url}/user/{username}")
    return handle_response(response)

# 6. Eliminar Usuario Existente
print("6. Eliminar Usuario Existente:")
data, success, status_code = delete_user("john_doe")
print("Respuesta:", data, "\nÉxito:", success, "\nCódigo de Estado:", status_code)
print("-" * 50)
