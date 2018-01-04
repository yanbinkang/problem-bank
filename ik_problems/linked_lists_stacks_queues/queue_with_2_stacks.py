# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise ValueError('Queue is empty')
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())

            return self.out_stack.pop()

        if not self.out_stack.is_empty():
            return self.out_stack.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)

print q.dequeue()
print q.dequeue()
print q.dequeue()
