require_relative 'linked_list'

def remove_nth_from_end(head, n)
  slow = head
  fast = head

  n.times do
    fast = fast.next
    if fast.nil?
      return head.next
    end
  end

  while fast.next
    fast = fast.next
    slow = slow.next
  end

  slow.next = slow.next.next

  return head
end

a = Node.new(1)
b = Node.new(2)
c = Node.new(3)
d = Node.new(4)
e = Node.new(5)

a.next = b
b.next = c
c.next = d
d.next = e

res = remove_nth_from_end(a, 2)

while res
  puts res.val
  puts
  res = res.next
end
