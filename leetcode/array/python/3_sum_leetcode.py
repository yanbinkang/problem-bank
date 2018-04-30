"""
https://leetcode.com/problems/3sum/

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

algorithm: The idea is to sort an input array and then run through all indices of a possible first element of a triplet. For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array. Also we want to skip equal elements to avoid duplicates in the answer without making a set or smth like that.

O(n^2) time O(n) space
"""
"""
# https://discuss.leetcode.com/topic/22619/python-easy-to-understand-solution-o-n-n-time

In the inner while loop why do we have to  do l += 1; r -= 1 after skipping duplicates?

If we didn't skip any duplicates, then we definitely have to move r and l.

If we skipped duplicates, why do we still have to move?

Imagine nums = [-4, -1, -1 ... 5]:

i is the element -4
l is the element -1
r is the element 5
s = 0

At this point the first l is part of the result we want and we've skipped l to the last -1 (using the first inner while loop: line 60). In the next iteration we still don't want to include -1 in the result (it'll result in a duplicate). So we need to move l again, and also move r as usual. That's why!

The same explanation works for r
"""
def threeSum(nums):
    res = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s < 0:
                l +=1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])

                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1

                l += 1; r -= 1
    return res

# https://discuss.leetcode.com/topic/8125/concise-o-n-2-java-solution/15
def three_sum(nums):
    nums.sort()
    result = []

    """
    because of left, right = i + 1, len(nums) - 1 you are guaranteed to reach the last 2 indexes always so you can do this instead of iterating to the end of the list:

    for in in range(len(nums) - 2):
        pass
    """
    for i in range(len(nums)):
        # avoid duplicates
        if i != 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]

        left, right = i + 1, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                result.append([nums[i], nums[left], nums[right]])

                # avoid duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # avoid duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

    return result

# TLE
def three_sum_brute_force(nums):
    res = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j: continue

            for k in range(len(nums)):
                if i == k or j == k: continue

                if nums[i] + nums[j] + nums[k] == 0:
                    temp = sorted([nums[i], nums[j], nums[k]])

                    if temp not in res:
                        res.append(temp)

    return res

if __name__ == '__main__':
    print three_sum([-1, 0, 1, 2, -1, -4])
    print threeSum([-1, 0, 1, 2, -1, -4])
    print threeSum([0, 0, 0, 0, 0, 0])

