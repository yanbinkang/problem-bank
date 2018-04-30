class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_biginning(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.set_next(self.head)
            self.head = new_node
            new_node.set_prev(None)
        else:
            self.insert_before(self.head, data)

    def insert_after(self, node, data):
        new_node = Node(data)
        new_node.set_prev(node)
        new_node.set_next(node.get_next())
        if node.get_next() == None:
            self.tail = new_node
        else:
            node.get_next().set_prev(new_node)
        node.set_next(new_node)

    def insert_before(self, node, data):
        new_node = Node(data)
        new_node.set_prev(node.get_prev())
        new_node.set_next(node)
        if node.get_prev() == None:
            self.head = new_node
        else:
            node.get_prev().set_next(new_node)
        node.set_prev(new_node)

    def insert_end(self, data):
        if self.tail == None:
            self.insert_biginning(data)
        else:
            self.insert_after(self.tail, data)

dl = DoublyLinkedList()
dl.insert_biginning(12)
dl.insert_after(dl.head, 99)
dl.insert_after(dl.head.get_next(), 37)
dl.insert_end(45)


print dl.head.get_next().get_next().get_next().get_data()
