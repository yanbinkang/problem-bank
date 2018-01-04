from sll import *
"""
example: {a, b, c, d, e, f, g}
result: {a, c, e, g} ; {b, d, f}
"""
def alternative_list_split(head):
    if head == None:
        return None

    n1 = head
    head_2 = n1.next
    n2 = head_2

    while n1 != None and n1.next != None:
        n1.next = n1.next.next
        if n2.next != None:
            n2.next = n2.next.next
        n1 = n1.next
        n2 = n2.next

    if n2 != None:
        n2.next = None

    # for displaying results
    head_data = []
    head_2_data = []

    while head != None:
        head_data.append(str(head.data))
        head = head.next

    while head_2 != None:
        head_2_data.append(str(head_2.data))
        head_2 = head_2.next

    print ",".join(head_data)
    print ",".join(head_2_data)


if __name__ == '__main__':
    a = Node(1)
    b = Node(32)
    c = Node(12)
    d = Node(1)
    e = Node(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    f = Node(47)
    g = Node(32)
    h = Node(12)
    i = Node(1)

    f.next = g
    g.next = h
    h.next = i

    j = Node('a')
    k = Node('b')
    l = Node('c')
    m = Node('d')
    n = Node('e')
    o = Node('f')
    p = Node('g')

    j.next = k
    k.next = l
    l.next = m
    m.next = n
    n.next = o
    o.next = p

    alternative_list_split(a)

    alternative_list_split(f)

    alternative_list_split(j)
