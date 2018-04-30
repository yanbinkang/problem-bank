from stack import *
def par_checker(symbol_string):
    stack = Stack()
    for i in symbol_string:
        if i == "(":
            stack.push(i)
        else:
            if not stack.isEmpty():
                stack.pop()
    if stack.isEmpty():
        return True
    else:
        return False

print(par_checker('((()))'))
print(par_checker('(()'))
