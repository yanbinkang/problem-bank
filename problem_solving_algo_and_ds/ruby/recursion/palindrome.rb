def is_palindrome(a_string)
  if a_string.length <= 1
    return true
  elsif is_palindrome(a_string[1..-2]) && a_string[0] == a_string[-1]
    return true
  else
    return false
  end
end

puts is_palindrome("civic")
