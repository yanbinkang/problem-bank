require_relative 'linked_list'

def add_two_numbers(l1, l2)
  carry = 0
  dummy_node = n = Node.new(0)

  while (l1 && !l1.next_pointer.nil?) || (l2 && !l2.next_pointer.nil?) || carry
    v1 = v2 = 0

    if l1
      v1 = l1.data
      l1 = l1.next_pointer
    end

    if l2
      v2 = l2.data
      l2 = l2.next_pointer
    end

    carry, val = (v1+v2+carry).divmod(10)

    n.next_pointer = Node.new(val)
    n = n.next_pointer

  end

  return dummy_node.next_pointer
end

a = Node.new(2)
b = Node.new(4)
c = Node.new(3)

d = Node.new(5)
e = Node.new(6)
f = Node.new(4)

a.next_pointer = b
b.next_pointer = c

d.next_pointer = e
e.next_pointer = f

res = add_two_numbers(a, d)

# while !res.nil?
#   puts res.data + "\n"
#   res = res.next_pointer
# end

# loop do
#   puts res.data + "\n"
#   res = res.next_pointer
# end if res.nil?
