"""
https://leetcode.com/problems/meeting-rooms/#/description

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

algo: Sort the intervals based on start time. Why? Because ideally you want to attend the earliest meeting first.

For the given example after sorting we have [[0, 30], [5, 10], [15, 20]]. Now start from index 1 and compare the current start time with the previous end time. Anytime the current start time is less than the previous end time, return False.

Retrun True at the end of the loop, meaning we can attend all meetings.

PLEASE TRY TO REMEMBER SORTING USING THIS lambda SHIT!

ITS IMPORTANT!

https://discuss.leetcode.com/topic/20913/my-python-solution

O(nlogn) time and O(n) space
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        sorted_intervals = sorted(intervals, key=lambda x: x.start) # O(nlogn)

        for i in range(1, len(sorted_intervals)): # O(n)
            if sorted_intervals[i].start < sorted_intervals[i - 1].end:
                return False

        return True
