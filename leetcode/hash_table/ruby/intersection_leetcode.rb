# https://leetcode.com/problems/intersection-of-two-arrays/
# Given two arrays, write a function to compute their intersection.

def intersection(nums1, nums2)
  nums1 & nums2
end

p intersection([1, 2, 2, 1], [2, 2])
p intersection([1, 1, 3, 5], [1, 2, 3])
p intersection([ 'a', 'b', 'b', 'z' ], [ 'a', 'b', 'c' ])
