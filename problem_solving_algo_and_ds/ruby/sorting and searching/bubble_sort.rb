def bubble_sort(a_list)
  a_list.reverse.each_index do |pass_num|
    pass_num.times.each do |i|
      if a_list[i] > a_list[i + 1]
        temp = a_list[i]
        a_list[i] = a_list[i + 1]
        a_list[i + 1] = temp
      end
    end
  end

  return a_list
end

my_list = [54,26,93,17,77,31,44,55,20]
p bubble_sort(my_list)
