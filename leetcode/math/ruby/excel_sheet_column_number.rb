=begin
https://leetcode.com/problems/excel-sheet-column-number/

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

ref: https://leetcode.com/problems/excel-sheet-column-number/discuss/52289/Explanation-in-Python
=end
def title_to_number(s)
  s = s.reverse
  total = 0

  s.chars.each_with_index do |char, exp|
    total += (char.ord - 65 + 1) * (26**exp)
  end

  total
end

if $PROGRAM_NAME == __FILE__
  puts title_to_number('AB')
  puts title_to_number('YZ')
  puts title_to_number('CAA')
end