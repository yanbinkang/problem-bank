# http://stackoverflow.com/questions/25952326/find-the-length-of-the-longest-valid-parenthesis-sequence-in-a-string-in-on-t

def longest_valid_parens(string):
    stack = []
    max_length = 0
    last_valid_idx = 0
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        else:
            if stack == []:
                last_valid_idx = i + 1
            else:
                stack.pop()
                if stack == []:
                    max_length = max(max_length, i - last_valid_idx + 1)
                else:
                    max_length = max(max_length, i - stack[-1])

    return max_length
