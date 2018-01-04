def find_subsets(subset, input):
    if not input:
        print subset
    else:
        # add to subset, remove from input, recur
        find_subsets(subset + [input[0]], input[1:])
        # don't add to subset, remove from input, recur
        find_subsets(subset, input[1:])

find_subsets([], [1, 2, 3, 4])
