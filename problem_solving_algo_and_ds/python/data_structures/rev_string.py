from stack import *
def rev_string(my_str):
    stack = Stack()
    rev_str = ""
    for ch in my_str:
        stack.push(ch)
    while not stack.isEmpty():
        rev_str += stack.pop()

    return rev_str

print(rev_string("apple"))
