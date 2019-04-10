=begin
https://leetcode.com/problems/spiral-matrix-ii/description/

Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
=end

def generate_matrix(n)
  counter = 0
  matrix = Array.new(n) { Array.new(n, nil) }

  row_start = 0
  col_start = 0
  row_end = n - 1
  col_end = n - 1

  while row_start <= row_end && col_start <= col_end
    (col_start...col_end + 1).each do |j|
      counter += 1
      matrix[row_start][j] = i
    end

    row_start += 1

    (row_start...row_end + 1).each do |j|
      counter += 1
      matrix[j][col_end] = i
    end

    col_end -= 1

    break if row_start > row_end || col_start > col_end

    (col_start...col_end + 1).reverse_each do |j|
      counter += 1
      matrix[row_end][j] = i
    end

    row_end -= 1

    (row_start...row_end + 1).reverse_each do |j|
      counter += 1
      matrix[j][col_start] = i
    end

    col_start += 1
  end

  matrix
end
