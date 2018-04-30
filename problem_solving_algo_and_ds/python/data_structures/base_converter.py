from stack import *

def base_converter(num, base):
    stack = Stack()
    digits = "0123456789ABCDEF"

    while num > 0:
        rem = num % base
        stack.push(rem)
        num = num // base

    conv_num = ""

    while not stack.isEmpty():
        conv_num += digits[stack.pop()]

    return conv_num

print(base_converter(34, 8))
