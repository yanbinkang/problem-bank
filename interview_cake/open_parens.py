def get_closing_paren(sentence, opening_paren_index):
    open_nested_parens = 0
    position = opening_paren_index + 1
    for char in sentence[position:]:
        if char == '(':
            open_nested_parens += 1
        elif char == ')':
            if open_nested_parens == 0:
                return position
            else:
                open_nested_parens -= 1
        position += 1
    raise Exception("No closing parenthesis :(")

print(get_closing_paren("Sometimes (when (like  (a))).", 10))


# input = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

# def matching_parens(input, position):
#     count = 0
#     i = position
#     while i < len(input):
#         if input[i] == "(":
#             count += 1
#         elif input[i] == ")":
#             count -= 1

#         if count == 0:
#             return i
#         i += 1
#     return False

# print matching_parens(input, 10) # return 79
# print matching_parens("Sometimes (when (like  (a))).", 10)
