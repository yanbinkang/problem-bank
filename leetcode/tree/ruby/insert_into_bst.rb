=begin
https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
=end
# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left, @right = nil, nil
  end
end

# @param {TreeNode} root
# @param {Integer} val
# @return {TreeNode}
def insert_into_bst(root, val)
  return if root.nil?

  put(val, root)

  root
end

def put(val, current_node)
  if val < current_node.val
    if current_node.left
      put(val, current_node.left)
    else
      current_node.left = TreeNode.new(val)
    end
  elsif current_node.right
    put(val, current_node.right)
  else
    current_node.right = TreeNode.new(val)
  end
end
