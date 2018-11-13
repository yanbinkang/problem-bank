=begin
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
=end
# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next

  def initialize(val)
    @val = val
    @next = nil
  end
end

def add_two_numbers(l1, l2)
  carry = 0
  dummy_node = n = ListNode.new(0)

  while l1 || l2 || carry
    v1 = v2 = 0

    if l1
      v1 = l1.val
      l1 = l1.next
    end

    if l2
      v2 = l2.val
      l2 = l2.next
    end

    carry, val = (v1 + v2 + carry).divmod(10)

    n.next = ListNode.new(val)
    n = n.next
  end

  dummy_node.next
end

a = ListNode.new(2)
b = ListNode.new(4)
c = ListNode.new(3)

d = ListNode.new(5)
e = ListNode.new(6)
f = ListNode.new(4)

a.next = b
b.next = c

d.next = e
e.next = f

res = add_two_numbers(a, d)

# while !res.nil?
#   puts res.val + "\n"
#   res = res.next
# end

# loop do
#   puts res.val + "\n"
#   res = res.next
# end if res.nil?
