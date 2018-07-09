"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

https://discuss.leetcode.com/topic/25499/share-my-java-solution-using-hashset

https://discuss.leetcode.com/topic/11632/a-python-solution-85ms-o-n

https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems
"""
def length_of_longest_substring_3(s):
    dic = {}
    left, right, count, max_length = 0, 0, 0, 0

    while right < len(s):
        char = s[right]

        dic[char] = dic.get(char, 0) + 1

        """
        there is a repeated character. Think about it, if the value of char in the dictionary are all 1's, we're looking at unique characters. Hence when dic[char] > 1, that condition changes
        """
        if dic[char] > 1:
            count += 1

        right += 1

        while count > 0:
            if s[left] in dic:

                # if s[left] is a repeated character
                if dic[s[left]] > 1:
                    count -= 1

                dic[s[left]] -= 1

            left += 1

        max_length = max(max_length, right - left)

    return max_length


"""
ref: https://leetcode.com/articles/longest-substring-without-repeating-characters/#approach-2-sliding-window-accepted


By using HashSet as a sliding window, checking if a character in the current can be done in O(1)

A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i, j) (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we slide [i, j) to the right by 1 element, then it becomes [i+1, j+1) (left-closed, right-open).

Back to our problem. We use HashSet to store the characters in current window [i, j) (j = i initially).

Then we slide the index j to the right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already in the HashSet.

At this point, we found the maximum size of substrings without duplicate characters start with index i. We remove string indexed at i from set and now close the window by increasing i (the else part of the code). If we do this for all i, we get our answer.


Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by i and j

Space complexity : O(min(m, n))
"""
def length_of_longest_substring(s):
    i, j, s_max = 0, 0, 0

    s_set = set()

    while j < len(s):
        if s[j] not in s_set:
            s_set.add(s[j])
            j +=1
            s_max = max(s_max, len(s_set)) # s_max = max(s_max, j - i)
        else:
            s_set.remove(s[i])
            i += 1

    return s_max

def length_of_longest_substring_2(s):
    left = max_length = 0
    used = {}

    for i, char in enumerate(s):
        if char in used and left <= used[char]:
            left = used[char] + 1
        else:
            # we're adding 1 to cater for zero based index when counting actualt length
            # (i - left + 1) signifies end of substring minus left of substring plus 1
            max_length = max(max_length, i - left + 1)

        used[char] = i

    return max_length

if __name__ == '__main__':
    print length_of_longest_substring('abcabcbb')
    print length_of_longest_substring('bbbbb')
    print length_of_longest_substring('pwwkew')
    print('\n')
    print length_of_longest_substring_2('abcabcbb')
    print('\n')
    print length_of_longest_substring_3('abcabcbb')
    print length_of_longest_substring_3('pwwkew')
