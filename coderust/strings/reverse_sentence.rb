def reverse_sentence(a_string)
  reverse_chars(a_string, 0, a_string.length - 1)
  str_position = 0
  i = 0

  while i < a_string.length
    if a_string[i] == ' ' or i == a_string.length
      reverse_chars(a_string, str_position, i-1)
      str_position = i + 1
    end

    i += 1
  end

  return a_string
end

def reverse_chars(a_string, first, last)

  while first <= last
    temp = a_string[first]
    a_string[first] = a_string[last]
    a_string[last] = temp

    first += 1
    last -= 1
  end
end

puts reverse_sentence('I am going to school')
