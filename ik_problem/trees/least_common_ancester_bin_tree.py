"""
solution: http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

Method 1 (By Storing root to n1 and root to n2 paths):
Following is simple O(n) algorithm to find LCA of n1 and n2.
1) Find path from root to n1 and store it in a vector or array.
2) Find path from root to n2 and store it in another vector or array.
3) Traverse both paths till the values in arrays are same. Return the common element just before the mismatch.
"""
class Node:
    def __init__(self, k):
        self.key = k
        self.left_child = None
        self.right_child = None


def find_path(root, k, path=[]):

    # base case
    if root == None:
        return False

    # store this node in path array. The node will be removed if not in path from rook to k
    path.append(root.key)

    # see if k is the same as root's key
    if root.key == k:
        return True

    # check if k is found in left or right sub-tree
    if root.left_child and find_path(root.left_child, k, path) or \
        root.right_child and find_path(root.right_child, k, path):
        return True

    path.pop()
    return False


def find_lca(root, n1, n2):
    path_1, path_2 = [], []
    if ( not find_path(root, n1, path_1) or not find_path(root, n2, path_2)):
        return -1

    i = 0
    while i < len(path_1) and i < len(path_2):
        if path_1[i] != path_2[i]:
            break
        i += 1

    return path_1[i-1]


if __name__ == '__main__':
    tree                            = Node(1)
    tree.left_child                 = Node(2)
    tree.right_child                = Node(3)
    tree.left_child.left_child      = Node(4)
    tree.left_child.right_child     = Node(5)
    tree.right_child.left_child     = Node(6)
    tree.right_child.right_child    = Node(7)

    print find_lca(tree, 4, 5)
    print find_lca(tree, 4, 6)
    print find_lca(tree, 3, 4)
    print find_lca(tree, 2, 4)
