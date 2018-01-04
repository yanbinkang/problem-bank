"""
http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/

            1
          /   \
        2      3
      /  \
    4     5

Step 1 Creates an empty stack: S = NULL

Step 2 sets current as address of root: current -> 1

Step 3 Pushes the current node and set current = current->left until current is NULL
     current -> 1
     push 1: Stack S -> 1
     current -> 2
     push 2: Stack S -> 2, 1
     current -> 4
     push 4: Stack S -> 4, 2, 1
     current = NULL

Step 4 pops from S
     a) Pop 4: Stack S -> 2, 1
     b) print "4"
     c) current = NULL /*right of 4 */ and go to step 3
Since current is NULL step 3 doesn't do anything.

Step 4 pops again.
     a) Pop 2: Stack S -> 1
     b) print "2"
     c) current -> 5/*right of 2 */ and go to step 3

Step 3 pushes 5 to stack and makes current NULL
     Stack S -> 5, 1
     current = NULL

Step 4 pops from S
     a) Pop 5: Stack S -> 1
     b) print "5"
     c) current = NULL /*right of 5 */ and go to step 3
Since current is NULL step 3 doesn't do anything

Step 4 pops again.
     a) Pop 1: Stack S -> NULL
     b) print "1"
     c) current -> 3 /*right of 5 */

Step 3 pushes 3 to stack and makes current NULL
     Stack S -> 3
     current = NULL

Step 4 pops from S
     a) Pop 3: Stack S -> NULL
     b) print "3"
     c) current = NULL /*right of 3 */

Traversal is done now as stack S is empty and current is NULL.
"""
from binary_tree import *
def inorder(root):
    current = root
    stack = []
    done = False

    while not done:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if stack:
                current = stack.pop()
                print current.val,
                current = current.right
            else:
                done = True

def inorder_1(root):
    stack = []
    result = []


    if not root: return []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        result.append(root.val)
        root = root.right

    return result

# Time Complexity: O(n)

if __name__ == '__main__':
    """ Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """

    t = BinaryTree(1)
    t.insert_left(2)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(5)

    inorder(t)
