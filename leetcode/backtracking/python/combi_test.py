"""
https://leetcode.com/problems/combinations/
"""

def combine(n, k):
    result = []

    if not n or not k:
        return result

    helper(n, k, result, 1, [])

    return result

def helper(n, k, result, start, temp_list):
    if k == 0:
        result.append([] + temp_list)
    else:
        if n - start + 1 >= k:
            for i in range(start, n + 1):
                temp_list.append(i)
                helper(n, k - 1, result, i + 1, temp_list)
                temp_list.pop()


if __name__ == '__main__':
    print combine(4, 2)
    print('\n')
    print combine(10, 7)
    print('\n')
    print combine(20, 16)
