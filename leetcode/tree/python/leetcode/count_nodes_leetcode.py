from binary_tree import *

# https://leetcode.com/problems/count-complete-tree-nodes/
# http://www.programcreek.com/2014/06/leetcode-count-complete-tree-nodes-java/

def count_nodes(root):
    if root == None:
        return 0

    height_left, height_right = 0, 0

    l, r = root, root

    while l:
        height_left += 1
        l = l.left

    while r:
        height_right += 1
        r = r.right

    if height_left == height_right:
        return pow(2, height_left) - 1

    return 1 + count_nodes(root.left) + count_nodes(root.right)
