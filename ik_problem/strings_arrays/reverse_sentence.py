def reverse_sentence(sentence):
    n = len(sentence)
    input = list(sentence)
    rev_sen = reverse(input, 0, n-1)

    i = 0
    position = 0

    while i <= n:
        # this line is very important. reverse the order and you'll get an IndexError
        if i == n or rev_sen[i] == ' ':
            reverse(rev_sen, position, i - 1)
            position = i + 1

        i += 1

    return ''.join(rev_sen)



def reverse(a_list, first, last):
    while first < last:
        temp = a_list[first]
        a_list[first] = a_list[last]
        a_list[last] = temp

        first += 1
        last -= 1

    return a_list

sen = 'boys love girls'
print reverse_sentence(sen)
