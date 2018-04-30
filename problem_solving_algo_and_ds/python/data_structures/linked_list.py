class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)

        if self.head == None:
            self.tail = temp

        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def reverse_rec(self, a_node):
        if a_node != None:
            right = a_node.get_next()
            if self.head != a_node:
                a_node.next = self.head
                self.head = a_node
            else:
                a_node.next = None

            self.reverse_rec(right)

    def insert(self, item, exsitItem):
        temp = Node(item)
        current = self.head
        found = False
        while not found:
            if current.getData() == exsitItem:
                found = True
            else:
                current = current.getNext()

        temp.setNext(current.getNext())
        current.setNext(temp)

    def pop(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

                if current ==  None:
                    raise ValueError("Item cannot be found.")

        if previous == None:
            temp = self.head
            self.head = current.getNext()
            return temp.getData()
        else:
            temp = current
            previous.setNext(current.getNext())
            return temp.getData()

    def append(self, item):
        # O(1)
        temp = Node(item)
        self.tail.setNext(temp)
        self.tail = temp



mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(54)

mylist.add(100)
mylist.append(-1)
mylist.append(2)
print("Size of linked list is " + str(mylist.size()))
head = mylist.head
tail = mylist.tail
print(head.data)
print(tail.data)
print(head.getNext().data)
print(head.getNext().getNext().data)

print(mylist)
