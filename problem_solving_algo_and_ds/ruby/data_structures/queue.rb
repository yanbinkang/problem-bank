class Queue
  attr_accessor :items

  def initialize
    @items = []
  end

  def is_empty
    items.empty?
  end

  def enqueue(item)
    items.unshift(item)
  end

  def dequeue
    return nil if items.empty?
    return items.pop
  end

  def size
    items.length
  end
end


if __FILE__ == $0
  q = Queue.new
  p q.is_empty
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  q.enqueue(4)

  p q.dequeue
  p q.is_empty
end
