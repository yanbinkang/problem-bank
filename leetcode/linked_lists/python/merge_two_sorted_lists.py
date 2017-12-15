from linked_list import *

# https://leetcode.com/problems/merge-two-sorted-lists/

def merge_two_lists(a, b):
    # base cases
    if a == None:
        return b
    elif b == None:
        return a

    # pick either a or b and recur
    if a.data <= b.data:
        result = a
        result.next = merge_two_lists(a.next, b)
    else:
        result = b
        result.next = merge_two_lists(a, b.next)

    return result

# https://discuss.leetcode.com/topic/21292/python-solutions-iteratively-recursively-iteratively-in-place
def merge_two_lists_1(a, b):
    dummy = current = Node(0)

    while a and b:
        if a.data < b.data:
            current.next = a
            a = a.next
        else:
            current.next = b
            b = b.next

        current = current.next

    current.next = a or b
    return dummy.next

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)


    e = Node(4)
    f = Node(5)
    g = Node(6)

    a.next = b
    b.next = c

    e.next = f
    f.next = g

    # 1 -> 2 -> 3
    # 4 -> 5 -> 6

    res = merge_two_lists(a, e)

    while res != None:
        print str(res.data) + "\n"
        res = res.next
