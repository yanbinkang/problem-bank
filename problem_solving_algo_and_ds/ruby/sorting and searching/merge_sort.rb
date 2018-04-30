def merge_sort(a_list)
  if a_list.size > 1
    mid = a_list.size / 2
    left_half = a_list[0...mid]
    right_half = a_list[mid..-1]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i < left_half.size && j < right_half.size
      if left_half[i] < right_half[j]
        a_list[k] = left_half[i]
        i = i + 1
      else
        a_list[k] = right_half[j]
        j = j + 1
      end
      k = k + 1
    end

    while i < left_half.size
      a_list[k] = left_half[i]
      i = i + 1
      k = k + 1
    end

    while j < right_half.size
      a_list[k] = right_half[j]
      j = j + 1
      k = k + 1
    end

  end

  return a_list
end

some_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
p merge_sort(some_list)
