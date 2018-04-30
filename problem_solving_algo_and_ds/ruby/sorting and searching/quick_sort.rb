def quick_sort(a_list)
  quick_sort_helper(a_list, 0, a_list.length - 1)
end

def quick_sort_helper(a_list, first, last)
  if first < last
    split_point = partition(a_list, first, last)

    quick_sort_helper(a_list, first, split_point-1)
    quick_sort_helper(a_list, split_point+1, last)
  end
end

def partition(a_list, first, last)
  pivot_value = a_list[first]

  left_mark = first + 1
  right_mark = last

  done = false

  unless done
    while left_mark <= right_mark && a_list[left_mark] <= pivot_value
      left_mark = left_mark + 1
    end

    while a_list[right_mark] >= pivot_value && right_mark >= left_mark
      right_mark = right_mark - 1
    end

    if right_mark < left_mark
      done = true
    else
      temp = a_list[left_mark]
      a_list[left_mark] = a_list[right_mark]
      a_list[right_mark] = temp
    end
  end

  temp = a_list[first]
  a_list[first] = a_list[right_mark]
  a_list[right_mark] = temp

  return right_mark
end

my_list = [54, 26, 93, 17]
quick_sort(my_list)
p my_list
