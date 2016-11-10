class Node
  attr_accessor :data, :next_pointer

  def initialize(init_data)
    @data = init_data
    @next_pointer = nil
  end

  def has_next?
    !self.next_pointer.nil?
  end
end
