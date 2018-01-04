"""
solution: http://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/
"""
class Node:
    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None

def insert(node, key):
    if node == None:
        return Node(key)

    if key < node.key:
        node.left_child = insert(node.left_child, key)
    elif key > node.key:
        node.right_child = insert(node.right_child, key)

    return node

def kth_largest(root, k):
    # count = 0
    kth_largest_util(root, k, 0)

def kth_largest_util(root, k, count):
    # base case, the second condition is important to avoid unnecessary recursive calls
    if root == None or count >= k:
        return

    # follow reverse inorder traversal so that the largest element is visited first
    kth_largest_util(root.right_child, k, count)

    # increment count of visited nodes
    count += 1

    # if c becomes k, then this is the k'th largest
    if count == k:
        print "K'th largest element is %s" % (root.key)
        return

    # recurse for the left subtree
    kth_largest_util(root.left_child, k, count)

if __name__ == '__main__':
    """
                50
              /    \
            30     70
           /  \   /  \
          20  40 60   80
    """
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    for k in range(1, 8):
        kth_largest(root, k)
