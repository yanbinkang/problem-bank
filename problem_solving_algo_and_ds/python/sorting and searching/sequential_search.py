def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found
