=begin
https://leetcode.com/problems/merge-two-binary-trees/#/description

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
        Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7

Output:
Merged tree:
         3
        / \
       4   5
      / \   \
     5   4   7

solution: https://discuss.leetcode.com/topic/92105/java-solution-6-lines-tree-traversal
=end
# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left, @right = nil, nil
  end
end

def merge_trees(t1, t2)
  return if t1.nil? && t2.nil?

  val = (t1 ? t1.val : 0) + (t2 ? t2.val : 0)

  root = TreeNode.new(val)

  root.left = merge_trees(t1 ? t1.left : nil, t2 ? t2.left : nil)

  root.right = merge_trees(t1 ? t1.right : nil, t2 ? t2.right : nil)

  root
end

if $PROGRAM_NAME == __FILE__
  t1 = TreeNode.new(1)
  t1.left = TreeNode.new(3)
  t1.right = TreeNode.new(2)
  t1.left.left = TreeNode.new(5)

  t2 = TreeNode.new(2)
  t2.left = TreeNode.new(1)
  t2.right = TreeNode.new(3)
  t2.left.right = TreeNode.new(4)
  t2.right.right = TreeNode.new(7)

  res = merge_trees(t1, t2)

  # test level order traversal
  queue = [res]

  data = []

  until queue.empty?
    collection = []

    queue.length.times do
      node = queue.pop
      collection << node.val
      queue.insert(0, node.left) if node.left

      queue.insert(0, node.right) if node.right
    end

    data << collection
  end

  p data
end
