

def binarySearch(t, A):
    l, u = 0, len(A) - 1
    
    while l <= u:

        M = l + (u - l) / 2
        if A[M] < t:
            l = M + 1
        elif A[M] == t:
            return M
        else:
            U = M - 1
    return -1