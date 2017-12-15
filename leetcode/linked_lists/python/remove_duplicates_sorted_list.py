from linked_list import *

def delete_duplicates(head):
    current = head
    previous = None

    hash_table = {}

    while current != None:
        if current.data in hash_table.keys():
            previous.next = current.next
        else:
            hash_table[current.data] = 1
            previous = current

        current = current.next

    return head
