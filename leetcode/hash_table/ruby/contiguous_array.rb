def find_max_length(nums)
  nums.length.times do |i|
    if nums[i] == 0
      nums[i] = -1
    end
  end

  sum_to_index_map = {}
  sum_to_index_map[0] = -1

  total, max_size = 0, 0

  nums.length.times do |i|
    total += nums[i]

    if sum_to_index_map.include?(total)
      max_size = [max_size, i - sum_to_index_map[total]].max
    else
      sum_to_index_map[total] = i
    end
  end

  max_size
end

if __FILE__ == $0
  p find_max_length([0, 1])
  p find_max_length([0, 1, 0])
  p find_max_length([0, 1, 0, 0, 1, 1])
end
