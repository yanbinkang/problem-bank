from stack import *

def infix_to_postfix(infix_expr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            top_token = stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = stack.pop()
        else:
            while (not stack.isEmpty()) and (prec[stack.peek()] >= prec[token]):
                postfix_list.append(stack.pop())
            stack.push(token)

    while not stack.isEmpty():
        postfix_list.append(stack.pop())

    return " ".join(postfix_list)


print(infix_to_postfix("( A + B ) * ( C + D )"))
print(infix_to_postfix("( A + B ) * C"))
print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))
