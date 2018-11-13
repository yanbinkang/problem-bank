=begin
https://leetcode.com/problems/reverse-string/?tab=Description

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

https://discuss.leetcode.com/topic/43296/java-simple-and-clean-with-explanations-6-solutions
=end
def reverse_string(s)
  first = 0
  last = s.length - 1

  while first < last
    # temp = s[first]
    # s[first] = s[last]
    # s[last] = temp
    s[first], s[last] = s[last], s[first]

    first += 1
    last -= 1
  end

  s
end

if $PROGRAM_NAME == __FILE__
  puts reverse_string('hello')
end
