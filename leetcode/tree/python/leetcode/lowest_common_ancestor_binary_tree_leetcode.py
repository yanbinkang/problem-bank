from binary_tree import *

"""
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
"""

def lowest_common_ancestor(root, p, q):
    if root == None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q) #find p or q in left subtree
    right = lowest_common_ancestor(root.right, p, q) #find p or q in right subtree

    # three possible return values

    if left is not None and right is not None: return root # p and q can be found on root's left or right subtree. meaning root is LCA

    if left == None and right == None: return None # neither p or q cannot be found. return None

    return left if left else right # return non null node

"""
https://discuss.leetcode.com/topic/27479/java-python-iterative-solution

To find the lowest common ancestor, we need to find where is p and q and a way to track their ancestors. A parent pointer for each node found is good for the job. After we found both p and q, we create a set of p's ancestors. Then we travel through q's ancestors, the first one appears in p's is our answer.
"""
def lowest_common_ancestor_iterative(root, p, q):
    stack = [root]
    parent = {root: None}

    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    ancestors = set()

    while p:
        ancestors.add(p)
        p = parent[p]

    while q not in ancestors:
        q = parent[q]

    return q

if __name__ == '__main__':
    """
                                        3
                                      /   \
                                     6     8
                                    /  \    \
                                   2   11    13
                                      /  \   /
                                     9    5  7

lca(8, 7) => 8
lca(8, 11) => 3
    """
    tree = BinaryTree(3)

    tree.insert_left(6)
    tree.insert_right(8)

    tree.left.insert_left(2)
    tree.left.insert_right(11)
    tree.right.insert_right(13)

    tree.left.right.insert_left(9)
    tree.left.right.insert_right(5)
    tree.right.right.insert_left(7)

    print "Test for recursive code"
    print "------"
    p1 = tree.right
    q1 = tree.right.right.left
    res = lowest_common_ancestor(tree, p1, q1)
    print res.val #8

    print('\n')
    p2 = tree.right
    q2 = tree.left.right

    res1 = lowest_common_ancestor(tree, p2, q2)
    print res1.val #3


    print('\n')
    print "Test for itereative code"
    print "------"
    a = lowest_common_ancestor_iterative(tree, p1, q1)
    print a.val #8
    print('\n')
    b = lowest_common_ancestor_iterative(tree, p2, q2)
    print b.val



