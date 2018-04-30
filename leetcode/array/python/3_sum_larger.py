"""
You are given an array A of N non-negative integers. For a given integer M, count how many triplets of A have a sum larger than M.

A triplet is a tuple (A[i], A[j], A[k]) where i < j < k

Example:

a = [3, 1, 2, 5]
m = 8

Return 2

The two triplets with sum greater than 8 are (3, 2, 5) and (3, 1, 5)
"""

def threeSumLarger(nums, target):
    nums.sort()

    count = 0

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total > target:
                count += right - left
                right -= 1
            else:
                left += 1

    return count

if __name__ == '__main__':
    print threeSumLarger([3, 1, 2, 5], 8)
    print threeSumLarger([5, 1, 3, 4, 7], 12)

