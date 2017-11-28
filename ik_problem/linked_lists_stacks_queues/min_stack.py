class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, item):
        self.stack.push(item)

        if item <= self.min_stack.peek():
            self.min_stack.push(item)

    def pop(self):
        item = self.min_stack.pop()

        if item == self.min_stack.peek():
            self.min_stack.pop()

        return item

    def get_min(self):
        return self.min_stack.peek()
