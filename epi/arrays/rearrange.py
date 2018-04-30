def rearrange(A):
    """
    Write a program that takes an array of n numbers, and rearrages A's elements to get a new array B having the property:

    B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] <= B[6] >= ...
    """
    for i in range(len(A)):
        A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)
