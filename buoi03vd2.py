class Node:
    def __init__(self):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.num0fNodes = 0

    def insert_start(self, data):
        self.num0fNodes = self.num0fNodes + 1
        new_node = Node(data)

        if not self.head:
            self.heafd = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self, data):
        self.num0fNodes = self.num0fNodes + 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node
