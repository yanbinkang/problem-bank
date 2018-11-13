=begin
https://leetcode.com/problems/valid-parentheses/#/description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

https://discuss.leetcode.com/topic/6534/simple-python-solution-with-stack

O(n) time and space
ref: https://wiki.python.org/moin/TimeComplexity
=end
def is_valid(s)
  stack = []
  d = { ']' => '[', '}' => '{', ')' => '(' }

  s.chars.each do |char|
    if d.value?(char) # just append any open parens
      stack << char
    elsif d.key?(char)
      # at this point we should have already seen any opens '({['.
      # So if stack is empty return false. Also, if opens doesn't match closers ']})' return false

      return false if stack.empty? || d[char] != stack.pop
    else # char not in the characters we want
      return false
    end
  end

  # if stack is empty at this point, return true else false
  stack.empty?
end

# FIX ME!
# def is_valid_2(s)
#   stack = []

#   s.chars.each do |char|
#     if '([{'.include?(char)
#       stack << char
#     elsif !stack.empty?
#       top = stack.pop
#       return false unless matches(top, char)
#     end
#   end

#   stack.empty?
# end

# def matches(open, close)
#   opens = '([{'
#   closers = ')]}'

#   opens.index(open) == closers.index(close)
# end

if $PROGRAM_NAME == __FILE__
  puts is_valid('()') # true
  puts
  # puts is_valid(']') # false
  # puts
  # puts is_valid('()[]{}') # true
  # puts
  # puts is_valid('([)]') # false
  # puts
  # puts is_valid('{{([][])}()}') # true
  # puts
  # puts is_valid_2('{{([][])}()}') # true
  # puts
  # puts is_valid_2('()[]{}') # true
  # puts
  # puts is_valid_2('{{([][])}()}') # true

end
