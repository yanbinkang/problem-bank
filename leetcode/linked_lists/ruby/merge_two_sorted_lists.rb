require_relative 'linked_list'

def sorted_merge(a, b)
  if a.nil?
    return b
  elsif b.nil?
    return a
  end

  if a.val <= b.val
    result =  a
    result.next = sorted_merge(a.next, b)
  else
    result = b
    result.next = sorted_merge(a, b.next)
  end

  return result
end


a = Node.new(1)
b = Node.new(2)
c = Node.new(3)

e = Node.new(4)
f = Node.new(5)
g = Node.new(6)

a.next = b
b.next = c

e.next = f
f.next = g

res = sorted_merge(a, e)

while !res.nil?
  puts res.val
  puts
  res = res.next
end
