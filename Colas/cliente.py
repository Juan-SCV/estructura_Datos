import requests
import random

url = 'https://humble-guide-7v7xjpwqxp9hjww-8000.app.github.dev'

timeout = 5

names = ["Juan", "Alexander", "Sebastian", "David", "Eva"]
last_names = ["Cardona", "Rios", "Valencia", "Cano", "Muñoz"]
items = ["Frutas", "Utiles Escolares", "Vegetales", "Productos de Aseo", "Tecnologia"]

def generate_element():
    first_name = random.choice(names)
    last_name = random.choice(last_names)
    products = [random.choice(items) for _ in range(2)]
    return {
        "name": f"{first_name} {last_name}",
        "products": products
    }

for _ in range(5):
    element_to_enqueue = generate_element()
    response = requests.post(f'{url}/enqueue', json=element_to_enqueue, timeout=timeout)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Element enqueued successfully: {data}")
    else:
        print(f'Error in POST to /enqueue: {response.status_code}')