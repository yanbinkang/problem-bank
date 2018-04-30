class BinaryHeap

  # attr_accessor :heap_list, :current_size

  def initialize
    @heap_list = [0]
    @current_size = 0
  end

  def perc_up(index)
    while index / 2 > 0
      if @heap_list[index] < @heap_list[index / 2]
        temp = @heap_list[index]
        @heap_list[index] = @heap_list[index / 2]
        @heap_list[index / 2] = temp
      end

      index = index / 2
    end
  end

  def insert(item)
    @heap_list.push(item)
    @current_size += 1
    perc_up(@current_size)
  end

  def perc_down(index)
    while (index * 2) <= @current_size
      mc = min_child(index)
      if @heap_list[index] > @heap_list[mc]
        temp = @heap_list[index]
        @heap_list[index] = @heap_list[mc]
        @heap_list[mc] = temp
      end

      index = mc
    end
  end

  def min_child(index)
    if (index * 2 + 1) > @current_size
      return index * 2
    else
      if @heap_list[index * 2] < @heap_list[index * 2 + 1]
        return index * 2
      else
        return index * 2 + 1
      end
    end
  end

  def del_min
    ret_val = @heap_list[1]
    @heap_list[1] = @heap_list[@current_size]
    @current_size -= 1
    @heap_list.pop
    perc_down(1)
    return ret_val
  end

  def build_heap(a_list)
    i = a_list.length / 2
    @current_size = a_list.length
    @heap_list = [0] + a_list

    while i > 0
      perc_down(i)
      i = i - 1
    end
  end

end


bh = BinaryHeap.new()
bh.build_heap([9, 6, 5, 2, 3])
bh.del_min
p bh
