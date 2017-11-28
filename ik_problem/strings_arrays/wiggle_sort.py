"""
You are given an array of numbers.
Rearrange elements in the array according to
the following order: a1 <= a2 >= a3 <= a4 >= a5 ...
eg. [1,3,6,9,-3,-4]     Answer: [1, 6, 3, 9, -4, -3]

A reverse arrangement is also acceptable: a1 >= a2 <= a3 ...

Aim for O(N)
"""

def wiggle_sort(a_list):
	i = 0

	while i < len(a_list) - 1:
		if i % 2 == 0:
			if a_list[i] > a_list[i+1]:
				temp = a_list[i]
				a_list[i] = a_list[i+1]
				a_list[i+1] = temp
		else:
			if a_list[i] < a_list[i+1]:
				temp = a_list[i]
				a_list[i] = a_list[i+1]
				a_list[i+1] = temp
		i += 1

	return a_list

my_list = [1, 3, 6, 9, -3, -4]

print wiggle_sort(my_list)
