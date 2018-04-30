"""
https://leetcode.com/problems/min-stack/#/description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

idea:
0. Maintain 2 lists stack and min_stack

1. Push :- Just keep pushing unto stack. Push an item into min_stack only if that item is <= the last item in min_stack

2. pop :- remove last item on stack and save the value. Remove from min_stack only if removed item is same as last item on min_stack

Rest of operations just return the last item on the lists
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x) # append to stack

        if self.min_stack and x <= self.min_stack[-1]:
            self.min_stack.append(x)

        if not self.min_stack:
            self.min_stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        item = self.stack.pop()

        if item == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]



if __name__ == '__main__':
    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    print 'Minimum element on stack is %s' % (obj.getMin())
    print('\n')
    print 'stack is %s and self.stack is %s' % (obj.stack, obj.min_stack)
    print('\n')
    obj.pop()
    print 'after pop operation, stack is %s and self.stack is %s' % (obj.stack, obj.min_stack)
    print('\n')
    print 'Minimum element on stack is %s' % (obj.getMin())
    print('\n')
    print 'stack is %s and self.stack is %s' % (obj.stack, obj.min_stack)
