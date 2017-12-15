from linked_list import *

def ordered_insert(head, item):
    current = head
    previous = None
    stop  = False

    while current != None and not stop:
        if current.getData() > item:
            stop = True
        else:
            previous = current
            current = current.getNext()

    temp = Node(item)
    if previous == None:
        temp.setNext(head)
        head = temp
    else:
        temp.setNext(current)
        previous.setNext(temp)


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(5)

    a.next = b
    b.next = c
    c.next = d

    ordered_insert(a, 4)

    start_node = a

    while start_node != None:
        print("Node data is %s" % (start_node.data))
        start_node = start_node.next
