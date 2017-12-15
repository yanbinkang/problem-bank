require_relative 'linked_list'

def is_palindrome(head)
  count = 0
  current = head

  while current
    current = current.next
    count += 1
  end

  current, previous = head, nil

  (count / 2).times do
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
  end

  h2 = (count % 2).even? ? current : current.next

  h1 = previous

  while h1
    if h1.val == h2.val
      h1 = h1.next
      h2 = h2.next
    else
      return false
    end
  end

  true
end

a = Node.new("r")
b = Node.new("a")
c = Node.new("d")
d = Node.new("a")
e = Node.new("r")

a.next = b
b.next = c
c.next = d
d.next = e

puts is_palindrome(a)
