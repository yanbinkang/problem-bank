from binary_tree import *

"""
https://leetcode.com/problems/path-sum-iii/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


            5
          /   \
         4     8
        /     /  \
       11    13   4
     /   \       /  \
    7     2     5    1

Return 3. The paths that sum to 22 are:

1. 5 -> 4 -> 11 -> 2
2. 4 -> 11 -> 7
3. 5 -> 8 -> 4 -> 5


           1
          /  \
        -2   -3

Return 1. The paths that sum to -1 are:

1. 1 -> -2

            0
          /  \
         1    1

Return 1. The paths that sum to 1 are:

1. 1 -> -2



Time Complexity should be O(N^2) for the worst case and O(NlogN) for balanced binary Tree.

"""

# need to make this pass OJ!
def path_sum_iterative(root, sum):
    if root is None: return 0

    d = {}
    d[0] = 1
    count = 0

    stack = [(root, root.val, d)]

    while stack:
        root, total, d = stack.pop()

        if (total - sum) in d:
            count += 1

        if root.left or root.right:
            d[total] = root.val

        if root.right:
            stack.append( (root.right, total + root.right.val, d) )

        if root.left:
            stack.append( (root.left, total + root.left.val, d) )

    return count

def path_sum(root, sum):
    if not root: return 0

    return helper(root, sum) +\
           path_sum(root.left, sum) +\
           path_sum(root.right, sum)

def helper(root, sum):
    if not root: return 0

    return (1 if root.val == sum else 0) + \
            helper(root.left, sum - root.val) + \
            helper(root.right, sum - root.val)


# https://discuss.leetcode.com/topic/64388/simple-ac-java-solution-dfs
def path_sum_1(root, sum):
    hash_map = {}
    hash_map[0] = 1

    return _helper(root, 0, sum, hash_map)

def _helper(root, sum, target, hash_map):
    if root is None: return 0

    sum += root.val

    result = hash_map.get((sum - target), 0)
    hash_map[sum] = hash_map.get(sum, 0) + 1

    result += _helper(root.left, sum, target, hash_map) +\
              _helper(root.right, sum, target, hash_map)
    hash_map[sum] = hash_map[sum] -  1

    return result





if __name__ == '__main__':
    root = BinaryTree(10)
    root.insert_left(5)
    root.insert_right(-3)

    root.left.insert_left(3)
    root.left.insert_right(2)

    root.right.insert_right(11)

    root.left.left.insert_left(3)
    root.left.left.insert_right(-2)

    root.left.right.insert_right(1)

    t2 = BinaryTree(5)
    t2.insert_left(4)
    t2.insert_right(8)
    t2.left.insert_left(11)
    t2.left.left.insert_left(7)
    t2.left.left.insert_right(2)

    t2.right.insert_left(13)
    t2.right.insert_right(4)
    t2.right.right.insert_right(1)
    t2.right.right.insert_left(5)

    t3 = BinaryTree(0)
    t3.insert_right(1)
    t3.insert_left(1)

    print path_sum(root, 8)
    print('\n')
    print path_sum_1(root, 8)
    print('\n')
    print path_sum_iterative(root, 8)
    print('\n')
    print path_sum_iterative(t2, 22)
    print('\n')
    print path_sum_iterative(t3, 1)
