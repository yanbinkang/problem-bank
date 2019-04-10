def test(n):
    result = [['#' for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(i):
            result[i][j] = ' '

    for i in reversed(range(len(result))):
        print ''.join(result[i])


def reverse_rec(head, tail):
    return helper(head, None)


def helper(head, tail):
    if head is None: tail

    next_node = head.next
    head.next = tail

    return helper(next_node, tail)


if __name__ == '__main__':
    test(8)
