=begin
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.


Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

https://discuss.leetcode.com/topic/3396/my-iterative-sollution-very-simple-under-15-lines

Time complexity: Assuming the average number of letters on every number is m and the length of digits string is n, then the time complexity is O(m^n) [exponential]
=end
def letter_combinations(digits)
  result = ['']

  return result if digits.nil?

  char_map = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

  digits.chars.each do |digit|
    letters = char_map[digit.to_i]
    temp = []

    result.each do |str|
      letters.chars.each do |char|
        temp << str + char
      end
    end

    result = temp
  end

  return result
end

if __FILE__ == $0
  p letter_combinations('23')
end
