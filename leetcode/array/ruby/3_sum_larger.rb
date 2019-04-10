=begin
You are given an array A of N non-negative integers. For a given integer M, count how many triplets of A have a sum larger than M.

A triplet is a tuple (A[i], A[j], A[k]) where i < j < k

Example:

a = [3, 1, 2, 5]
m = 8

Return 2

The two triplets with sum greater than 8 are (3, 2, 5) and (3, 1, 5)

Note: Look at 3 sum smaller for explanation
=end
def three_sum_larger(nums, target)
  nums.sort!
  count = 0

  (0...nums.size - 2).each do |i|
    left = i + 1
    right = nums.size - 1

    while left < right
      total = nums[i] + nums[left] + nums[right]

      if total > target
        count += right - left
        right -= 1
      else
        left += 1
      end
    end
  end

  count
end

if $PROGRAM_NAME == __FILE__
  p three_sum_larger([3, 1, 2, 5], 8)
  puts
  p three_sum_larger([5, 1, 3, 4, 7], 12)
end
