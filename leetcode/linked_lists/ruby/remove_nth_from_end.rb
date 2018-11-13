=begin
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
=end

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next

  def initialize(val)
    @val = val
    @next = nil
  end
end

def remove_nth_from_end(head, n)
  slow = head
  fast = head

  n.times do
    fast = fast.next

    return head.next if fast.nil?
  end

  while fast.next
    fast = fast.next
    slow = slow.next
  end

  slow.next = slow.next.next

  head
end

a = ListNode.new(1)
b = ListNode.new(2)
c = ListNode.new(3)
d = ListNode.new(4)
e = ListNode.new(5)

a.next = b
b.next = c
c.next = d
d.next = e

res = remove_nth_from_end(a, 2)

while res
  puts res.val
  puts
  res = res.next
end
