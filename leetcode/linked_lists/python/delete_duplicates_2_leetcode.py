"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
def delete_duplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    previous = None
    current = head

    while current != None and current.next != None:
        if current.val != current.next.val:
            previous = current
            current = current.next
        else:
            while current.next != None and current.next.val == current.val:
                current = current.next
            if previous != None:
                previous.next = current.next
            else:
                head = current.next

            current = current.next

    return head
