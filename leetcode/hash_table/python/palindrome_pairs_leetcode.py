"""
https://leetcode.com/problems/palindrome-pairs/

https://discuss.leetcode.com/topic/39584/accepted-python-solution-with-explanation

The basic idea is to check each word for prefixes (and suffixes) that are themselves palindromes. If you find a prefix that is a valid palindrome, then the suffix reversed can be paired with the word in order to make a palindrome. It's better explained with an example.

words = ["bot", "t", "to"]
Starting with the string "bot". We start checking all prefixes. If "", "b", "bo", "bot" are themselves palindromes. The empty string and "b" are palindromes. We work with the corresponding suffixes ("bot", "ot") and check to see if their reverses ("tob", "to") are present in our initial word list. If so (like the word to"to"), we have found a valid pairing where the reversed suffix can be prepended to the current word in order to form "to" + "bot" = "tobot".

You can do the same thing by checking all suffixes to see if they are palindromes. If so, then finding all reversed prefixes will give you the words that can be appended to the current word to form a palindrome.

The process is then repeated for every word in the list. Note that when considering suffixes, we explicitly leave out the empty string to avoid counting duplicates. That is, if a palindrome can be created by appending an entire other word to the current word, then we will already consider such a palindrome when considering the empty string as prefix for the other word.
"""
def palindrome_pairs(words):
    word_dict = {}
    result = []

    for i, word in enumerate(words):
        word_dict[word] = i

    for word, i in word_dict.items():
        n = len(word)
        for j in range(n + 1):
            preffix = word[:j]
            suffix = word[j:]

            if is_palindrome(preffix):
                rev = suffix[::-1]
                if rev != word and rev in word_dict:
                    result.append([word_dict[rev], i])

            if j != n and is_palindrome(suffix):
                rev = preffix[::-1]
                if rev != word and rev in word_dict:
                    result.append([i, word_dict[rev]])

    return result

def is_palindrome(string):
    return string == string[::-1]

if __name__ == '__main__':
    print palindrome_pairs(['bat', 'tab', 'cat'])
    print palindrome_pairs(['abcd', 'dcba', 'lls', 's', 'sssll'])


