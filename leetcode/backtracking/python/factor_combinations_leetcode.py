"""
https://leetcode.com/problems/factor-combinations/

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:
You may assume that n is always positive.
Factors should be greater than 1 and less than n.

Examples:
input: 1
output:
[]

input: 37
output:
[]

input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""
import math
def get_factors(n):
    result = []

    if not n: return result

    factors(result, [], n, 2)

    return result

def factors(result, temp_list, n, start):
    if n < 4:
        return

    for i in range(start, int(math.sqrt(n) + 1)):
        if n % i == 0:
            temp_list.append(i)
            temp_list.append(n / i)

            result.append([] + temp_list)

            temp_list.pop()

            factors(result, temp_list, n / i, i)
            temp_list.pop()

# def get_factors(n):
#     result = []

#     if not n: return result

#     if n <= 3:
#         return result

#     helper(n, result, 2, [])

#     return result

# def helper(n, result, start, temp_list):
#     if n == 1 and len(temp_list) > 1:
#         result.append([] + temp_list)
#         return

#     for i in range(start, int(math.sqrt(n) + 1)):
#         if n % i != 0:
#             continue

#         temp_list.append(i)
#         helper(n / i, result, i, temp_list)
#         temp_list.pop()

#     i = n
#     temp_list.append(i)
#     helper(n / i, result, i, temp_list)
#     temp_list.pop()

# TLE
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        if not n: return result

        self.helper(n, result, 2, [])

        return result

    def helper(self, n, result, start, temp_list):
        if n <= 1:
            if len(temp_list) > 1:
                res = sorted([] + temp_list)
                if res not in result:
                    result.append(res)
        else:
            for i in range(start, n + 1):
                if n % i == 0:
                    temp_list.append(i)
                    self.helper(n / i, result, i, temp_list)
                    temp_list.pop()

if __name__ == '__main__':
    print get_factors(23848713)
    print get_factors(32)
    # print get_factors_alt(24)
    # print get_factors_alt(32)
    # print get_factors_alt(23848713)

