import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("Stack is empty.")

    def remove_node(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next is not None and temp.next.data != data:
                temp = temp.next
            
            if temp.next is not None:
                temp.next = temp.next.next
            else:
                print(f"{data} not found in the stack.")

    def print_stack(self):
        num_nodes = 0
        temp = self.head
        while temp is not None:
            print(f"Node {num_nodes + 1} has a data value of: {temp.data}")
            temp = temp.next
            num_nodes += 1

    def fill_stack(self, num_nodes):
        for a in range(num_nodes):
            self.push(random.randint(1, 20)) 

stack = Stack()
num_nodes = int(input("Enter the number of nodes to create: "))
if num_nodes == 0:
    print("Empty stack")
else:
    random_data = stack.fill_stack(num_nodes)
    print("Initial Stack:")
    stack.print_stack()

    data_to_remove = int(input("Enter the data value of the node to remove: "))
    stack.remove_node(data_to_remove)
    print("Stack after removing the node:")
    stack.print_stack()