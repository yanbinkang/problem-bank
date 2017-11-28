from sll import *

def merge(list_1, list_2):
    current_1 = list_1
    current_2 = list_2
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

if __name__ == '__main__':
    a = Node(5)
    b = Node(10)
    c = Node(15)

    a.next = b
    b.next = c

    f = Node(2)
    g = Node(3)
    h = Node(20)

    f.next = g
    g.next = h

    res = merge(a, f)

    print res

    # head = res.head

    # while head != None:
    #     print str(head.data) + "\n"
    #     head = head.next
