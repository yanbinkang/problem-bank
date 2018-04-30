require_relative "deque"

def pal_checker(a_string)
  char_deque = Deque.new

  a_string.chars.each do |char|
    char_deque.add_rear(char)
  end

  still_equal = true

  while char_deque.size > 1 && still_equal
    first = char_deque.remove_front
    last = char_deque.remove_rear
    if first != last
      still_equal = false
    end
  end

  return still_equal
end

puts pal_checker("lsdkjfskf")
puts pal_checker("radar")
