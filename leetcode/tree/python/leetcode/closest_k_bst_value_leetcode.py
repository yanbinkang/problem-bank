from binary_tree import BinaryTree

"""
https://leetcode.com/problems/closest-binary-search-tree-value-ii/

https://discuss.leetcode.com/topic/22940/ac-clean-java-solution-using-two-stacks
"""

def closest_k_values(root, target, k):
    result = []
    predecessors = []
    successors = []

    inorder(root, target, False, predecessors) # will return the next smaller node to target
    inorder(root, target, True, successors) # will return the next larger node to target

    while k > 0:
        if not predecessors:
            result.append(successors.pop())
        elif not successors:
            result.append(predecessors.pop())
        elif abs(predecessors[-1] - target) < abs(successors[-1] - target):
            result.append(predecessors.pop())
        else:
            result.append(successors.pop())

        k -= 1
    return result

def inorder(root, target, reverse, stack):
    if root is None: return

    if reverse:
        inorder(root.right, target, reverse, stack)
    else:
        inorder(root.left, target, reverse, stack)

    """
    Why this early return is useful:
    predecessors (reverse == False) cares about the smallest node closest to the target and successors (reverse == True) cares about the next largest node closest to target. Hence, when collating predecessors we don't care about values greater than target and when collating successors we dont care about values smaller than target. So we return early so we don't have to visit the whole tree.
    """
    if (reverse and root.val <= target) \
        or (not reverse and root.val > target):
            return
    stack.append(root.val)

    if reverse:
        inorder(root.left, target, reverse, stack)
    else:
        inorder(root.right, target, reverse, stack)


if __name__ == '__main__':
    tree =  BinaryTree(17)
    tree.insert_left(5)
    tree.insert_right(35)

    tree.left.insert_left(2)

    tree.right.insert_left(29)

    print closest_k_values(tree, 3, 2)
