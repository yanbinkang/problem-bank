class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def has_prev(self):
        return self.prev != None

    def __str__(self):
        return "Node[Data = %s]" % (self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = Node(data, None, current)
            self.tail = current.next

    def delete(self, data):
        current = self.head

        if current.data == data:
            self.head = current.next
            self.head.prev = None
            return True

        if current == None:
            return False

        if self.tail == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return True

        while current != None:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            current = current.next

        # the element is absent
        return False


    def insert_at_beginning(self, data):
        new_node = Node(data, None, None)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.set_prev(None)
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node


    def get_node(self, index):
        current_node = self.head
        if current_node == None:
            return None

        i = 0
        while i < index and current_node.get_next() is not None:
            current_node = current_node.get_next()
            if current_node == None:
                break

            i += 1
        return current_node


    def insert_at_given_position(self, index, data):
        new_node = Node(data)
        if self.head == None or index == 0:
            self.insert_at_beginning(data)
        elif index > 0:
            temp = self.get_node(index)
            if temp == None or temp.get_next() == None:
                self.insert(data)
            else:
                new_node.set_next(temp.get_next())
                new_node.set_prev(temp)
                temp.get_next().set_prev(new_node)
                temp.set_next(new_node)

    def find(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return True
            current = current.next
        return False


    def fwd_print(self):
        current = self.head

        if current == None:
            print("No elements")
            return False

        while current != None:
            print(current.data)
            current = current.next
        return True


    def rev_print(self):
        current = self.tail
        if self.tail == None:
            print('No Elements')
            return False

        while current != None:
            print(current.data)
            current = current.prev

        return True



if __name__ == '__main__':
    l = DoubleLinkedList()

    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)

    # Forward Print
    l.fwd_print()

    # Reverse Print
    l.rev_print()

    if l.find(3):
        print('Found')
    else:
        print('Not Found')

    l.delete(3)

    l.fwd_print()

    l.rev_print()


    if l.find(3):
        print('Found')
    else:
        print('Not Found')
