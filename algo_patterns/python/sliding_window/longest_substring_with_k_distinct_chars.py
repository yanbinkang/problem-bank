"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""


def longest_substring_with_k_distinct(str, k):
    window_start, max_length = 0, 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]

        char_frequency[right_char] = char_frequency.get(right_char, 0) + 1

        # shrink the sliding wondow, until we are left with 'k'
        # distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1

            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the window

        # remember maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == "__main__":
    print(longest_substring_with_k_distinct("araaci", 2))
    print(longest_substring_with_k_distinct("araaci", 1))
    print(longest_substring_with_k_distinct("cbbebi", 3))
