"""
https://leetcode.com/problems/merge-intervals/#/description

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # below code added my me
    def __str__(self):
        return str([self.start, self.end])

    def __repr__(self):
        return self.__str__()

"""
Just go through the intervals sorted by start coordinate and either combine the current interval with the previous one if they overlap, or add it to the output by itself if they don't.

https://discuss.leetcode.com/topic/17178/7-lines-easy-python


Algo:
If result is not empty and the current interval's start time is less than or equal to the end time of the last element in result, then we can obviously adjust the end time of the last element in result. Example:

                result = [1, 3]
                interval = [2, 6]

        The adjustment is done like so:

                    result[-1].end = max(result[-1].end, interval.end)

if the above condition doesn't hold just add the interval to result.

Time Complexity: n + nlogn => nlogn
Space Complexity: O(n)
"""
def merge2(intervals):
    if len(intervals) <= 1: return intervals

    intervals = sorted(intervals, key=lambda i: i.start) # O(nlogn)
    result = []

    for interval in intervals: # O(n)
        if result and result[-1].end >= interval.start: # times overlap!
            result[-1].end = max(result[-1].end, interval.end)
        else:
            result.append(interval)

    return result


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len(intervals) <= 1: return intervals

    sorted_intervals = sorted(intervals, key=lambda x: x.start)
    result = []

    prev_start, prev_end = sorted_intervals[0].start, sorted_intervals[0].end

    for interval in sorted_intervals[1:]:
        if interval.start <= prev_end:
            prev_end = max(prev_end, interval.end)
        else:
            result.append( Interval(prev_start, prev_end) )

            prev_start, prev_end = interval.start, interval.end

    result.append(Interval(prev_start, prev_end))

    return result


if __name__ == '__main__':
    intervals = [ Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18) ]
    intervals1 = [ Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16) ]

    print merge(intervals)
    print merge2(intervals)
    print merge2(intervals1)
