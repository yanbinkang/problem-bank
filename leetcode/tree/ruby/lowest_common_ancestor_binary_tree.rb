=begin
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.


According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself)."

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.



https://youtu.be/13m9ZCB8gjw

Algorithm:
1) Search for either of the two nodes whose lca we're looking for starting from the root

2) Anytime any of the node is found we return that node to its parent

3) Anytime any node gets a not null node from the left side and a not null node from the right side, it knows its the lca and returns its node value to its parent

O(n)
=end
def lowest_common_ancestor(root, p, q)
  return if root.nil?

  return root if root == p or root == q

  # find p or q in left subtree
  left = lowest_common_ancestor(root.left, p, q)
  # find p or q in right subtree
  right = lowest_common_ancestor(root.right, p, q)

  # three possible return values

  # p and q can be found on root's left or right subtree. meaning root is LCA
  return root if left && right

  # neither p or q can be found. return None
  return if left.nil? && right.nil?

  # return non null node
  left.nil? ? right : left
end
