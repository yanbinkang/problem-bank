from linked_list import *
"""
https://leetcode.com/problems/linked-list-cycle-ii/

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

# use dictionary, O(n) extra space
def detect_cycle(head):
    dic = {}
    while head:
        if head in dic:
            return head
        dic[head] = 0
        head = head.next
    return None

# two-pointer O(n)
def detect_cycle(head):
    if not head:
        return None

    fast = slow = head

    while fast is not None:
        slow = slow.next
        fast = fast.next

        if fast is None: return None

        fast = fast.next

        if fast == slow: # a cycle detected
            # now find where initial cycle started. we could have missed it while moving fast two steps ahead of slow!
            slow = head
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return fast

    return None
