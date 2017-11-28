def appears_twice(a_list):
    special_dict = {}
    for i in a_list:
        if i in special_dict:
            special_dict[i] += 1
        else:
            special_dict[i] = 1

    for key in special_dict:
        if special_dict[key] == 2:
            return key

print(appears_twice([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]))

print """
Solution
First, we sum all numbers 1...n. We can do this using the equation:

n(squared) + n
--------------
      2

because the numbers in 1...n are a triangular series.

Second, we sum all numbers in our input array,
which should be the same as our other sum but with our repeat number added in twice.
So the difference between these two sums is the repeated number!
Complexity
O(n) time and O(1) additional space.
"""
