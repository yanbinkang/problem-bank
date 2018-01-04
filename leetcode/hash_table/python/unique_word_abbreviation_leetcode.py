import collections
"""
https://leetcode.com/problems/unique-word-abbreviation/

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") ->
false

isUnique("cart") ->
true

isUnique("cane") ->
false

isUnique("make") ->
true

https://discuss.leetcode.com/topic/25938/python-short-solution-using-defaultdict-with-comments
"""
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dic = collections.defaultdict(set)

        for s in dictionary:
            val = s
            if len(s) > 2:
                abbr = s[0] + str(len(s) - 2) + s[-1]
            self.dic[abbr].add(val)


    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        val = word

        if len(word) > 2:
            abbr = word[0] + str(len(word) - 2) + word[-1]

        """
        if word abbreviation not in the dictionary, or word itself in the dictionary
        (word itself may appear multiple times in the dictionary, so it's better using set instead of list)
        """
        return len(self.dic[abbr]) == 0 or ( len(self.dic[abbr]) == 1 and val == list(self.dic[abbr])[0] )



# Your ValidWordAbbr object will be instantiated and called as such:
obj = ValidWordAbbr([ "deer", "door", "cake", "card" ])
print obj.isUnique('dear')
print('\n')
print obj.isUnique('cart')
print('\n')
print obj.isUnique('cane')
print('\n')
print obj.isUnique('make')


