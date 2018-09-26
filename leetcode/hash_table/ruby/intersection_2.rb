=begin
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
=end
def intersect(num1, num2)
  d, result = {}, []

  num1.each do |num|
    d[num] = d.fetch(num, 0) + 1
  end

  num2.each do |num|
    if d.include?(num)
      d[num] -= 1

      if d[num] >= 0
        result << num
      end
    end
  end

  result
end

def intersect2(num1, num2)
  n1, n2 = num1.sort, num2.sort
  i, j = 0 , 0
  result = []

  while i < n1.length && j < n2.length
    if n1[i] == n2[j]
      result << n1[i]

      i += 1
      j += 1
    elsif n1[i] < n2[j]
      i += 1
    else
      j += 1
    end
  end

  result
end


if __FILE__ == $0
  p intersect([1, 2, 2, 1], [2, 2])
  p intersect([1], [1, 1])  # [1]
  p intersect([1, 2], [1, 1]) # [1]
  p intersect([], [1]) # []
  p intersect([1], [1, 2]) # [1]

  puts

  p intersect2([1, 2, 2, 1], [2, 2])
  p intersect2([1], [1, 1])
end
