=begin
https://leetcode.com/problems/search-in-a-binary-search-tree/description/

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
=end
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left, @right = nil, nil
  end
end

def search_bst(root, val)
  return if root.nil?

  get(val, root)
end

def get(val, current_node)
  return if current_node.nil?

  if current_node.val == val
    current_node
  elsif val < current_node.val
    get(val, current_node.left)
  else
    get(val, current_node.right)
  end
end

if $PROGRAM_NAME == __FILE__
  t = TreeNode.new(4)
  t.left = TreeNode.new(2)
  t.right = TreeNode.new(7)
  t.left.left = TreeNode.new(1)
  t.left.right = TreeNode.new(3)

  p search_bst(t, 2)
end
