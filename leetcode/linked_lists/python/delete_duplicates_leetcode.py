"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
def delete_duplicates(head):
    current = head
    previous = None
    seen = {}

    while current != None:
        if current.val in seen:
            previous.next = current.next
        else:
            seen[current.val] = 1
            previous = current

        current = current.next

    return head
