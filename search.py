

def binarySearch(t, A):
    l, u = 0, len(A) - 1
    
    while l <= u:

        M = l + (u - l) // 2
        if A[M] < t:
            l = M + 1
        elif A[M] == t:
            return M
        else:
            U = M - 1
    return -1

def search_first_k(A, k):
    """ Search for first occurence of k
    """
    left, right, result = 0, len(A) - 1, -1

    while left <= right:
        M = (left + right) // 2
        if k < A[M]:
            right = M - 1
        elif k == A[M]:
            result = M
            right = M - 1
        else:
            left = M + 1
    
    return result

def searh_entry_equal_to_its_index(A):
    """ Search for first occurence of k
    """
    left, right = 0, len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        difference = A[mid] - mid
        # A[mid] == mid if and only if difference == 0
        if difference ==  0:
            return mid
        elif difference > 0:
            right = M - 1
        else:
            left = M + 1
    
    return -1
if __name__ == "__main__":
    data = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    print(search_first_k(data, 285))