"""
https://leetcode.com/problems/kth-largest-element-in-an-array/#/description

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 <= k <= array's length.

read: https://en.wikipedia.org/wiki/Quickselect

IMPORTANT: Think of k as the zero-based index in the array where the desired result will be.

Kth Largest
==========
For find_kth_largest with [5, 2, 1, 4, 3] and k = 2, we use (len(nums) - k) as k. Here is why: len(nums) - k == 5 - 2 == 3. When the array is sorted we'll have [1, 2, 3, 4, 5] and zero-based index 3 is where the answer can be found.

Kth Smallest
=========
For find_kth_smallest with [54, 26, 93, 17, 77, 31, 44, 55, 20] and k = 3 we use (k - 1) as k. Here is why: k - 1 == 3 - 1 == 2. When the array is sorted we'll have [17, 20, 26, 31, 44, 54, 55, 77, 93] and zero based index 2 is where the answer can be found.

https://discuss.leetcode.com/topic/14597/solution-explained

O(N) best case / O(N^2) worst case running time + O(1) memory

So how can we improve the above solution and make it O(N) guaranteed? The answer is quite simple, we can randomize the input, so that even when the worst case input would be provided the algorithm wouldn't be affected. So all what it is needed to be done is to shuffle the input.

import random

random.shuffle(list)

Then run the algo
"""
def find_kth_largest(nums, k):
    return quick_select_helper(nums, 0, len(nums)-1, len(nums) - k)

def find_kth_smallest(nums, k):
    return quick_select_helper(nums, 0, len(nums)-1, k - 1)

def quick_select_helper(nums, first, last, k):
    # list contains only one element, return that element
    if first == last:
        return nums[first]

    split_point = partition(nums, first, last)

    # remember k is the zero-based index of the element we're looking for!

    if k == split_point:
        return nums[k]
    elif k < split_point:
        return quick_select_helper(nums, first, split_point-1, k)
    else:
        return quick_select_helper(nums, split_point+1, last, k)


def partition(nums, first, last):
    pivot_val = nums[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        # nums[left_mark] is where its supposed to be in nums, move forward
        while left_mark <= right_mark and nums[left_mark] <= pivot_val:
            left_mark += 1

        # nums[right_mark] is where its supposed to be in nums, move backward
        while right_mark >= left_mark and nums[right_mark] >= pivot_val:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            temp = nums[left_mark]
            nums[left_mark] = nums[right_mark]
            nums[right_mark] = temp

    # split point is right_mark
    # swap pivot value and value at split point ie nums[right_mark]
    temp = nums[first]
    nums[first] = nums[right_mark]
    nums[right_mark] = temp
    return right_mark

# nLogn  time O(1) space
def find_kth_largest_1(nums, k):
    size = len(nums)
    sorted_nums = sorted(nums)
    return sorted_nums[size-k]

if __name__ == '__main__':
    print find_kth_largest([54, 26, 93, 17, 77, 31, 44, 55, 20], 3) #55
    print('\n')
    print find_kth_largest([5, 2, 1, 4, 3], 2) #4
    print('\n')
    print find_kth_smallest([54, 26, 93, 17, 77, 31, 44, 55, 20], 3) #26
    print('\n')
    print find_kth_smallest([5, 2, 1, 4, 3], 2) #2
