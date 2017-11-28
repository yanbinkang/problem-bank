"""
solution: http://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
steps:
1) Get the middle of the array and make it root
2) Recursively do same for left half and right half
    a) Get the middle of left and make it left child of the root created in step 1.
    b) Get the middle of right half and make it right child of the root created in step 1.
"""
class Node:
    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None

def level_order_traversal(root):
    queue = []

    queue.insert(0, root)

    while queue != []:
        root = queue.pop()

        print root.key

        if root.left_child:
            queue.insert(0, root.left_child)
        if root.right_child:
            queue.insert(0, root.right_child)

def sorted_array_to_bst(a_list, start, end):
    # base case
    if start > end:
        return None

    mid = (start + end) // 2

    root = Node(a_list[mid])

    # recursively construct the left subtree and make it left child of root
    root.left_child = sorted_array_to_bst(a_list, start, mid-1)

    # recursively construct the right subtree and make it right child of the root
    root.right_child = sorted_array_to_bst(a_list, mid+1, end)

    return root

if __name__ == '__main__':
    arr = [8, 10, 12, 15, 16, 20, 25]
    n = len(arr)

    root = sorted_array_to_bst(arr, 0, n-1)
    print "level order traversal of constructed BST:"
    level_order_traversal(root)

