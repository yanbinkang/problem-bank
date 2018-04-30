"""
https://leetcode.com/problems/product-of-array-except-self/#/description

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

O(n) time without extra space. since the output array does not count as extra space for the purpose of space complexity analysis.

solution: O(n) time O(1) space
"""
def product_except_self(nums):
    # we make an array with the length of the input array to
    # hold our result
    result = [1] * len(nums) # [1, 1, 1, 1]

    product = 1

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    for i in range(len(nums)):
        result[i] = product
        product = product * nums[i]

    product = 1

    # using [1, 2, 3, 4] as eg. we''' have [1, 1, 2, 6]

    # for each integer, we find the product of all the integers
    # after it. since each index in result already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers except at i
    for i in reversed(range(len(nums))):
        result[i] = result[i] * product
        product = product * nums[i]

    return result # [24, 12, 8, 6]

# https://discuss.leetcode.com/topic/18864/simple-java-solution-in-o-n-without-extra-space
def product_except_self_2(nums):
    n = len(nums)

    result = [None] * n

    result[0] = 1

    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    product = 1

    for i in reversed(range(n)):
        result[i] = result[i] * product
        product = product * nums[i]

    return result

"""Brute force
def product_except_self(a_list):
    result = []

    for i in range(len(a_list)):
        product = 1
        for j in range(len(a_list)):
            if i != j:
                product *= a_list[j]
        result.append(product)

    return result


print product_except_self([1, 7, 3, 4])
"""

if __name__ == '__main__':
    print product_except_self([1, 2, 3, 4])
    print product_except_self([1, 0])
    print('\n')
    print product_except_self_2([1, 2, 3, 4])
    print product_except_self_2([1, 0])
