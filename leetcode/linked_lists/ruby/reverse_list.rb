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

def reverse_list_rec(head)
  return _reverse(head, nil)
end

def _reverse(head, tail)
  return tail if head.nil?

  next_node = head.next
  head.next = tail

  return _reverse(next_node, head)
end

a = Node.new(1)
b = Node.new(2)
c = Node.new(3)

d = Node.new(1)
e = Node.new(2)
f = Node.new(3)

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
