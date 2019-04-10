"""
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x, y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
"""
'''
Brute force:

def find_pairs_with_given_difference(arr, k):
    result = []

    if len(arr) <= 1: return result

    for y in arr:
        for x in arr:
            if x - y == k:
                result.append([x, y])

    return result
'''


def find_pairs_with_given_difference(arr, k):
    result = []
    d = {}

    for x in arr:
        # store compliment as key
        d[x - k] = x

    for y in arr:
        if y in d:
            result.append([d[y], y])

    return result


def all_pairs_equal_target(nums, target):
    d = {}
    result = []

    for num in nums:
        d[target - num] = True

    for num in nums:
        if num in d:
            result.append([target - num, num])

    return result


def all_pairs_equal_target_1(nums, target):
    d = {}
    result = []

    for num in nums:
        d[target - num] = num

    for num in nums:
        if num in d:
            result.append([num, d[num]])

    return result


def all_pairs_equal_target_2(nums, target):
    s = set(nums)
    result = []

    for num in nums:
        if target - num in s:
            result.append([target - num, num])

    return result


if __name__ == "__main__":
    print(find_pairs_with_given_difference([0, -1, -2, 2, 1], 1))
    print("\n")
    print(find_pairs_with_given_difference([1, 7, 5, 3, 32, 17, 12], 17))
    print("\n")
    print(all_pairs_equal_target([1, 20, 99, 70, 80, 3], 100))
    # print(all_pairs_equal_target_alt([1, 20, 99, 70, 80, 3], 100))
    '''
    d = {}
    result = []

    num = 1
    {99: True}

    num = 20
    {99: True, 80: True}

    num = 99
    {99: True, 80: True, 1: True}

    num = 70
    {99: True, 80: True, 1: True, 30: True}

    num = 80
    {99: True, 80: True, 1: True, 30: True, 20: True}

    num = 3
    {99: True, 80: True, 1: True, 30: True, 20: True, 97: True}

    ====
    num = 1
    result = [[99, 1]]

    num = 20
    result = [[99, 1], [80, 20]]

    num = 99
    result = [[99, 1], [80, 20], [1, 99]]

    num = 70
    result = [[99, 1], [80, 20], [1, 99]]

    num = 80
    result = [[99, 1], [80, 20], [1, 99], [20, 80]]

    num = 3
    result = [[99, 1], [80, 20], [1, 99], [20, 80]]
    '''
