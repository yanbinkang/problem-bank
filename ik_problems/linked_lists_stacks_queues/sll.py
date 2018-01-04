class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.get_data

    def get_next(self):
        return self.next

    def set_data(self, newData):
        self.data = newData

    def set_next(self, newNext):
        self.next = newNext


class UnOrderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        res = []
        while current != None:
            res.append(current)
            current = current.get_next()

        return str(self.head.get_data()) + ' connected to: ' + str([x.get_data() for x in res[1:]])

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

class OrderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        res = []
        while current != None:
            res.append(current)
            current = current.get_next()

        return str(self.head.get_data()) + ' connected to: ' + str([x.get_data() for x in res[1:]])

    def add(self, item):
        current = self.head
        stop = False
        previous = None

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp
