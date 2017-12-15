require_relative 'linked_list'

def remove_elements(head, val)
  while head && head.val == val # cater for multiple inital nodes being equal to val
    head = head.next
  end

  current = head

  while current && current.next
    if current.next.val == val
      current.next = current.next.next
    else
      current = current.next
    end
  end

  head
end


a = Node.new(1)
b = Node.new(2)
c = Node.new(6)
d = Node.new(3)
e = Node.new(4)
f = Node.new(5)
g = Node.new(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

res = remove_elements(a, 6)

while res
  puts res.val
  puts
  res = res.next
end
