"""
solution: http://www.programcreek.com/2012/12/leetcode-3sum/
"""
def three_sum(a_list):
    res = []

    if len(a_list) < 3:
        return res

    sorted_array = sorted(a_list)

    i = 0
    while i < len(sorted_array) - 2:
        if i == 0 or sorted_array[i] > sorted_array[i - 1]:
            negate = -sorted_array[i]

            start = i + 1
            end = len(sorted_array) - 1

            while start < end:
                if sorted_array[start] + sorted_array[end] == negate:
                    temp = []
                    temp.append(sorted_array[end])
                    temp.append(sorted_array[start])
                    temp.append(sorted_array[i])

                    res.append(temp)
                    start += 1
                    end -= 1

                    # avoid duplicate solutions
                    while (start < end and sorted_array[end] == sorted_array[end + 1]):
                        end -= 1

                    while start < end and sorted_array[start] == sorted_array[start - 1]:
                        start -= 1

                elif sorted_array[start] + sorted_array[end] < negate:
                    start += 1
                else:
                    end -= 1

        i += 1

    return res

print three_sum([-1, 0, 1, 2, -1, -4])
