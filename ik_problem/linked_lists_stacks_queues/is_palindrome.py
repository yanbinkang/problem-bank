"""
ref: http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
METHOD 1 (Use a Stack)
A simple solution is to use a stack of list nodes. This mainly involves three steps.
1) Traverse the given list from head to tail and push every visited node to stack.
2) Traverse the list again. For every visited node, pop a node from stack and compare data of popped node with currently visited node.
3) If all nodes matched, then return true, else false.

Time complexity of above method is O(n), but it requires O(n) extra space. Following methods solve this with constant extra space
"""
def is_palindrome(sll):
    stack = []
    current = sll.head

    while current != None:
        stack.append(current.get_data())
        current = current.get_next()

    _head = sll.head

    while _head != None and stack != []:
        item = stack.pop()
        ll = _head.get_data()

        if item != ll:
            return False

        _head = _head.get_next()

    return True
