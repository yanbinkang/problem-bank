from sll import *

def remove_duplicates(head):
    hash_map = {}
    current = head
    prev = None

    while current != None:
        if current.data in hash_map:
            prev.next = current.next
        else:
            hash_map[current.data] = 1
            prev = current
        current = current.next

    return head

def pretty_print(res):
    while res != None:
        print str(res.data) + str("\n")
        res = res.next


if __name__ == '__main__':
    a = Node(12)
    b = Node(11)
    c = Node(12)
    d = Node(12)
    e = Node(21)
    f = Node(43)
    g = Node(21)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    h = Node(12)
    i = Node(11)
    j = Node(12)
    k = Node(21)
    l = Node(41)
    m = Node(43)
    n = Node(21)

    h.next = i
    i.next = j
    j.next = k
    k.next = l
    l.next = m
    m.next = n

    x = remove_duplicates(a)
    y = remove_duplicates(h)

    pretty_print(x)
    print "\n"
    pretty_print(y)



