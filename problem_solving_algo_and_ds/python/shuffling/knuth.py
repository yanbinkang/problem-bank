# Pseudocode: http://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

from random import seed, randint


def shuffle(a_list):
    seed()
    for i in reversed(range(len(a_list))):
        j = randint(0, 1)
        temp = a_list[i]
        a_list[i] = a_list[j]
        a_list[j] = temp

    return a_list

print shuffle([1, 2, 3, 4, 5])
