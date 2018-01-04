#solution: http://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/

from sll import *

def swap_kth_node(head, k):

    # count nodes in linked list
    n = size(head)

    # check if k is valid
    if n < k:
        return

    # if x (kth node from start) and y (kth node from end) are same
    if 2 * k - 1 == n:
        head

    # find the kth node from beginning of linked list. We also find the previous of kth node because we need to update next pointer of previous.
    x = head
    x_prev = None
    i = 1
    while i < k:
        x_prev = x
        x = x.next
        i += 1

    # Similarly, find the kth node from end and its previous. kth node from end is (n-k+1)th node from beginning
    y = head
    y_prev = None
    i = 1
    while i < n - k + 1:
        y_prev = y
        y = y.next
        i += 1

    # if x_prev exists, then new next will be y. Consider the case
    # when y.next is x, in this case, x_prev and y are same. So the statement
    # "x_prev.next = y" creates a self loop. This self loop will be broken
    # when we change y.next
    if x_prev != None:
        x_prev.next = y

    # same thing applies to y_prev
    if y_prev != None:
        y_prev.next = x

    # swap next pointers of x and y. These statements also break self loop if x.next is y and y.next is x
    temp = x.next
    x.next = y.next
    y.next = temp

    # change head pointers when k is 1 or n
    if k == 1:
        head = y

    if k == n:
        head = x

    return head


def size(head):
    count = 0
    current = head
    while current != None:
        count += 1
        current = current.next

    return count

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(7)
f = Node(0)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

f = Node(1)
g = Node(2)
h = Node(4)
i = Node(7)
j = Node(0)

f.next = g
g.next = h
h.next = i
i.next = j

# swap_kth_node(f, 3)

res = swap_kth_node(f, 3)

while  res != None:
    print str(res.data) + "\n"
    res = res.next
