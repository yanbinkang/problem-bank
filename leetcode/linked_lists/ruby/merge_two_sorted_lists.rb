=begin
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
=end

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next

  def initialize(val)
    @val = val
    @next = nil
  end
end

def sorted_merge(a, b)
  # base cases
  return b if a.nil?
  return a if b.nil?

  if a.val <= b.val
    result =  a
    result.next = sorted_merge(a.next, b)
  else
    result = b
    result.next = sorted_merge(a, b.next)
  end

  result
end

a = ListNode.new(1)
b = ListNode.new(2)
c = ListNode.new(3)

e = ListNode.new(4)
f = ListNode.new(5)
g = ListNode.new(6)

a.next = b
b.next = c

e.next = f
f.next = g

res = sorted_merge(a, e)

until res.nil?
  puts res.val
  puts
  res = res.next
end
