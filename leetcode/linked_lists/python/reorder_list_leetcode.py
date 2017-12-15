from linked_list import *
"""
https://leetcode.com/problems/reorder-list/

1. cut the list into two halves
2. prev will be tail of 1st half
3. slow will be the head of 2nd half
4. reverse 2nd half
5. merge two lists

Given {1,2,3,4}, reorder it to {1,4,2,3}
"""
def reorder_list(head):
    if head is None or head.next is None:
        return None

    # step 1. cut list into two halves
    prev = None
    slow = fast = l1 = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None # terminate first half

    # step 2. reverse the 2nd half
    l2 = reverse(slow)

    # step 3, merge the two halves
    merge(l1, l2)

    return head

def reverse(head):
    prev = None
    current = head

    while current != None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def merge(l1, l2):
    while l1 is not None:
        l1_next, l2_next = l1.next, l2.next
        l1.next = l2

        if l1_next == None:
            break

        l2.next = l1_next

        l1 = l1_next
        l2 = l2_next

# 1 -> 2
# 4 -> 3

# 1 -> 4 -> 2 -> 3

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.next = b
    b.next = c
    c.next = d

    res = reorder_list(a)

    while res:
        print(str(res.data) + "\n")
        res = res.next


