def kth_to_last_node(k, head):
    list_length = 1
    current_node = head

    # find the length
    while current_node.next != None:
        current_node = current_node.next
        list_length += 1

    if k > list_length:
        raise('k is larger than the length of the linked list!')

    how_far_to_go = list_length - k

    current_node = head

    for i in xrange(how_far_to_go):
        current_node = current_node.next

    return current_node







def kth_to_last_node(k, head):
    left_node = head
    right_node = head

    for i in xrange(k-1):
        if not right_node.next:
            raise LookupError('k is larger than the length of the linked list!')

        right_node = right_node.next

    while right_node.next is not None:
        left_node = left_node.next
        right_node = right_node.next

    return left_node
