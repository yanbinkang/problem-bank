from linked_list import *
"""
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

Algo: the idea is simple. Reverse the first half of the linked list and compare it to the second half.
"""
# O(n) time O(1) space
def is_palindrome(head):
    count = 0
    current = head

    while current:
        current = current.next
        count += 1

    current = head
    previous = None
    mid_point = count // 2

    # reverse first half
    for i in range(mid_point):
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    h2 = current if count % 2 == 0 else current.next
    """
    Ask yourself, what is a palindrome?
    1 -> 2 -> 3 -> 4 -> 5 in this case current becomes 4
    1 -> 2 -> 3 -> 4 in this case current becomes 3
    """

    h1 = previous
    while h1:
        if h1.data == h2.data:
            h1 = h1.next
            h2 = h2.next
        else:
            return False
    return True

"""
ref: http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
METHOD 1 (Use a Stack)
A simple solution is to use a stack of list nodes. This mainly involves three steps.
1) Traverse the given list from head to tail and push every visited node to stack.
2) Traverse the list again. For every visited node, pop a node from stack and compare data of popped node with currently visited node.
3) If all nodes matched, then return true, else false.

Time complexity of above method is O(n), but it requires O(n) extra space. Following methods solve this with constant extra space
"""
def is_palindrome_stack(head):
    stack = []
    current = head

    while current != None:
        stack.append(current.data)
        current = current.next

    current = head

    while current and stack:
        item = stack.pop()
        ll = current.data

        if item != ll:
            return False

        current = current.next

    return True

if __name__ == '__main__':
    a = Node("r")
    b = Node("a")
    c = Node("d")
    d = Node("a")
    e = Node("r")

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print is_palindrome(a)
    print is_palindrome_stack(a)
