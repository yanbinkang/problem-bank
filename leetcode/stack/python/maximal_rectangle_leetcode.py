"""
https://leetcode.com/problems/maximal-rectangle/

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6.


https://youtu.be/g8bSdXCG-lA

Algorithm: Use largest rectangle in histogram to solve subproblems.

1. Create a temp array with same size as total columns in 2D matrix.

2. Then copy zeroth row from matrix into temp array.

3. Next find the maximum area rectangle of temp and update max_area.

4. Move to the next row in matrix and update temp array such that when the value in the matrix is 1, add the value to the corresponding value in temp array; when the value in matrix is 0 make corresponding temp array value 0.

5. Next, find maximum area rectangle of temp and update max_area. Keep doing this until you reach end of matrix.

Space: O(cols)
time = O(rows * cols)
"""
def maximal_rectangle(matrix):
    temp = [0] * len(matrix[0])
    max_area = 0
    area = 0

    for i in range(len(matrix)):
        for j in range(len(temp)):
            if matrix[i][j] == 0:
                temp[j] = 0
            else:
                temp[j] += int(matrix[i][j])

        area = largest_rectangle_area(temp)

        max_area = max(max_area, area)

    return max_area

def largest_rectangle_area(input):
    stack = []
    area = 0
    max_area = 0
    i = 0

    while i < len(input):
        if stack == [] or input[stack[-1]] <= input[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if stack == []:
                area = input[top] * i
            else:
                area = input[top] * (i - stack[-1] - 1)

            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        if stack == []:
            area = input[top] * i
        else:
            area = input[top] * (i - stack[-1] - 1)

        max_area = max(max_area, area)

    return max_area


if __name__ == '__main__':
    matrix = [['1', '0', '1', '0', '0'],
              ['1', '0', '1', '1', '1'],
              ['1', '1', '1', '1', '1'],
              ['1', '0', '0', '1', '0']]

    print maximal_rectangle(matrix)
