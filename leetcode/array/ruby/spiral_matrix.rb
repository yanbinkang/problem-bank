=begin
https://leetcode.com/problems/spiral-matrix/description/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

solution ref: https://discuss.leetcode.com/topic/3713/super-simple-and-easy-to-understand-solution

solve next: https://leetcode.com/problems/spiral-matrix-ii/description/
=end
def spiral_order(matrix)
  result = []

  return result if matrix.size.zero?

  row_start = 0
  col_start = 0
  row_end = matrix.size - 1
  col_end = matrix.first.size - 1

  while row_start <= row_end && col_start <= col_end
    (col_start...col_end + 1).each do |j|
      result << matrix[row_start][j]
    end

    row_start += 1

    (row_start...row_end + 1).each do |j|
      result << matrix[j][col_end]
    end

    col_end -= 1

    break if row_start > row_end || col_start > col_end

    (col_start...col_end + 1).reverse_each do |j|
      result << matrix[row_end][j]
    end

    row_end -= 1

    (row_start...row_end + 1).reverse_each do |j|
      result << matrix[j][col_start]
    end

    col_start += 1
  end

  result
end

if $PROGRAM_NAME == __FILE__
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  p spiral_order(matrix)
end
