class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None

class CircularList():
    def __init__(self):
        self.length = 0
        self.head = None

    def circular_list_length(self):
        currentnode = self.head
        if currentnode == None:
            return 0
        count  = 1
        currentnode = currentnode.getNext()
        while currentnode != self.head:
            currentnode = currentnode.getNext()
            count += 1
        return count

    def print_circular_list():
        currentnode = self.head
        if currentnode == None: return 0
        print(currentnode.getData())
        currentnode = currentnode.getNext()
        while currentnode != self.head:
            currentnode = currentnode.getNext()
            print(currentnode.getData())

    def insert_at_end_in_cll(self, data):
        current = self.head
        new_node = Node()
        new_node.setData(data)
        while current.getNext() != self.head:
            current = current.getNext()

        new_node.setNext(new_node)
        if self.head == None:
            self.head = new_node
        else:
            new_node.setNext(self.head)
            current.setNext(new_node)

    def insert_at_begin_in_cll(self, data):
        current = self.head
        new_node = Node()
        new_node.setData(data)
        while current.getNext() != self.head:
            current = current.getNext()

        new_node.setNext(new_node)
        if self.head == None:
            self.head = new_node
        else:
            new_node.setNext(self.head)
            current.setNext(new_node)
            self.head = new_node

    def delete_last_node_from_cll(self):
        temp  = self.head
        current = self.head

        if self.head == None:
            print("List Empty")
            return

        while current.getNext() != self.head:
            temp = current
            current = current.getNext()

        temp.setNext(current.getNext())

        return

    def delete_front_node_from_cll(self):
        current = self.head

        if self.head == None:
            print("List Empty")
            return

        while current.getNext() != self.head:
            current = current.getNext()

        current.setNext(self.head.getNext())
        self.head = self.head.getNext()
        return
