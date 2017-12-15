from linked_list import *
"""
https://leetcode.com/problems/merge-k-sorted-lists/

The trick is to use a PriorityQueue or Heap
"""
def merge_k_lists_priority_queue(lists):
    from Queue import PriorityQueue

    dummy_node = Node(None)
    current = dummy_node
    q = PriorityQueue()

    # store head of all nodes in list
    for node in lists:
        if node:
            q.put((node.data, node))

    while q.qsize() > 0:
        current.next = q.get()[1]
        current = current.next

        # put node and node's data in q if it has next
        if current.next:
            q.put((current.next.data, current.next))

    return dummy_node.next



def merge_k_lists_heap(lists):
    from heapq import heappush, heappop, heapreplace, heapify
    dummy_node = node = Node(0)
    h = [(n.val, n) for n in lists if n]
    heapify(h)

    while h:
        val, n = h[0]
        if n.next is None:
            heappop(h)
        else:
            heapreplace(h, (n.next.val, n.next))
        node.next = n
        node = node.next

    return dummy_node.next

