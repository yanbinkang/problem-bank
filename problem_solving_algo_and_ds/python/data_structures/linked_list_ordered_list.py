class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newData):
        self.data = newData

    def set_next(self, newNext):
        self.next = newNext


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

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next()

        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

def merge(list_1, list_2):
    current_1 = list_1.head
    current_2 = list_2.head
    dummy = OrderedList()

    while current_1 != None and current_2 != None:
        if current_1.get_data() < current_2.get_data():
            dummy.add(current_1.get_data())
            current_1 = current_1.get_next()
        else:
            dummy.add(current_2.get_data())
            current_2 = current_2.get_next()

    if current_1 == None:
        dummy.add(current_2.get_data())
    else:
        dummy.add(current_1.get_data())
    return dummy


l1 = OrderedList()
l1.add(7)
l1.add(5)
l1.add(2)

l2 = OrderedList()
l2.add(11)
l2.add(3)

print merge(l1, l2)
