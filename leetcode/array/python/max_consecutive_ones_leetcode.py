"""
https://leetcode.com/problems/max-consecutive-ones/#/description

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:
 - The input array will only contain 0 and 1.
 - The length of input array is a positive integer and will not exceed 10,000

solution: https://discuss.leetcode.com/topic/75426/concise-o-n-solution-slight-modification-of-two-pointers-and-1-liner-solution-for-fun/5

O(n) time O(1) space

Algo: initialize count, max_so_far to 0.

Now iterate the array, if element == 1, increment count by one and find the max_so_far.

Else when element is 0, set count to 0.

In the end return max_so_far.
"""
def find_max_consecutive_ones_2(nums):
    count = 0
    max_so_far = 0

    for num in nums:
        if num == 1:
            count += 1
            max_so_far = max(max_so_far, count)
        else:
            count = 0
    return max_so_far

def find_max_consecutive_ones(nums):
    # without this we might not find correct answer if max consecutive 1's at the end of array
    nums.append(0)

    lo = 0; result = 0

    for hi, num in enumerate(nums):
        if num == 0:
            result = max(result, hi - lo)

            # move lo since we've covered all elements up to this point
            lo = hi + 1

    return result

"""
Use two pointers l and r. if num == 1 find the max and then move r pointer. Else move r, l to i. Finally return max
"""
def find_max_consecutive_ones_3(nums):
    l, r, i_max = 0, 0, 0

    for i in range(len(nums)):
        if nums[i] == 1:
            i_max = max(i_max, r - l + 1)
            r += 1
        else:
            l = r = i

    return i_max


import itertools
def find_max_consecutive_ones_1(nums):
    counter = [len(list(g)) for k, g in itertools.groupby(nums) if k == 1]

    return max(counter) if counter else 0


if __name__ == '__main__':
    print find_max_consecutive_ones([1,1,0,1,1,1])
    print('\n')
    print find_max_consecutive_ones_1([1,1,0,1,1,1])
    print('\n')
    print find_max_consecutive_ones_1([1,1,0,1,1,1])
    print('\n')
    print(find_max_consecutive_ones_3([1,1,0,1,1,1]))
