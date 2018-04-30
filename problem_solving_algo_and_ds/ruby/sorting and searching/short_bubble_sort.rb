def short_bubble_sort(a_list)
  exchanges = true
  pass_num = a_list.length - 1

  while pass_num > 0 && exchanges
    exchanges = false
    (0...pass_num).each do |i|
      if a_list[i] > a_list[i + 1]
        exchanges = true
        temp = a_list[i]
        a_list[i] = a_list[i + 1]
        a_list[i + 1] = temp
      end
    end
    pass_num = pass_num - 1
  end

  return a_list
end

my_list = [20,30,40,90,50,60,70,80,100,110]
p short_bubble_sort(my_list)
