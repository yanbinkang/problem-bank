=begin
https://leetcode.com/problems/number-complement/description/

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
=end
# Note: check out bit manipulation solutions
def find_complement(num)
  result = 0

  num_bits = num.to_s(2).chars.map(&:to_i) # Convert to binary (base 2) and map to integers

  num_bits.reverse.each_with_index do |n, idx|
    n = n == 0 ? 1 : 0
    result += 2 ** idx * (n) # Convert to base 10
  end

  result
end
