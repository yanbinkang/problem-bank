"""
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

http://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/

https://discuss.leetcode.com/topic/21217/java-o-n-and-o-1-extra-space
"""
def verify_preorder(pre_order):
    root = float("-inf")

    s = []

    for value in pre_order:
        if value < root:
            return False

        # we must be branching to right subtree
        while s and s[-1] < value:
            root = s.pop()

        s.append(value)

    return True

if __name__ == '__main__':
    pre1 = [40, 30, 35, 80, 100]
    """
         40
       /   \
     30    80
      \      \
      35     100
    """
    pre2 = [40, 30, 35, 20, 80, 100]

    print verify_preorder(pre1)
    print('\n')
    print verify_preorder(pre2)

    # value = 35
    # s = [40, 35], root = 30
    # call func
    # pre_order(root)

    # def pre_order(root):
    #   if root:
    #       print root.val
    #       pre_order(root.left)
    #       pre_order(root.right)
