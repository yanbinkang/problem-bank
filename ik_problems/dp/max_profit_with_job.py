"""
http://www.cs.princeton.edu/courses/archive/spr05/cos423/lectures/06dynamic-programming.pdf
Given set of jobs with start and end interval and profit, how to maximize profit such that jobs in subset do not overlap.
input format (start, finish, profit)
"""

def maximize_profit_with_job(jobs):

    # sorted by endtime
    sorted_jobs = sorted(jobs, key=lambda x:x[1])

    result = []

    for start, end, profit in sorted_jobs:
        result.append(profit)

    i = 0
    while i < len(result):
        j = 0
        while j < i:
            # jobs do not overlap
            if sorted_jobs[i][0] >= sorted_jobs[j][1]:
                result[i] = max(result[j] + sorted_jobs[i][2], result[i])
            j += 1
        i += 1

    return max(result)

if __name__ == '__main__':
    input_1 = [(7, 9, 2), (1, 3, 5), (5, 8, 11), (2, 5, 6), (6, 7, 4), (4, 6, 5)]
    input_2 = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 6), (11, 15, 3), (7, 9, 4)]
    print maximize_profit_with_job(input_1)
    print maximize_profit_with_job(input_2)
