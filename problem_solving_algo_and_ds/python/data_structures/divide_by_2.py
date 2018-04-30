from stack import *
def divide_by_2(num):
    stack = Stack()

    while num > 0:
        rem = num % 2
        stack.push(rem)
        num = num // 2

    cov_num = ""
    while not stack.isEmpty():
        cov_num += str(stack.pop())

    return cov_num

print(divide_by_2(12))
