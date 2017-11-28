from binary_tree import BinaryTree
"""

solution:
We can solve this problem using BST properties. We can recursively traverse the BST from root. The main idea of the solution is, while traversing from top to bottom, the first node n we encounter with value between n1 and n2, i.e., n1 < n < n2 or same as one of the n1 or n2, is LCA of n1 and n2 (assuming that n1 < n2). So just recursively traverse the BST in, if node's value is greater than both n1 and n2 then our LCA lies in left side of the node, if it's is smaller than both n1 and n2, then LCA lies on right side. Otherwise root is LCA (assuming that both n1 and n2 are present in BST)
"""
def lca(root, n1, n2):
    if root == None:
        return None

    if root.key > n1 and root.key > n2:
        return lca(root.left_child, n1, n2)

    if root.key < n1 and root.key < n2:
        return lca(root.right_child, n1, n2)

    return root

if __name__ == '__main__':
    root                                    = BinaryTree(20)
    root.left_child                         = BinaryTree(8)
    root.right_child                        = BinaryTree(22)
    root.left_child.left_child              = BinaryTree(4)
    root.left_child.right_child             = BinaryTree(12)
    root.left_child.right_child.left_child  = BinaryTree(10)
    root.left_child.right_child.right_child = BinaryTree(14)

    n1, n2 = 10, 14

    t = lca(root, n1, n2)

    print "LCA of %s and %s is %d" % (n1, n2, t.key)
