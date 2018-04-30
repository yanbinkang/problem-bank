"""
https://leetcode.com/problems/merge-sorted-array/description/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

https://discuss.leetcode.com/topic/2461/this-is-my-ac-code-may-help-you/2

Algorithm:

Use two pointer and set i, j to the end of the digits in both arrays. Then initialize k to the end of the first array. Compare numbers at the end of both arrays and move the bigger value to the end of the first array. Decrement k and the pointer for the bigger element.

In the end, one array's elements will be moved completely to the end of the first array. If nums2 contains the bigger elements then your work is done cos nums1 will already have the smaller sorted elements.

If nums1 has the bigger elements, the pointer j for nums2 wouldnt have changed at all hence the second while loop will just copy the elements in nums2 to its appropraite location in nums1
"""
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1

if __name__ == '__main__':
    nums1 = [5, 6, 7, 8, None, None, None, None]
    nums2 = [1, 2, 3, 4]

    merge(nums1, 4, nums2, 4)
    print nums1
    print('\n')

    x = [1, 2, 3, 4, None, None, None, None]
    y = [5, 6, 7, 8]

    merge(x, 4, y, 4)
    print x
