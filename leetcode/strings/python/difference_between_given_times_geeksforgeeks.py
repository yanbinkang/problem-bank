"""
Given two times in string "HH:MM" format. Here "H" shows hours and "M" shows minutes. You have to find the difference in same string format between these two strings. But both given strings should follow these cases.

1) Time 1 will be less than or equal to time2
2) Hours will be possible from 0 to 23.
3) Minutes will be possible from 0 to 59

Examples:

Input : s1 = "14:00";
        s2 = "16:45";
Output : result = "2:45"

Input : s1 = "1:04"
        s2 = "13:05"
Output : result = "12:01"

ref: https://stackoverflow.com/questions/10742296/python-time-conversion-hms-to-seconds
"""
def diff2(s1, s2):
    h1, m1 = [int(i) for i in s1.split(':')]
    h2, m2 = [int(i) for i in s2.split(':')]

    # muitlply hours by 60 to convert to minutes
    h1 *= 60
    h2 *= 60

    # find difference
    duration = (h2 + m2) - (h1 + m1)

    total_hours = duration / 60
    total_mins = duration % 60

    return str(total_hours) + ':' + str(total_mins)


def diff(s1, s2):
    time1 = int(''.join(s1.split(':')))
    time2 = int(''.join(s2.split(':')))

    hour_diff = (time2 / 100) - (time1 / 100) - 1

    min_diff = time2 % 100 + (60 - time1 % 100)

    if min_diff >= 60:
        hour_diff += 1
        min_diff = min_diff - 60

    result = str(hour_diff) +  ':' + str(min_diff)

    return result

if __name__ == '__main__':
    print diff('14:00', '16:45')
    print diff2('14:00', '16:45')
