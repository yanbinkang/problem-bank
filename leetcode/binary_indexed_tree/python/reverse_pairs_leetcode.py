"""
https://leetcode.com/problems/reverse-pairs/#/description

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:
Input: [1,3,2,3,1]
Output: 2

Example2:
Input: [2,4,3,5,1]
Output: 3

Note:
    1) The length of the given array will not exceed 50,000.
    2) All the numbers in the input array are in the range of 32-bit integer.

GREAT EXPLANATION: https://discuss.leetcode.com/topic/79227/general-principles-behind-problems-similar-to-reverse-pairs
"""
def reverse_pairs(nums):
    result = 0
    bit = [0] * (len(nums) + 1)
    copy = sorted(nums)

    for num in nums:
        result += prefix_sum(bit, index(copy, 2 * num + 1))

        update(bit, index(copy, num))

    return result

# binary search
def index(arr, val):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = l + ((r - l) >> 1)
        # m = (l + r) / 2 # same as above

        if arr[m] >= val:
            r = m - 1
        else:
            l = m + 1

    return l


def prefix_sum(bit, index):
    index += 1

    total = 0

    while index < len(bit):
        total += bit[index]
        index += (index & -index)

    return total

def update(bit, index):
    index += 1

    while index > 0:
        bit[index] += 1
        index -= (index & -index)

def reverse_pairs_merge_sort(nums):
    return reverse_pairs_sub(nums, 0, len(nums) - 1)

def reverse_pairs_sub(nums, l, r):
    if l >= r: return 0

    m = l + ((r - l) >> 1)
    res = reverse_pairs_sub(nums, l, m) + reverse_pairs_sub(nums, m + 1, r)
    merge = [None] * (r - l + 1)

    i = l
    j = m + 1
    k = 0
    p = m + 1

    while i <= m:
        while p <= r and nums[i] > 2 * nums[p]:
            p += 1

        res += p - (m + 1)

        while j <= r and nums[i] >= nums[j]:
            merge[k] = nums[j]
            k += 1
            j += 1

        merge[k] = nums[i]

        k += 1
        i += 1

    while j <= r:
        merge[k] = nums[j]
        k += 1
        j += 1



if __name__ == '__main__':
    print reverse_pairs([1, 3, 2, 3, 1])
    print reverse_pairs([2, 4, 3, 5, 1])
