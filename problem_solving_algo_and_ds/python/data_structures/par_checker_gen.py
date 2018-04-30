from stack import *
def par_checker(my_string):
    stack = Stack()

    for i in my_string:
        if i in "([{":
            stack.push(i)
        else:
            if not stack.isEmpty():
                top = stack.pop()
                if not matches(top, i):
                    return False

    if stack.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))
