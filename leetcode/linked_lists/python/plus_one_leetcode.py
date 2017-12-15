from linked_list import *

"""
https://leetcode.com/problems/plus-one-linked-list/

Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4
"""

def plus_one(head):
    s = []
    current = head

    while current != None:
        s.append(current.data)
        current = current.next

    total = 1
    node = Node(0)

    while len(s) != 0:
        total += s.pop()

        carry, val = divmod(total, 10)
        node.data = val
        head = Node(carry)
        head.next = node
        node = head

        total /= 10

    return node.next if node.data == 0 else node


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.next = b
    b.next = c

    res = plus_one(a)

    while res:
        print(str(res.data) + "\n")
        res = res.next
