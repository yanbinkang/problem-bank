def check_subarray_sum(nums, k)
  hash_map = {}
  hash_map[0] = -1

  running_sum = 0

  nums.length.times do |i|
    running_sum += nums[i]

    if k != 0
      running_sum = running_sum % k
    end

    if hash_map.include?(running_sum)
      return true if i - hash_map[running_sum] > 1
    else
      hash_map[running_sum] = i
    end
  end

  false
end

if __FILE__ == $0
  p check_subarray_sum([23, 2, 4, 6, 7], 6)
  p check_subarray_sum([23, 2, 6, 4, 7], 6)
  p check_subarray_sum([7, 6, 6], 6)
  p check_subarray_sum([0, 0], 0)
  p check_subarray_sum([0], -1)
end
