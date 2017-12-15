from linked_list import *
"""
https://leetcode.com/problems/insertion-sort-list/
"""
def insertion_sort_list(head):
    if head == None:
        return head

    dummy_node = previous = Node(0)
    current = head
    next_node = None

    while current != None:
        next_node = current.next

        # find the right place to insert
        while previous.next != None and previous.next.data < current.data:
            previous = previous.next

        # insert between previous and previous.next
        current.next = previous.next
        previous.next = current
        previous = dummy_node
        current = next_node

    return dummy_node.next

if __name__ == '__main__':
    a = Node(54)
    b = Node(26)
    c = Node(93)
    d = Node(17)

    a.next = b
    b.next = c
    c.next = d

    res = insertion_sort_list(a)

    while res:
        print(str(res.data) + "\n")
        res = res.next

