"""
https://leetcode.com/problems/meeting-rooms-ii/#/description

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],

return 2.

Algo:

1. Sort intervals by start time (asc) call it starts
2. Sort the intervals by end time (asc) call it ends

3. For each start time, we want to know if there is an end time that is less than or equal to the start time. If this is so, we have to increase the number of available rooms by 1. Think about it, in real life, whenever you want to start a meeting, if there is a meeting that ends before your meeting starts, you have one potential available meeting room. That's what the while loop does.

4. If there's an available room, take it. Else find a new meeting room.

        if available:
            available -= 1
        else:
            num_rooms += 1

ref: https://discuss.leetcode.com/topic/20912/my-python-solution-with-explanation/4
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # below added by me
    def __str__(self):
        return str([self.start, self.end])

    def __repr__(self):
        return self.__str__()

def min_meeting_rooms(intervals):
    starts = sorted(i.start for i in intervals)
    ends = sorted(i.end for i in intervals)

    e = 0
    num_rooms = available = 0

    for start in starts:
        while ends[e] <= start:
            available += 1
            e += 1

        if available:
            available -= 1
        else:
            num_rooms += 1

    return num_rooms

"""
1. Sort intervals by start time (asc) call it starts
2. Sort the intervals by end time (asc) call it ends


Say you have two meeting times for meetings scheduled to take place. If one meeting ends before the other starts, then you automatically have an available room. (Look at the outer else conditional).

If one meeting starts before the other meeting ends and there are no available rooms, you need to find a new room. If there is an available room, you just take it
"""
def min_meeting_rooms_1(intervals):
    starts = sorted(i.start for i in intervals)
    ends = sorted(i.end for i in intervals)

    s = e = 0
    num_rooms = available = 0

    while s < len(starts):
        if starts[s] < ends[e]:
            if available == 0:
                num_rooms += 1
            else:
                available -= 1

            s += 1
        else:
            available += 1
            e += 1

    return num_rooms

if __name__ == '__main__':
    intervals_1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    intervals_2 = [Interval(9, 10), Interval(4, 9), Interval(4, 17)]
    intervals_3 = [Interval(2, 7)]
    print min_meeting_rooms(intervals_1)
    print('\n')
    print min_meeting_rooms(intervals_2)
    print('\n')
    print min_meeting_rooms(intervals_3)
