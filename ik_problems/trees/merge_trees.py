"""
solution: http://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/
soln: http://stackoverflow.com/questions/7540546/merging-2-binary-search-trees

solution:
Method 2 (Merge Inorder Traversals)
1) Do inorder traversal of first tree and store the traversal in one temp array arr1[]. This step takes O(m) time.
2) Do inorder traversal of second tree and store the traversal in another temp array arr2[]. This step takes O(n) time.
3) The arrays created in step 1 and 2 are sorted arrays. Merge the two sorted arrays into one array of size m + n. This step takes O(m+n) time.
4) Construct a balanced tree from the merged array using the technique discussed in this post. This step takes O(m+n) time.

Time complexity of this method is O(m+n) which is better than method 1. This method takes O(m+n) time even if the input BSTs are not balanced.
"""
class Node:
    def __init__(self, k):
        self.key = k
        self.left_child = None
        self.right_child = None

def store_inorder(root, res):
    if root == None:
        return None

    if root.left_child:
        store_inorder(root.left_child, res)

    res.append(root.key)

    if root.right_child:
        store_inorder(root.right_child, res)

def merge(arr_1, arr_2):
    result = [None] * (len(arr_1) + len(arr_2))
    i = 0
    j = 0
    k = 0

    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            result[k] = arr_1[i]
            i += 1
        else:
            result[k] = arr_2[j]
            j += 1
        k += 1

    while i < len(arr_1):
            result[k] = arr_1[i]
            i += 1
            k += 1

    while j < len(arr_2):
            result[k] = arr_2[j]
            j += 1
            k += 1

    return result

def sorted_array_to_bst(a_list, first, last):
    if first > last:
        return None

    mid = (first + last) // 2

    root = Node(a_list[mid])

    root.left_child = sorted_array_to_bst(a_list, first, mid-1)
    root.right_child = sorted_array_to_bst(a_list, mid+1, last)

    return root

def level_order(root):
    queue = []

    queue.insert(0, root)

    while queue != []:
        root = queue.pop()

        print root.key

        if root.left_child:
            queue.insert(0, root.left_child)
        if root.right_child:
            queue.insert(0, root.right_child)

def merge_trees(tree_1, tree_2):
    list_1, list_2 = [], []

    store_inorder(tree_1, list_1)
    store_inorder(tree_2, list_2)

    res = merge(list_1, list_2)

    return sorted_array_to_bst(res, 0, len(res)-1)



if __name__ == '__main__':
    """
    Given 2 BSTs. Find If BST2 is subtree of BST1.

              2

             /  \
            1    3


            7
           / \
          6   8
    """

    tree                                        = Node(2)
    tree.left_child                             = Node(1)
    tree.right_child                            = Node(3)

    bst = Node(7)
    bst.left_child = Node(6)
    bst.right_child = Node(8)

    t = merge_trees(tree, bst)

    level_order(t)


