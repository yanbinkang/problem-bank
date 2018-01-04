"""
https://leetcode.com/problems/repeated-dna-sequences/

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

https://discuss.leetcode.com/topic/33990/clean-python-code

Time complexity is O(n)
Space complexity is O(n)
"""
def find_repeated_dna_sequences(s):
    repeat, seen = set(), set()

    for i in range(len(s) - 9):
        substring = s[i:i + 10]

        if substring in seen:
            repeat.add(substring)
        else:
            seen.add(substring)

    return list(repeat)

def find_repeated_dna_sequences_alt(s):
    repeat, seen = set(), set()

    i = 0

    while i + 9 < len(s):
        substring = s[i:i + 10]

        if substring in seen:
            repeat.add(substring)
        else:
            seen.add(substring)

        i += 1

    return list(repeat)



if __name__ == '__main__':
    s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    print find_repeated_dna_sequences(s) # ["AAAAACCCCC", "CCCCCAAAAA"]
