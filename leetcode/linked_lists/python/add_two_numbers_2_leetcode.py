from linked_list import *

"""
https://leetcode.com/problems/add-two-numbers-ii/

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

def add_two_numbers(l1, l2):
    s1 = []
    s2 = []

    while l1 != None:
        s1.append(l1.data)
        l1 = l1.next

    while l2 != None:
        s2.append(l2.data)
        l2 = l2.next

    total = 0
    node = Node(0)

    while len(s1) != 0 or len(s2) != 0:
        if len(s1) != 0:
            total += s1.pop()
        if len(s2) != 0:
            total += s2.pop()

        node.data = total % 10
        head = Node(total // 10)
        head.next = node
        node = head

        total /= 10

    return node.next if node.data == 0 else node

if __name__ == '__main__':
    a = Node(3)
    b = Node(6)
    c = Node(2)
    d = Node(4)
    e = Node(3)

    f = Node(5)
    g = Node(6)
    h = Node(4)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    f.next = g
    g.next = h

    res = add_two_numbers(a, f)

    while res is not None:
        print(str(res.data) + "\n")
        res = res.next
