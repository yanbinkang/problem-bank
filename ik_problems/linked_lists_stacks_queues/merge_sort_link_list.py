from sll import *

def merge_sort_link_list(head, is_ascending):
    if head == None or head.next == None:
        return head

    head_1 = get_middle_of_list(head)
    head = merge_sort_link_list(head, is_ascending)
    head_1 = merge_sort_link_list(head_1, is_ascending)
    return sorted_merge(head, head_1, is_ascending)

def sorted_merge(head_1, head_2, is_ascending):
    if head_1 == None:
        return head_2

    if head_2 == None:
        return head_1

    if is_ascending:
        if head_1.data <= head_2.data:
            head_1.next = sorted_merge(head_1.next, head_2, is_ascending)
            return head_1
        else:
            head_2.next = sorted_merge(head_1, head_2.next, is_ascending)
            return head_2
    else:
        if head_1.data >= head_2.data:
            head_1.next = sorted_merge(head_1.next, head_2, is_ascending)
            return head_1
        else:
            head_2.next = sorted_merge(head_1, head_2.next, is_ascending)
            return head_2

# get middle node in sll
def get_middle_of_list(head):
    if head == None:
        return None

    slow = head
    fast = head.next

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    new_head = slow.next
    slow.next = None
    return new_head

if __name__ == '__main__':
    a = Node(5)
    b = Node(23)
    c = Node(29)
    d = Node(6)
    e = Node(12)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    merged_ll = merge_sort_link_list(a, False)

    while merged_ll:
        print(str(merged_ll.data) + "\n")
        merged_ll = merged_ll.next
