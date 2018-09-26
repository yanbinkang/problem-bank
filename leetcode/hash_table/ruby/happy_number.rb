=begin
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

https://discuss.leetcode.com/topic/19520/my-python-solution

Note: we're using a set because we don't want to compute two numbers twice. Eg. 82 and 28.
=end
require 'set'
def is_happy(n)
  seen = Set.new

  while !seen.include?(n)
    seen.add(n)

    n = n.to_s.split('').map { |num| num.to_i ** 2 }.inject(&:+)
  end

  n == 1
end

if __FILE__ == $0
  puts is_happy(19)
  puts is_happy(3)
  puts RUBY_ENGINE_VERSION
end
