"""
https://leetcode.com/problems/permutation-sequence/

The set [1,2,3,..,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

https://discuss.leetcode.com/topic/19269/share-my-python-solution-with-detailed-explanation

https://discuss.leetcode.com/topic/17348/explain-like-i-m-five-java-solution-in-o-n

https://discuss.leetcode.com/topic/5081/an-iterative-solution-for-reference
"""
import math

def get_permutation_1(n, k):
    result, nums = '', range(1, n + 1)

    # generate and store factorial
    factorial_col = [None for i in range(n + 1)]
    factorial_col[0] = 1
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
        factorial_col[i] = factorial

    k -= 1

    while n:
        n -= 1
        # get the index of current digit
        index, k = divmod(k, factorial_col[n])

        # remove handled number
        result += str(nums.pop(index))

    return result

def get_permutation(n, k):
    nums = map(str, range(1, 10))

    k -= 1
    factorial = 1

    for i in range(1, n):
        factorial *= i

    result = []

    for i in reversed(range(n)):
        result.append(nums[k / factorial])
        nums.remove(nums[k / factorial])

        if i != 0:
            k %= factorial
            factorial /= i

    return ''.join(result)


if __name__ == '__main__':
    print get_permutation(9, 54494)
    print get_permutation(8, 37565)
    print('\n')
    print get_permutation_1(3, 2)
    print get_permutation_1(9, 54494)
    print get_permutation_1(8, 37565)


