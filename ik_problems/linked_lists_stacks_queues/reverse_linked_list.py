def reverse(ssl):
    current = ssl.head
    previous = None
    next_node = None

    while current != None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous
