import requests
from bs4 import BeautifulSoup

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Lista_Doblemente_Enlazada:
    def __init__(self):
        self.head = None
        self.rear = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.rear = new_node
        else:
            new_node.previous = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            print('')
            current = current.next

url = "https://listado.mercadolibre.com.co/herramientas/herramientas-manuales/nuevo/herramientas-manuales_BestSellers_YES_NoIndex_True#deal_print_id=8c8b7500-5d84-11ee-a730-1917980a18a8&c_id=special-normal&c_element_order=2&c_campaign=HERRAMIENTAS-MANUALES&c_uid=8c8b7500-5d84-11ee-a730-1917980a18a8"

timeout = 5
response = requests.get(url, timeout=timeout)

data_list = Lista_Doblemente_Enlazada()

soup = BeautifulSoup(response.text, 'html.parser')

container = soup.find_all('div', class_='ui-search-result__wrapper shops__result-wrapper')


if response.status_code == 200:

    for item in container:
        product_name = item.find('h2', class_='ui-search-item__title shops__item-title')
        product_price = item.find('span', class_='andes-money-amount__fraction')
        product_image = item.find('img', class_='ui-search-result-image__element shops__image-element')['src'] if not ('src') else ''
        product_link = item.find('a', class_='ui-search-item__group__element shops__items-group-details ui-search-link')['href']

        if product_name and product_price and product_link:
            name = product_name.text.strip()
            price = product_price.text.strip()
            image_url = product_image['src'] if isinstance(product_image, dict) and product_image.has_attr('src') else ''
            link = product_link

            product_data = {
                'Name': name,
                'Price': price,
                'Image': image_url,
                'Link': link,
            }

            data_list.add(product_data)   

    data_list.display()

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)



