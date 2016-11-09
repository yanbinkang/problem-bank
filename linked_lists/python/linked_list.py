class Node:
    def __init__(self, data):
        self.data = data
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


class LinkedList():
    def __init__(self):
        self.length = 0
        self.head = None

    def addNode(self, node):
        if self.length == 0:
            self.addBeg(node)
        else:
            self.addLast(node)


    def addBeg(self, node):
        newNode = node
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    # method to add a node after the node having the data-data. The data of the new nide is value2
    def addAfterValue(self, data, node):
        newNode = node
        currentnode = self.head

        while currentnode.next != None or currentnode.data != data:
            if currentnode.data == data:
                newNode.next = currentnode.next
                currentnode.next = newNode
                self.length = self.length + 1
                return
            else:
                currentnode = currentnode.next

        print('The data provided is not present')

    def addAtPos(self, pos, node):
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print('The position does not exist. Please enter a valid position')
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = node
                    node.next = currentnode
                    self.length += 1
                    return

                else:
                    previousnode = currentnode
                    currentnode = currentnode.next


    def addLast(self, node):
        currentnode = self.head

        while currentnode.next != None:
            currentnode = currentnode.next

        newNode = node
        newNode.next = None
        currentnode.next = newNode
        self.length = self.length + 1


    def deleteBeg(self):
        if self.length == 0:
            print('The list is empty')
        else:
            self.head = self.head.next
            self.length -= 1


    def deleteLast(self):
        if self.length == 0:
            print('The list is empty')
        else:
            currentnode = self.head
            previousnode = self.head

            while currentnode.next != None:
                previousnode = currentnode
                currentnode = currentnode.next

            previousnode.next = None

            self.length -= 1


    def deleteValue(self, data):
        currentnode = self.head
        previousnode = self.head

        while currentnode.next != None or currentnode.data != data:
            if currentnode.data == data:
                previousnode.next = currentnode.next
                self.length -= 1
                return

            else:
                previousnode = currentnode
                currentnode = currentnode.next

        print('The data provided is not present')


    def deleteAtPos(self, pos):
        count = 0
        previousnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print('The position does not exist. Please enter a valid position')
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next


    def getLength(self):
        return self.length


    def getFirst(self):
        if self.length == 0:
            print('The list is empty')
        else:
            return self.head.data


    def getLast(self):
        if self.length == 0:
            print('The list is empty')
        else:
            currentnode = self.head

            while currentnode.next != None:
                currentnode = currentnode.next

            return currentnode.data


    def getAPos(self, pos):
        count = 0
        currentnode = self.head


        if pos > self.length or pos < 0:
            print('The position does not exist. Please enter a valid postion')

        else:
            while currentnode.next != None or count < pos:
                count += 1
                if count == pos:
                    return currentnode.data
                else:
                    currentnode = currentnode.next


    def printList(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next

        print(nodeList)


