"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

ref: https://discuss.leetcode.com/topic/16988/7-lines-3-easy-solutions

ALGO:

Partition the intervals into two parts, left and right

1. All intervals in left have their end less than start of new_interval

        if i.end < s:
            left += [i]

2. All intervals in right have their start greater than end of new_interval

        elif i.start > e:
            right += [i]

3. Else find the range for any overlap by finding the min start so far and max end so far:

        else:
            s = min(s, i.start)
            e = max(e, i.end)

4. return left + overlap + right:

        return left + [Interval(s, e)] + right

Note on left += i,

What I'm using is the comma operator, and it creates a tuple.

I think sometimes it looks nicer than append (thanks to the spaces around +=), I think it's slightly faster in one of Python 2 or 3 (can never remember which one), and I want to make people aware of the comma operator :-)

O(n) time and space

"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str([self.start, self.end])

    def __repr__(self):
        return self.__str__()

def insert(intervals, new_interval):
    s, e = new_interval.start, new_interval.end
    left, right = [], []

    for i in intervals:
        if i.end < s:
            left += [i] # can also do: left += i,
        elif i.start > e:
            right += [i] # can also do: right += i,
        else:
            s = min(s, i.start)
            e = max(e, i.end)

    return left + [Interval(s, e)] + right

if __name__ == '__main__':
    intervals = [ Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16) ]

    print insert(intervals, Interval(4, 9))
    print('\n')
    print insert([ Interval(1, 3), Interval(6, 9) ], Interval(2, 5))
