=begin
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
=end
# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

def reverse_list(head)
  current = head
  previous = nil

  while current
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
  end

  previous
end

def reverse_list_rec(head)
  reverse_helper(head, nil)
end

def reverse_helper(head, tail)
  return tail if head.nil?

  next_node = head.next
  head.next = tail

  reverse_helper(next_node, head)
end

a = ListNode.new(1)
b = ListNode.new(2)
c = ListNode.new(3)

d = ListNode.new(1)
e = ListNode.new(2)
f = ListNode.new(3)

a.next = b
b.next = c

d.next = e
e.next = f

res = reverse_list(a)
res1 = reverse_list_rec(d)

puts "=====res1====="
while res
  puts res.val
  puts
  res = res.next
end
puts "=====res2====="
while res1
  puts res1.val
  puts
  res1 = res1.next
end
