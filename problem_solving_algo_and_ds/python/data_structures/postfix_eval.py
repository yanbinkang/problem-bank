# Evaluate a postfix expression

from stack import *

def postfix_eval(postfix_expr):
    stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            stack.push(int(token))
        else:
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            result = do_math(token, operand_1, operand_2)
            stack.push(result)

    return stack.pop()

def do_math(op, op_1, op_2):
    if op == "*":
        return op_1 * op_2
    elif op == "/":
        return op_1 / op_2
    elif op == "+":
        return op_1 + op_2
    else:
        return op_1 - op_2


print(postfix_eval("7 8 + 3 2 + /"))
