class Stack
  attr_accessor :items

  def initialize
    @items = []
  end

  def is_empty
    items.empty?
  end

  def push(item)
    items.push(item)
  end

  def pop
    return nil if items.empty?
    return items.pop
  end

  def peek
    return nil if items.empty?
    return items[-1]
  end

  def size
    items.length
  end
end


=begin
s = Stack.new
p s.is_empty
s.push(1)
s.push(2)
s.push(3)
s.push(4)

p s.peek
p s.pop
p s.peek

p s.is_empty
=end
