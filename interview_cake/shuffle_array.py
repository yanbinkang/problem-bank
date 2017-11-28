from random import randint
def shuffle_array(a_list):
    if len(a_list) <= 1:
        return a_list

    for index, num in enumerate(a_list):
        rand_num = randint(index, len(a_list)-1)
        temp = a_list[rand_num]
        a_list[rand_num] = a_list[index]
        a_list[index] = temp

    return a_list

print(shuffle_array([1, 2, 3, 4, 5, 6, 7]))

# Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >=floor and <=ceiling.
# def shuffle(the_array):
#     # if it's 1 or 0 items, just return
#     if len(the_array)  <= 1:
#         return the_array

#     last_index_in_the_array = len(the_array) - 1

#     # walk through from beginning to end
#     for index_we_are_choosing_for in xrange(0, len(the_array)):

#         # choose a random not-yet-placed item to place there
#         # (could also be the item currently in that spot)
#         # must be an item AFTER the current item, because the stuff
#         # before has all already been placed
#         random_choice_index = get_random(index_we_are_choosing_for, last_index_in_the_array)

#         # place our random choice in the spot by swapping
#         the_array[index_we_are_choosing_for], the_array[random_choice_index] = the_array[random_choice_index], the_array[index_we_are_choosing_for]
