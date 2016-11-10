require_relative 'linked_list'

def sorted_merge(a, b)
  if a.nil?
    return b
  elsif b.nil?
    return a
  end

  if a.data <= b.data
    result =  a
    result.next_pointer = sorted_merge(a.next_pointer, b)
  else
    result = b
    result.next_pointer = sorted_merge(a, b.next_pointer)
  end

  return result
end


a = Node.new(1)
b = Node.new(2)
c = Node.new(3)

e = Node.new(4)
f = Node.new(5)
g = Node.new(6)

a.next_pointer = b
b.next_pointer = c

e.next_pointer = f
f.next_pointer = g

res = sorted_merge(a, e)

while !res.nil?
  puts res.data
  res = res.next_pointer
end
