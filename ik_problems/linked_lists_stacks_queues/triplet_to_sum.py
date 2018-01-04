# http://www.geeksforgeeks.org/find-a-triplet-from-three-linked-lists-with-sum-equal-to-a-given-number/
from sll import *
import merge_sort_link_list

def triplet_to_sum(head_1, head_2, head_3, target_sum):
    if head_1 == None or head_2 == None or head_3 == None:
        return

    a = head_1

    head_2 = merge_sort_link_list.merge_sort_link_list(head_2, True)
    head_3 = merge_sort_link_list.merge_sort_link_list(head_3, False)

    while a != None:
        b = head_2
        c = head_3
        while b != None and c != None:
            total = a.data + b.data + c.data

            if total == target_sum:
                print "Triplet found: %s %s %s" % (a.data, b.data, c.data)
                return True
            elif total < target_sum:
                b = b.next
            else:
                c = c.next
        a = a.next

    print("No triplet found")
    return False


l1 = UnOrderedList()
l1.add(29)
l1.add(6)
l1.add(12)

l2 = UnOrderedList()
l2.add(8)
l2.add(5)
l2.add(23)

l3 = UnOrderedList()
l3.add(59)
l3.add(20)
l3.add(90)

l4 = UnOrderedList()
l4.add(20)
l4.add(5)
l4.add(15)
l4.add(10)

l5 = UnOrderedList()
l5.add(10)
l5.add(9)
l5.add(4)
l5.add(2)

l6 = UnOrderedList()
l6.add(1)
l6.add(2)
l6.add(4)
l6.add(8)

print triplet_to_sum(l1.head, l2.head, l3.head, 101)
print triplet_to_sum(l4.head, l5.head, l6.head, 25)
