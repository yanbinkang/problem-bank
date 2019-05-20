# frozen_string_literal: true

=begin
Given an array of positive numbers and a positive number 'k', find the maximum sum of any subarray of size 'k'.

Example 1:
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
    Input: [2, 3, 4, 1, 5], k=2
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
=end

# Brute force O(N + K)
def max_subarray_size_k(size, arr)
  max_sum = 0
  window_sum = 0

  (arr.length - size + 1).times do |i|
    window_sum = 0
    (i...i + size).each do |j|
      window_sum += arr[j]
    end

    max_sum = [max_sum, window_sum].max
  end

  max_sum
end

def max_sub_array_of_size_k(k, arr)
  max_sum = -Float::INFINITY
  window_start = 0
  window_total = 0

  arr.size.times do |window_end|
    window_total += arr[window_end]

    next unless window_end >= k - 1

    max_sum = [window_total, max_sum].max
    window_total -= arr[window_start]
    window_start += 1
  end

  max_sum
end

if $PROGRAM_NAME == __FILE__
  p max_subarray_size_k(3, [2, 1, 5, 1, 3, 2])
  p max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])
end
