=begin
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5

Explanation: You need to sort [6, 4, 8, 10, 9] in
ascending order to make the whole array sorted in ascending order.

Note:
    * Then length of the input array is in range [1, 10,000].
    * The input array may contain duplicates, so ascending order here means <=

ref: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/#approach-3-using-sorting-accepted

Time: O(nlogn) for because of sorting
Space: O(n)

Algo: Another very simple idea is as follows.
We can sort a copy of the given array nums,
say given by nums_sorted.
Then, if we compare the elements of nums and nums_sorted,
we can determine the leftmost and rightmost elements which mismatch.
The subarray lying between them is,
then, the required shorted unsorted subarray
=end
def find_unsorted_subaaray(nums)
  sorted_nums = nums.sort

  first = Float::INFINITY
  last = 0

  sorted_nums.length.times do |i|
    if sorted_nums[i] != nums[i]
      first = [first, i].min
      last = [last, i].max
    end
  end

  last - first >= 0 ? last - first + 1 : 0
end

if $PROGRAM_NAME == __FILE__
  puts find_unsorted_subaaray([2, 6, 4, 8, 10, 9, 15])
end
