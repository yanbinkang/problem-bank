"""
http://blog.gainlo.co/index.php/2017/01/05/uber-interview-questions-permutations-array-arrays/?utm_source=email&utm_campaign=email&utm_medium=email

Given a list of array, return a list of arrays, each array is a combination of one element in each given array.

Suppose the input is [[1, 2, 3], [4], [5, 6]], the output should be [[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]]

What pattern do you recognise here? What leetcode question is this similar to?
"""

def permutation_array(nums):
    result = []

    if not nums: return result

    result.append([])

    for num in nums:
        temp = []

        for i in num:
            for elem in result:
                temp.append(elem + [i])
        result = temp

    return result

def permutation_array_backtracking(nums):
    result = []

    if len(nums) == 0: return result

    helper(nums, 0, result, [])

    return result

def helper(nums, start, result, temp_list):
    if len(temp_list) == len(nums):
        result.append(temp_list)
    else:
        for i in range(start, len(nums)):
            for elem in nums[i]:
                helper(nums, i + 1, result, temp_list + [elem])


if __name__ == '__main__':
    nums = [[1, 2, 3], [4], [5, 6]]
    print permutation_array(nums)
    print('\n')
    print permutation_array_backtracking(nums)


"""
result = [[1], [2], [3]]

result = [[1, 4], [2, 4], [3, 4]]

result = [[1, 4, 5], [2, 4, 5], [3, 4, 5], [1, 4, 6], [2, 4, 6], [3, 5, 6]]
"""
