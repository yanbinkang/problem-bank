"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

O(log(min(m, n))) where m and n are the lengths of the two arrays.
"""
def findMedianSortedArrays(nums1, nums2):
    # if nums1 length is greater than switch them so that nums1 is smaller than nums2.
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)

    x, y = len(nums1), len(nums2)

    low, high = 0, x

    while low <= high:
        partition_x = (low + high) / 2
        partition_y = (x + y + 1) / 2 - partition_x

        """
        if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX

        if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
        """

        max_left_x = -float('inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == x else nums1[partition_x]


        max_left_y = -float('inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == y else nums2[partition_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            """
            We have partitioned array at correct place
            Now get max of left elements and min of right elements to get the median in case of even length combined array size
            or get max of left for odd length combined array size.
            """
            if (x + y) % 2 == 0:
                return 1.0 * (max(max_left_x, max_left_y) + \
                                        min(min_right_x, min_right_y)) / 2
            else:
                return 1.0 * max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1


if __name__ == '__main__':
    print findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 19, 21, 18, 25])
    print('\n')
    print findMedianSortedArrays([1, 3], [2])


