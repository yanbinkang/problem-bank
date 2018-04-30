"""
You parked your car in a parking lot and want to compute the total cost of the ticket. The billing rules are as follows:

    * The entrace fee of the car parking lot is 2
    * The first full or partial hour costs 3
    * Each successive full or partial hour (after the first) costs 4.

You entered the car parking lot at time E and left at time L. In this task, times are represented as strings in the format "HH:MM" (where "HH" is a two-digit number between 0 and 23, which stands for hours, and "MM" is a two-digit number between 0 and 59, which stands for minutes).

Write a function:

        def solution(E, L)

that, given strings E and L specifying points in time in the format "HH:MM", returns the total cost of parking bill from your entry at the time E to your exit at time L. You can assume that E describes a time before L on the same day.

For example, given "10:00" and "13:21" your function should return 17, because the entrance fee equals 2, the first hour costs 3 and there are two more full hours and part of a further hour, so the total cost is 2 + 3 + (3 * 4) = 17.

Given, "09:42" and "11:42" your function should return 9, because the entrance fee equals 2, the first hour costs 3 and the second hour costs 4, so the total cost is 2 + 3 + 4 = 9

Assume that:

    * strings E and L follow the format "HH:MM" strintly
    * string E describes a time L before L on the same day.

ref: http://jsfiddle.net/jnuas/8uoufLry/
"""
def solution(E, L):
    # write your code in Python 2.7
    # pass
    cost = 5 # entrance fee + first full or partial hour cost (2 + 3)
    hour_cost = 4

    # convert times to minutes
    h1, m1 = [int(i) for i in E.split(':')]
    h2, m2 = [int(i) for i in L.split(':')]

    # convert hours to minutes. no need to convert minutes
    h1 *= 60
    h2 *= 60

    # find the differnece between times
    duration = (h2 + m2) - (h1 + m1)

    if duration > 60:
        duration -= 60 # because we've already added the first hour

        cost += (duration / 60) * hour_cost

        # check partial hour
        if duration % 60 > 0:
            cost += hour_cost

    return cost

if __name__ == '__main__':
    print solution('10:00', '13:21')
    print solution('09:42', '11:42')
    print solution('10:00', '10:21')
    print solution('10:59', '11:01')
