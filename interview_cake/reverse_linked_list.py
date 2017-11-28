def reverse(head_of_list):
    current = head_of_list
    previous = None
    next = None

    while (current is not None):
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


# def reverse_linked_list(head):
#     if linked_list.count <= 1:
#         return head

#     current = head.next
#     head.next = None
#     while current != None:
#         current.next = head
#         head = current
#         current = current.next
#     return head
