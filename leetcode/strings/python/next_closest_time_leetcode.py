"""
https://leetcode.com/problems/next-closest-time/description

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

ref: https://discuss.leetcode.com/topic/104710/python

algo: Just turn the clock forwards one minute at a time until a time with the original digits is reached.
"""
from datetime import *

def next_closest_time(time):
    digits = set(time)

    while True:
        time = (datetime.strptime(time, '%H:%M') + timedelta(minutes=1)).strftime('%H:%M')

        print time, set(time)
        print('\n')

        if set(time) <= digits:
            return time

if __name__ == '__main__':
    print next_closest_time('19:34')
