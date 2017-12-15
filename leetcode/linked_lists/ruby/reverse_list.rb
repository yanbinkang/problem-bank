require_relative 'linked_list'

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

a = Node.new(1)
b = Node.new(2)
c = Node.new(3)

a.next = b
b.next = c

res = reverse_list(a)

while res
  puts res.val
  puts
  res = res.next
end
