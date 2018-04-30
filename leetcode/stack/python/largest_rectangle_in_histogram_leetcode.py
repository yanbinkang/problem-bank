"""
https://leetcode.com/problems/largest-rectangle-in-histogram/

Video link https://youtu.be/ZmnqCZp9bBs

Given an array representing height of bar in bar graph, find max histogram
area in the bar graph. Max histogram will be max rectangular area in the
graph.

Maintain a stack

If stack is empty or value at index of stack is less than or equal to value at current index, push this into stack.

Otherwise keep removing values from stack till value at index at top of stack is less than value at current index.

While removing value from stack calculate area if stack is empty

it means that till this point value just removed has to be smallest element
so area = input[top] * i

if stack is not empty then this value at index top is less than or equal to
everything from stack top + 1 till i. So area will:

area = input[top] * (i - stack.peek() - 1);

Finally maxArea is area if area is greater than maxArea.


 Time complexity is O(2n) => O(n)
 Space complexity is O(n)

 References:
 http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
"""
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    area = 0
    i = 0

    while i < len(heights):
        if stack == [] or heights[stack[-1]] <= heights[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if stack == []:
                area = heights[top] * i
            else:
                area = heights[top] * (i - stack[-1] - 1)

            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        if stack == []:
            area = heights[top] * i
        else:
            area = heights[top] * (i - stack[-1] - 1)

        max_area = max(max_area, area)


    return max_area

print largest_rectangle_area([6, 2, 5, 4, 5, 1, 6])
print largest_rectangle_area([2, 1, 5, 6, 2, 3])
print largest_rectangle_area([2, 1, 2])
