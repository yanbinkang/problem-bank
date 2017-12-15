require_relative 'linked_list'

# https://leetcode.com/problems/partition-list/

def partition(head, x)
  dummy_node_1 = p1 = Node.new(0)
  dummy_node_2 = p2 = Node.new(0)

  while head
    if head.val < x
      p1.next = head
      p1 = p1.next
    else
      p2.next = head
      p2 = p2.next
    end

    head = head.next
  end

  p2.next = nil
  p1.next = dummy_node_2.next

  dummy_node_1.next
end


a = Node.new(1)
b = Node.new(4)
c = Node.new(3)
d = Node.new(2)
e = Node.new(5)
f = Node.new(2)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

res = partition(a, 3)

loop do
  puts res.val
  puts
  res = res.next

  break if res.nil?
end
