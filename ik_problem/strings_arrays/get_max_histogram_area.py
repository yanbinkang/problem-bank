"""
Video link https://youtu.be/ZmnqCZp9bBs

 Given an array representing height of bar in bar graph, find max histogram
 area in the bar graph. Max histogram will be max rectangular area in the
 graph.

 Maintain a stack

 If stack is empty or value at index of stack is less than or equal to value at current
 index, push this into stack.
 Otherwise keep removing values from stack till value at index at top of stack is
 less than value at current index.
 While removing value from stack calculate area
 if stack is empty
 it means that till this point value just removed has to be smallest element
 so area = input[top] * i
 if stack is not empty then this value at index top is less than or equal to
 everything from stack top + 1 till i. So area will
 area = input[top] * (i - stack.peek() - 1);
 Finally maxArea is area if area is greater than maxArea.


 Time complexity is O(n)
 Space complexity is O(n)

 References:
 http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
"""

def maximum_histogram(input):
    stack = []
    max_area = 0
    area = 0
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
            if area > max_area:
                max_area = area

    while stack != []:
        top = stack.pop()
        if stack == []:
            area = input[top] * i
        else:
            area = input[top] * (i - stack[-1] - 1)

        if area > max_area:
            max_area = area

    return max_area

print maximum_histogram([6, 2, 5, 4, 5, 1, 6])
print maximum_histogram([2, 1, 5, 6, 2, 3])
print maximum_histogram([2, 1, 2])
