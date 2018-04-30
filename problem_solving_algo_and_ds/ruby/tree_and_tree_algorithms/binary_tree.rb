class BinaryTree
  attr_accessor :key, :left_child, :right_child

  def initialize(root_obj)
    @key = root_obj
    @left_child = nil
    @right_child = nil
  end

  def insert_left(new_node)
    if left_child.nil?
      self.left_child = BinaryTree.new(new_node)
    else
      temp = BinaryTree.new(new_node)
      temp.left_child = left_child
      self.left_child = temp
    end
  end

  def insert_right(new_node)
    if right_child.nil?
      self.right_child = BinaryTree.new(new_node)
    else
      temp = BinaryTree.new(new_node)
      temp.right_child = right_child
      self.right_child = temp
    end
  end

  def pre_order
    p key
    if left_child
      left_child.pre_order
    end
    if right_child
      right_child.pre_order
    end
  end

  def in_order
    if left_child
      left_child.in_order
    end
    p key
    if right_child
      right_child.in_order
    end
  end

  def post_order
    if left_child
      left_child.post_order
    end
    if right_child
      right_child.post_order
    end
    p key
  end
end

def build_tree
  tree = BinaryTree.new('a')

  tree.insert_left('b')
  tree.insert_right('c')
  tree.left_child.insert_left('d')
  tree.left_child.insert_right('e')
  tree.right_child.insert_left('f')
  tree.right_child.insert_right('g')

  return tree
end

=begin
              a
            /   \
           b     c
          / \   / \
         d   e f   g
=end

tree = build_tree

tree.in_order
