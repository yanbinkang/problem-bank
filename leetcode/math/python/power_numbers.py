"""
A Power Number is defined as a number greater than zero that can be expressed as X ^ Y, where X and Y are integers greater than one.

Thus, the first few (in order) are:

4 (2 ^ 2)
8 (2 ^ 3)
9 (3 ^ 2)
16 (2 ^ 4, 4 ^ 2)
25 (5 ^ 2)
27 (3 ^ 3)
32 (2 ^ 5)
36 (6 ^ 2)
49 (7 ^ 2)
64 (2 ^ 6, 8 ^ 2)
81 (3 ^ 4, 9 ^ 2)
100 (10 ^ 2)

Write a function that takes an integer i and returns the (zero-indexed) ith power number.

Constraints:
* 0 <= i < 1000

Example 1:

Input getPowerNumber(0)
Output: 4

Example 2:

Input: getPowerNumber(3)
Output: 16

Example 3:
Input: getPowerNumber(8)
Output: 49
"""
