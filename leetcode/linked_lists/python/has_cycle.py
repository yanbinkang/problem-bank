from linked_list import *

"""
https://leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

def has_cycle(head):
    fast = head
    slow = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast - fast.next.next

        if fast == slow:
            return True

    return False
