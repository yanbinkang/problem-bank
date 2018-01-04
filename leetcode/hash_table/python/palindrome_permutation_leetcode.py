"""
https://leetcode.com/problems/palindrome-permutation/

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

https://discuss.leetcode.com/topic/22057/java-solution-w-set-one-pass-without-counters

The idea is to iterate over string, adding current character to set if set doesn't contain that character, or removing current character from set if set contains it.
When the iteration is finished, just return set.size()==0 || set.size()==1.

set.size()==0 corresponds to the situation when there are even number of any character in the string, and
set.size()==1 corresponds to the fact that there are even number of any character except one.
"""
def can_permute_palindrome(string):
    if not string: return False

    char_set = set()

    for char in string:
        if char in char_set:
            char_set.remove(char)
        else:
            char_set.add(char)

    return len(char_set) == 0 or len(char_set) == 1

if __name__ == '__main__':
    print can_permute_palindrome('aab')
    print can_permute_palindrome('code')
    print can_permute_palindrome('carerac')
