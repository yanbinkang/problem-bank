"""
http://www.geeksforgeeks.org/clone-linked-list-next-arbit-pointer-set-2/
"""

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.arbitrary = None

def deep_copy_arbitrary_pointer(head):
    if head == None:
        return None

    current = head
    new_head = None
    previous = None
    hash_table = {}

    while current != None:
        new_node = Node(current.data)

        if current.arbitrary:
            new_node.arbitrary = current.arbitrary

        if previous != None:
            previous.next = new_node
        else:
            new_head = new_node

        hash_table[current] = new_node

        previous = new_node
        current = current.next

    new_current = new_head

    # updating arbitrary pointer
    while new_current != None:
        if new_current.arbitrary != None:
            new_current_arbitrary = hash_table[new_current.arbitrary]

            new_current.arbitrary = new_current_arbitrary

        new_current = new_current.next

    return new_head


if __name__ == '__main__':
    a = Node(7)
    b = Node(14)
    c = Node(21)

    a.next = b
    b.next = c

    a.arbitrary = c
    c.arbitrary = a

    res = deep_copy_arbitrary_pointer(a)
