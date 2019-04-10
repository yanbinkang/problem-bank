=begin
https://leetcode.com/problems/zigzag-conversion/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

solution: https://discuss.leetcode.com/topic/34573/python-o-n-solution-in-96ms-99-43

Idea: Iterate over each character in the string and distribute the characters in the string in a zigzag fashion.

Let num_rows equal three empty strings i.e ['', '', '']. Concatenate the first character to the first empty string. When index is zero, we know we have to move to the next index. When index is equal to (num_rows - 1) we have to change direction.
=end
def convert(s, num_rows)
  return s if num_rows == 1 || num_rows >= s.size

  result = [''] * num_rows
  index = 0
  step = 0

  s.chars.each do |char|
    result[index] += char

    if index.zero?
      step = 1
    elsif index == num_rows - 1
      step = -1
    end

    index += step
  end

  result.join
end

if $PROGRAM_NAME == __FILE__
  p convert('PAYPALISHIRING', 3)
  puts
  p convert('ABC', 2)
end
