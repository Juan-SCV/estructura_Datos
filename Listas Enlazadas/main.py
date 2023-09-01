import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def create_list(self, num_nodes):
        if num_nodes <= 0:
            return
        new_data = random.randint(1, 5)
        self.insert(new_data)
        self.create_list(num_nodes - 1)
    
    def print_list(self):
        current = self.head
        current_node = 1  
        while current:
            print(f"El Nodo {current_node} tiene un dato de valor: {current.data}")
            current = current.next
            current_node += 1

number_of_nodes = int(input("How many nodes do you wish to create: "))

my_list = LinkedList()
my_list.create_list(number_of_nodes)
my_list.print_list()