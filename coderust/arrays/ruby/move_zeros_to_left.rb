def move_zeros_to_left(nums)
  insert_pos = nums.length - 1

  nums.to_enum.with_index.reverse_each do |num, index|
    if num != 0
      nums[insert_pos] = nums[index]
      insert_pos -= 1
    end
  end

  while insert_pos >= 0
    nums[insert_pos] = 0
    insert_pos -= 1
  end

  nums
end


def move_zeros_to_left_1(arr)
  if (arr.length < 1)
    return
  end

  lengthA = arr.length
  write_index = lengthA - 1
  read_index = lengthA - 1

  while (read_index >= 0)
    if (arr[read_index] != 0)
      arr[write_index] = arr[read_index]
      write_index-=1
    end

    read_index-=1
  end

  while (write_index >= 0)
    arr[write_index] = 0
    write_index-=1
  end
end

if __FILE__ == $PROGRAM_NAME
  p move_zeros_to_left([1, 10, 20, 0, 59, 63, 0, 88, 0])
end
