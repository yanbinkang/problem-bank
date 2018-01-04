"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note: Intersection means elements common to both arrays

Note:
    * Each element in the result should appear as many times as it shows in both arrays.

    * The result can be in any order.

Follow up:
    * What if the given array is already sorted? How would you optimize your algorithm?

    * What if nums1's size is small compared to nums2's size? Which algorithm is better?

    * What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


https://discuss.leetcode.com/topic/45893/c-hash-table-solution-and-sort-two-pointers-solution-with-time-and-space-complexity

solution to third follow up question:
If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array that fit into the memory, and record the intersections.

If both nums1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort), then read 2 elements from each array at a time in memory, record intersections.

read this: https://discuss.leetcode.com/topic/45992/solution-to-3rd-follow-up-question
"""
def intersect(nums1, nums2):
    if not nums1 or not nums2: return []

    d = {}

    result = []

    for num in nums1:
        d[num] = d.get(num, 0) + 1

    for num in nums2:
        if num in d:
            d[num] -= 1
            if d[num] >= 0:
                result.append(num)

    return result

# binary search
def intersect_2(nums1, nums2):
    n1 = sorted(nums1)
    n2 = sorted(nums2)
    result = []

    i, j = 0, 0

    while i < len(n1) and j < len(n2):
        if n1[i] == n2[j]:
            result.append(n1[i])
            i += 1
            j += 1
        elif n1[i] < n2[j]:
            i += 1
        else:
            j += 1

    return result

if __name__ == '__main__':
    print intersect([1, 2, 2, 1], [2, 2]) # [2, 2]
    print intersect([1], [1, 1])  # [1]
    print intersect([1, 2], [1, 1]) # [1]
    print intersect([], [1]) # []
    print intersect([1], [1, 2]) # [1]

    print ('\n')
    print intersect_2([1, 2, 2, 1], [2, 2])
    print intersect_2([1], [1, 1])


