"""
https://leetcode.com/problems/expression-add-operators/#/description

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []

ref: https://discuss.leetcode.com/topic/24523/java-standard-backtrace-ac-solutoin-short-and-clear

explanation of last recursive call:

for example, if you have a sequence of 12345 and you have proceeded to 1 + 2 + 3, now your eval is 6 right? If you want to add a * between 3 and 4, you would take 3 as the digit to be multiplied, so you want to take it out from the existing eval. You have 1 + 2 + 3 * 4 and the eval now is (1 + 2 + 3) - 3 + (3 * 4).

Time Complexity: O(4^n)
"""
def add_operators(num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    res = []

    if not num or len(num) == 0: return res

    helper(res, '', num, target, 0, 0, 0)

    return res

def helper(res, path, num, target, pos, prev, last_added):
    if pos == len(num):
        if target == prev:
            res.append(path)
        return

    for i in range(pos, len(num)):
        if num[pos] == '0' and i != pos: # still don't understand this
            break

        cur = int(num[pos:i + 1])

        if pos == 0:
            helper(res, path + str(cur), num, target, i + 1, last_added + cur, last_added+ cur)
        else:
            helper(res, path + '+' + str(cur), num, target, i + 1, prev + cur, cur)

            helper(res, path + '-' + str(cur), num, target, i + 1, prev - cur, -cur)

            helper(res, path + '*' + str(cur), num, target, i + 1, prev - last_added + last_added * cur, last_added * cur)

if __name__ == '__main__':
    print add_operators('12', 3)
    print('\n')
    print add_operators('123', 6)
    print('\n')
    print add_operators('232', 8)
    print('\n')
    print add_operators('105', 5)
    print('\n')
    print add_operators('00', 0)
    print('\n')
    print add_operators('3456237490', '9191')
