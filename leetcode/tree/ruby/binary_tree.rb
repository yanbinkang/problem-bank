class BinaryTree
  attr_accessor :left, :right

  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end

  def insert_left(new_node)
    if left.nil?
      left = BinaryTree.new(new_node)
    else
      t = BinaryTree.new(new_node)
      t.left = left
      left = t
    end
  end

  def insert_right(new_node)
    if right.nil?
      right = BinaryTree.new(new_node)
    else
      t = BinaryTree.new(new_node)
      t.right = right
      right = t
    end
  end
end
