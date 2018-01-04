class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, items):
        self.stack.push(item)

        if item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if (item == self.max_stack.peek()):
            self.max_stack.pop()
        return item

    def get_max(self):
        return self.max_stack.peek()
