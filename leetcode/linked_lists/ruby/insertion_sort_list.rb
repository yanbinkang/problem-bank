require_relative 'linked_list'

def insertion_sort_list(head)
  head if head.nil?

  dummy_node = previous = Node.new(0)
  current = head
  next_node = nil

  while current
    next_node = current.next

    while previous.next and previous.next.val < current.val
      previous = previous.next
    end

    current.next = previous.next
    previous.next = current
    previous = dummy_node
    current = next_node
  end

  dummy_node.next
end

a = Node.new(54)
b = Node.new(26)
c = Node.new(93)
d = Node.new(17)

a.next = b
b.next = c
c.next = d

res = insertion_sort_list(a)

while res
  puts res.val
  puts
  res = res.next
end
