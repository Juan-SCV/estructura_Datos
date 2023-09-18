class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class Cola:
    def __init__(self):
        self.front = None
        self.rear = None
        self.message_id = 1 

    def is_empty(self):
        return self.front is None

    def encolar(self, value):
        value['id'] = self.message_id
        new_node = Nodo(value)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.message_id += 1

    def desencolar(self):
        if self.is_empty():
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None

        current_node = self.front
        new_id = 1
        while current_node:
            current_node.value['id'] = new_id
            new_id += 1
            current_node = current_node.next

        return value

    def ver_listado(self):
        elements = []
        current_node = self.front
        while current_node:
            elements.append(current_node.value)
            current_node = current_node.next
        return elements

    def ver_primero(self):
        if not self.is_empty():
            return self.front.value
        else:
            return None

    def ver_ultimo(self):
        if not self.is_empty():
            return self.rear.value
        else:
            return None

    def contar(self):
        counter = 0
        current_node = self.front
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter

    def desencolar_id(self, message_id):
        current_node = self.front
        previous_node = None
        while current_node:
            if current_node.value['id'] == message_id:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.front = current_node.next
                if current_node == self.rear:
                    self.rear = previous_node

                new_front = self.front
                new_id = 1
                while new_front:
                    new_front.value['id'] = new_id
                    new_id += 1
                    new_front = new_front.next

                return current_node.value
            previous_node = current_node
            current_node = current_node.next
        return None
