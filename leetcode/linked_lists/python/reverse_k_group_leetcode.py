from linked_list import *
"""
https://leetcode.com/problems/reverse-nodes-in-k-group/

https://discuss.leetcode.com/topic/31618/succinct-iterative-python-o-n-time-o-1-space

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

left, right: used to define reversion range
jump : used to connect last node in previous k-group to first node in following k-group
"""
def reverse_k_group(head, k):
    dummy_node = jump = Node(0)
    dummy_node.next = left = right = head

    while True:
        count = 0
        while right and count < k:
            right = right.next
            count += 1

        if count == k:
            prev, current = right, left

            for _ in range(k):
                # standard reversing
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # connect two k-groups
            jump.next = prev
            jump = left
            left = right
        else:
            return dummy_node.next

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    res = reverse_k_group(a, 2)

    while res:
        print(str(res.data) + "\n")
        res = res.next
