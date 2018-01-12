"""
https://leetcode.com/problems/find-the-celebrity/#/description

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

O(n) calls to knows(a, b); O(1) space
"""
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

def find_celebrity(n):
    """
    :type n: int
    :rtype: int
    """
    celebrity = 0

    for i in range(1, n):
        if knows(celebrity, i): # celebrity knows someone, is not a celebrity
            celebrity = i # find a new celebrity

    for i in range(n):
        if i == celebrity: # celebrity knows self. we don't care about this
            continue

        # if celebrity knows another person, then s/he is not a celebrity.
        # if no one knows the celebrity, then s/he is not a celebrity.
        if knows(celebrity, i) or not knows(i, celebrity):
            return -1

    return celebrity

# https://discuss.leetcode.com/topic/23550/ac-java-solution-using-stack
def find_celebrity_1(n):
    if n <= 0: return -1
    if n == 1: return 0

    stack = 0

    # put all the people on the stack
    for i in range(n):
        stack.append(i)

    a, b = 0, 0

    while len(stack) > 1: # because we need to pop to elements always
        a = stack.pop()
        b = stack.pop()

        if know(a, b):
            # a knows b, so a is not the celebrity, but b may be
            stack.append(b)
        else:
            # a doesn't know b, so a may be.
            stack.append(a)

        # celebrity is the last item on stack. check if this guy is real celebrity
        c = stack.pop()

        for i in range(n):
            # c should not know anyone else
            """
            return -1:
                1. since celebrity knows self i != c
                2. celebrity should not know anyone
                3. if no one knows the celebrity
            """
            if i != c and (knows(c, i) or not knows(i, c)):
                return -1

        return c
