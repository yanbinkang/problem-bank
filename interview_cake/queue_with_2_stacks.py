class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
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




queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(5)
print queue.dequeue()
# print queue.out_stack.items
queue.enqueue(6)
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.in_stack.items
print queue.out_stack.items
# queue.enqueue(6)
# queue.enqueue(7)
# print queue.dequeue()
# print queue.in_stack.items
# print queue.out_stack.items
