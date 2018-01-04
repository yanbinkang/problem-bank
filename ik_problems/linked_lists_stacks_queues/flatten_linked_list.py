# http://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/
"""
1) find tail
2) if head has child then
    i) set tail's next pointer to child
    ii) update tail pointer
    iii) set head -> child pointer to None
3) move head pointer
4) repeat
"""
def flatten_linked_list(head):
    tail = get_tail(head)

    while head != None:
        if head.child != None:
            tail.next = head.child
            tail = get_tail(tail.next)
            head.child = None
        head = head.next

def get_tail(head):
    if head == None:
        return None
    while head.next != None:
        head = head.next
    return head
