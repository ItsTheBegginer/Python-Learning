class Node():
    def __init__(self , value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self , value):
        self.value = value
        new_node = Node(self.value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self , value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 

        def pop(self):
            temp = 
