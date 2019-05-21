# frozen_string_literal: true

=begin
Given an array, find the averages of all subarray of size 'K' in it.

Example:
[1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

Output: [2.2, 2.8, 2.4, 3.6, 2.8]
=end

# Brute force O(N * K) where N is the number of elements in the input array
def find_averages_of_subarrays(k, arr)
  result = []

  (0...arr.size - k + 1).each do |i|
    total = 0.0
    (i...i + k).each do |j|
      total += arr[j]
    end

    result << total / k
  end

  result
end

# O(n) time O(1) space optimal solution
def averages_of_subarrays(k, arr)
  result = []

  window_sum = 0.0
  window_start = 0

  arr.size.times do |window_end|
    window_sum += arr[window_end]

    next unless window_end >= k - 1

    result << window_sum / k
    window_sum -= arr[window_start]
    window_start += 1
  end

  result
end

if $PROGRAM_NAME == __FILE__
  p find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  p averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
end
