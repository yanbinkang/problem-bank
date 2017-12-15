from linked_list import *
"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 # 2 -> 4 -> 3
 +
 # 5 -> 6 -> 9
 # => 7 -> 0 -> 8
"""
def add_two_numbers(l1, l2):
    carry = 0
    dummy_node = n = Node(0)

    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.data
            l1 = l1.next
        if l2:
            v2 = l2.data
            l2 = l2.next

        carry, val = divmod(v1+v2+carry, 10)
        n.next = Node(val)
        n = n.next

    return dummy_node.next


if __name__ == '__main__':
    a = Node(2)
    b = Node(4)
    c = Node(3)

    d = Node(5)
    e = Node(6)
    f = Node(4)

    a.next = b
    b.next = c

    d.next = e
    e.next = f

    res = add_two_numbers(a, d)

    while res is not None:
        print(str(res.data) + "\n")
        res = res.next


