"""
https://leetcode.com/problems/intersection-of-two-arrays/

https://discuss.leetcode.com/topic/45685/three-java-solutions/

Given two arrays, write a function to compute their intersection.

Note: Intersection means elements common to the two arrays
"""
# O(n) time and space
def intersection(nums1, nums2):
    intersect, seen = set(), set()

    for num in nums1:
        seen.add(num)

    for num in nums2:
        if num in seen:
            intersect.add(num)

    return list(intersect)

# sort both arrays and use two pointers. O(nLogn) time, O(n) space
def intersection_alt(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    intersect = set()

    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            intersect.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return list(intersect)


if __name__ == '__main__':
    print intersection([1, 2, 2, 1], [2, 2])
    print intersection([1, 1, 3, 5], [1, 2, 3])
    print intersection([ 'a', 'b', 'b', 'z' ], [ 'a', 'b', 'c' ])
    print('\n')
    print intersection_alt([1, 2, 2, 1], [2, 2])
    print intersection_alt([1, 1, 3, 5], [1, 2, 3])
    print intersection_alt([ 'a', 'b', 'b', 'z' ], [ 'a', 'b', 'c' ])

