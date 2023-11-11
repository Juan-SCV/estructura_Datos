import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, data, label, predicted_label):
        self.data = data
        self.label = label
        self.predicted_label = predicted_label
        self.left = None
        self.right = None

class Arbol:
    def __init__(self):
        self.root = None

    def insert_data(self, data, label, predicted_label, is_ham):
        self.root = self._insert_data(self.root, data, label, predicted_label, is_ham)

    def _insert_data(self, node, data, label, predicted_label, is_ham):
        if node is None:
            return Node(data, label, predicted_label)

        if is_ham:
            node.left = self._insert_data(node.left, data, label, predicted_label, is_ham)
        else:
            node.right = self._insert_data(node.right, data, label, predicted_label, not is_ham)

        return node

    def inorden_traversal(self, node):
        if node is not None:
            self.inorden_traversal(node.left)
            print(f"Data: {node.data}, Actual Label: {node.label}, Predicted Label: {node.predicted_label}")
            self.inorden_traversal(node.right)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.inorden_traversal(self.root)
