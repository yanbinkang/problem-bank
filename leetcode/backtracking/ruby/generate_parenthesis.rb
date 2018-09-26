=begin
https://leetcode.com/problems/generate-parentheses/#/description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

left represents how many left parenthesis remains. right represents how many right parenthesis remains.
=end
def generate_parenthesis(n)
  result = []
  helper(result, '', n, n)

  result
end

def helper(result, string, left, right)
  result << string if left.zero? && right.zero?

  if left > 0
    helper(result, string + '(', left - 1, right)
  end

  if right > left
    helper(result, string + ')', left, right - 1)
  end
end

if __FILE__ == $0
  puts generate_parenthesis(3)
end
