class Node
  attr_accessor :data, :next

  def initialize(initdata)
    @data = initdata
    @next = nil
  end
end


class OrderedList
  attr_accessor :head

  def initialize
    @head = nil
  end

  def is_empty?
    head.nil?
  end

  def size
    current = head
    count = 0

    while !current.nil?
      count += 1
      current = current.next
    end

    return count
  end

  def remove(item)
    current = head
    previous = nil
    found = false

    while !found
      if current.data == item
        found = true
      else
        previous = current
        current = current.next
      end
    end

    if previous.nil?
      self.head = current.next
    else
      previous.next = current.next
    end
  end

  def search(item)
    current = head
    found = false
    stop = false

    while !current.nil? && !found && !stop
      if current.data == item
        found = true
      else
        if current.data > item
          stop = true
        else
          current = current.next
        end
      end
    end

    return found
  end

  def add(item)
    current = head
    previous = nil
    stop = false

    while !current.nil? && !stop
      if current.data > item
        stop = true
      else
        previous = current
        current = current.next
      end
    end

    temp = Node.new(item)
    if previous.nil?
      temp.next = head
      self.head = temp
    else
      temp.next = current
      previous.next = temp
    end
  end
end


l1 = OrderedList.new()
(1..10).to_a.shuffle.each do |num|
  l1.add(num)
end

p l1.search(7)
p l1.size

p l1
