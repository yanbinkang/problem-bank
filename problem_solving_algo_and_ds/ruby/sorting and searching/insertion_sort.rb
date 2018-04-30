def insertion_sort(a_list)
  len = a_list.length
  (1...len).each do |index|
    current_value = a_list[index]
    position = index

    while position > 0 && a_list[position - 1] > current_value
      a_list[position] = a_list[position - 1]
      position = position - 1
    end

    a_list[position] = current_value
  end

  return a_list
end

my_list = [54,26,93,17,77,31,44,55,20]
p insertion_sort(my_list)
