def bracket_validator(some_string):
    stack = []
    token_list = some_string.split()
    for token in token_list:
        if token in "{[(":
            stack.append(token)
        else:
            if not stack == []:
                top = stack.pop()
                if not matches(top, token):
                    return False

    if stack == []:
        return True
    else:
        return False

def matches(open, close):
    opens = "{[("
    closers = "}])"
    return opens.index(open) == closers.index(close)


print bracket_validator("{ [ ] ( ) }")
