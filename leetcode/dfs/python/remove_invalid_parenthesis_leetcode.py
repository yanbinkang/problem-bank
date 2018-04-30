"""
https://leetcode.com/problems/remove-invalid-parentheses/#/description

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""

"""
# https://discuss.leetcode.com/topic/28827/share-my-java-bfs-solution

The idea is straightforward, with the input string s, we generate all possible states by removing one ( or ), check if they are valid, if found valid ones on the current level, put them to the final result list and we are done, otherwise, add them to a queue and carry on to the next level.

The good thing of using BFS is that we can guarantee the number of parentheses that need to be removed is minimal, also no recursion call is needed in BFS.
"""
def remove_invalid_parenthesis_1(s):
    result = []

    if not s: return result

    visited = set()
    queue = []

    # initialize
    queue.append(s)
    visited.add(s)

    found = False

    while queue:
        s = queue.pop()

        if is_valid(s):
            result.append(s)
            found = True

        if found: continue

        # generate all possible states
        for i in range(len(s)):
            # we only try to remove left or right paren
            if s[i] != '(' and s[i] != ')':
                continue

            candidate = s[:i] + s[i + 1:]

            if candidate not in visited:
                # for each state, if its not in visited, add it to the queue
                queue.insert(0, candidate)
                visited.add(candidate)

    return result

def is_valid(s):
    count = 0

    for i in range(len(s)):
        char = s[i]

        if char == '(':
            count += 1
        if char == ')':
            if count == 0:
                return False

            count -= 1

    return count == 0

# "()())()" => "(())()"
# "()())()" => "()()()"


"""
ref: https://discuss.leetcode.com/topic/34875/easy-short-concise-and-fast-java-dfs-3-ms-solution


Time complexity: https://discuss.leetcode.com/topic/34875/easy-short-concise-and-fast-java-dfs-3-ms-solution/13
"""
def remove_invalid_parenthesis(s):
    result = []

    remove(s, result, 0, 0, '()')

    return result

def remove(s, result, last_i, last_j, par):
    count = 0

    for i in range(last_i, len(s)):
        # count += (s[i] == par[0]) - (s[i] == par[1])

        # Search for a mismatch
        if s[i] == par[0]:
            count += 1

        if s[i] == par[1]:
            count -= 1

        if count < 0:
            break

    # Remove a parenthesis
    # We've found an extra ')'. Remove the first ')' starting from the left
    if count < 0:
        for j in range(last_j, i + 1):
            # if the char we're looking at is ')' and it is the first char
            # if the char we're looking at is ')' and the previous char is not '('
            if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                candidate = s[:j] + s[j + 1:]
                remove(candidate, result, i, j, par)

        return

    # If no mismatch, try reverse of the string
    reversed_s = s[::-1]

    if par[0] == '(': # finished left to right
        remove(reversed_s, result, 0, 0, ')(')
    else:
        result.append(reversed_s) # both sides are finished, got your answer




if __name__ == '__main__':
    print remove_invalid_parenthesis('()())()')
    print('\n')
    print remove_invalid_parenthesis_1('()())()')
    print remove_invalid_parenthesis_1(')d))')

