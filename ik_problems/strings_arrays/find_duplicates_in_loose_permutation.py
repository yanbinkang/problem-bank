"""
Find a duplicated number in a loose permutation of numbers.

A strict permutation is an array that is size N, and also has positive numbers from 1 thru N.
A loose permutation is a permutation where some numbers are missing and some are duplicated, but the total is still N.

* We want to find any one duplicated number; not necessarily the first or the least.
* It can occur anywhere in the input array, and we don't care how many times it's duplicated.
* Input array may nor may not be sorted.

e.g.
Input: 1,7,4,3,2,7,4: This array has 7 numbers from 1 thru 7, with some missing (5 and 6) and some duplicated (4 and 7). Albeit unsorted, but sorting is irrelevant to a permutation.
Output: 4 or 7

Input: 3,1,2:  This array has nothing missing.
Output: -1

Solution:
1) Try to move each element to it's logical place i.e 1 at index 0, 2 at index 1 etc.
2) If element is already at it's logical place move counter
3) Else swap element with what's stored at it's logical place. Do not move counter
4) If number stored at logical place and element are equal, return element
5) If there is no element missing return -1
"""

def find_duplicate(a_list):
    i = 0

    while i < len(a_list):
        if a_list[i] - 1 != i:
            if a_list[a_list[i]-1] == a_list[i]:
                return a_list[i]
            else:
                temp = a_list[i]
                a_list[i] = a_list[a_list[i] - 1]
                a_list[temp - 1] = temp
        else:
            i += 1

    return -1


arr = [1, 7, 4, 3, 2, 7, 4]
arr_1 = [3, 1, 2]
print find_duplicate(arr)
print find_duplicate(arr_1)
