def has_matching_parantheses(str_expression):
    stack = []
    token_list = []

    for elem in str_expression:
        if elem in "({[)}]":
            token_list.append(elem)

    if len(token_list) % 2 != 0:
        return False

    for elem in token_list:
        if elem in "({[":
            stack.append(elem)
        else:
            if not stack == []:
                top = stack.pop()
                if not matching(top, elem):
                    return False

    return len(stack) == 0

def matching(open, close):
    opens = "({["
    closes = ")}]"

    return opens.index(open) == closes.index(close)

print has_matching_parantheses("( ( 1 + 2 ) * 3 )")
print has_matching_parantheses("} ( 1 * 2) + 3 * ( 5 - 6)")
