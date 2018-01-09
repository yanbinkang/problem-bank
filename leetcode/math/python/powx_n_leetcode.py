"""
Implement pow(x, n).

time complexity: nLogn because we're dividing n / 2 at every step.

Algo:

Logarithmic, O(log n).

The recursive solution has O(logn) memory complexity as it will consume memory on the stack.

A simple algorithm of this problem is to multiply 'x' by 'n' times. The time complexity of this algorithm would be O(n).

We can use divide and conquer approach to solving this problem more efficiently.

    - In divide step we keep dividing n by 2 recursively until we reach the base case i.e. n == 1
    - In combine step we get result 'r' of the sub-problem and compute result of the current problem using below two rules
        - if n is even, then result is r * r (where r is the result of sub-problem)
        - if n is odd, then result is x * r * r (where r is the result of sub-problem)

ref: https://www.educative.io/collection/page/5642554087309312/5679846214598656/170001
"""
def pow(x, n):
    if n == 0:
        return 1

    if n < 0:
        n = -n # remove negation
        x = 1 / x

    result = pow(x, n / 2)

    if n % 2 == 0:
        return result * result
    else:
        return x * result * result

if __name__ == '__main__':
    print pow(8, 4)
    print pow(5, 1)
    print pow(2, 4)
    print pow(4, 2)
