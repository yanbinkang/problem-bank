"""
http://www.geeksforgeeks.org/double-tree/

http://cslibrary.stanford.edu/110/BinaryTrees.html

For each node in a binary search tree, create a new duplicate node, and insert the duplicate as the left child of the original node. The resulting tree should still be a binary search tree.
 So the tree...

    2
   / \
  1   3

 is changed to...

       2
      / \
     2   3
    /   /
   1   3
  /
 1

Time Complexity: O(n) where n is the number of nodes in the tree.
"""
from binary_tree import *
def double_tree(root):
    if root is None: return

    temp = BinaryTree(root.val)

    old_left = root.left if root.left else None

    temp.left = old_left

    root.left = temp

    double_tree(root.left.left)
    double_tree(root.right)

    return root

def double_tree_1(root):
    if root is None:
        return

    double_tree_1(root.left)
    double_tree_1(root.right)

    old_left = root.left
    root.left = BinaryTree(root.val)
    root.left.left = old_left

    return root

def level_order(root):
    queue = [root]
    result = []

    while queue:
        temp = []
        for _ in range(len(queue)):
            node = queue.pop()

            temp.append(node.val)

            if node.left:
                queue.insert(0, node.left)

            if node.right:
                queue.insert(0, node.right)

        result.append(temp)

    print result

def morris_traversal(root):
    current = root
    result = []

    while current:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left

            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right


    print result


if __name__ == '__main__':
    t = BinaryTree(2)
    t.insert_left(1)
    t.insert_right(3)

    t1 = BinaryTree(1)
    t1.insert_left(2)
    t1.insert_right(3)
    t1.left.insert_left(4)
    t1.left.insert_right(5)

    t3 = BinaryTree(2)
    t3.insert_left(1)
    t3.insert_right(3)

    result = double_tree(t)
    result1 = double_tree(t1)
    result2 = double_tree_1(t3)

    # test level order traversal
    level_order(result)
    print('\n')
    level_order(result1)
    print('\n')
    level_order(result2)
    print('\n')

    morris_traversal(result)
    print('\n')
    morris_traversal(result1)




