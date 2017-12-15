require_relative 'linked_list'

def delete_duplicates(head)
  previous = nil
  current = head

  while current && current.next
    if current.val != current.next.val
      previous = current
      current = current.next
    else
      current = current.next while current.next && current.next.val == current.val

      if previous
        previous.next = current.next
      else
        head = current.next
      end

      current = current.next
    end
  end

  return head
end


a = Node.new(1)
b = Node.new(2)
c = Node.new(3)
d = Node.new(3)
e = Node.new(4)
f = Node.new(4)
g = Node.new(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

# Given 1->2->3->3->4->4->5, return 1->2->5.
res = delete_duplicates(a)

loop do
  puts res.val
  puts
  res = res.next
  break if res.nil?
end
