from stack import *


def par_checker(symbol_string):
    stack = Stack()

    for paren in symbol_string:
        if paren == "(":
            stack.push(paren)
        else:
            if not stack.isEmpty():
                stack.pop()

    return stack.isEmpty()


print(par_checker('((()))'))
print(par_checker('(()'))
