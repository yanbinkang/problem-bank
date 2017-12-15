require_relative 'linked_list'
=begin
https://leetcode.com/problems/swap-nodes-in-pairs/

Given 1->2->3->4, you should return the list as 2->1->4->3
=end

def swap_pairs(head)
  if head.nil? or head.next.nil?
    return head
  end

  prev = head
  current = head.next

  head = current

  while true
    next_node = current.next
    current.next = prev

    if next_node.nil? or next_node.next.nil?
      prev.next = next_node
      break
    end

    prev.next = next_node.next
    prev = next_node
    current = prev.next
  end

  head
end

a = Node.new(1)
b = Node.new(2)
c = Node.new(3)
d = Node.new(4)

a.next = b
b.next = c
c.next = d

res = swap_pairs(a)

while res
  puts res.val
  puts
  res = res.next
end
