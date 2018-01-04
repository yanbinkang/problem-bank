"""
https://leetcode.com/problems/sort-characters-by-frequency/

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

similar to: https://leetcode.com/problems/top-k-frequent-elements/

solution: use bucket sort

O(n) time, O(n) space
"""
def frequency_sort(s):
    result = ''

    bucket = [None for i in range(len(s) + 1)]

    hash_map = {}

    for char in s:
        hash_map[char] = hash_map.get(char, 0) + 1

    for key, value in hash_map.items():
        if bucket[value] is None:
            bucket[value] = []
        bucket[value].append(key)

    for i in reversed(range(len(bucket))):
        if bucket[i] is not None:
            for char in bucket[i]:
                result += char * i

    return result



if __name__ == '__main__':
    print frequency_sort('Aabb')
    print frequency_sort('tree')
    print frequency_sort('cccaaa')

