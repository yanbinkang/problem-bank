def find_rotation_pt(words):
    first_word = words[0]
    first_index = 0
    last_index = len(words) - 1

    while (first_index < last_index):
        mid_point = (first_index + last_index) // 2
        if words[mid_point] > first_word:
            # go right
            first_index = mid_point
        else:
            # go left
            last_index = mid_point

        # if first_index and last_index have converged
        if first_index + 1 == last_index:
            return last_index
