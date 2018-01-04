"""
http://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/

Given a binary tree, write a function to get the maximum width of the given tree. Width of a tree is maximum of widths of all levels.

Let us consider the below example tree.

         1
        /  \
       2    3
     /  \     \
    4    5     8
              /  \
             6    7
For the above tree,

width of level 1 is 1,

width of level 2 is 2,

width of level 3 is 3

width of level 4 is 2.

So the maximum width of the tree is 3.

algorithm: LEVEL ORDER TRAVERSAL WITH QUEUE

In this method we store all the child nodes at the current level in the queue and then count the total number of nodes after the level order traversal for a particular level is completed. Since the queue now contains all the nodes of the next level, we can easily find out the total number of nodes in the next level by finding the size of queue. We then follow the same procedure for the successive levels. We store and update the maximum number of nodes found at each level.
"""
from binary_tree import *
def max_width(tree):
    maxmax = float('-inf')

    if tree is None: return 0

    queue = [tree]

    while queue:
        maxmax = max(maxmax, len(queue))
        for _ in range(len(queue)):
            node = queue.pop()

            if node.left:
                queue.insert(0, node.left)

            if node.right:
                queue.insert(0, node.right)

    return maxmax

if __name__ == '__main__':
    t = BinaryTree(1)
    t.insert_left(2)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(5)
    t.right.insert_right(8)
    t.right.right.insert_left(6)
    t.right.right.insert_right(7)

    print max_width(t)
