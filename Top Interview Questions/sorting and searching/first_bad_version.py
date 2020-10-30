def first_bad_version_linear(n): #linear search
    for i in range(1, n+1):
        if isBadVersion(i):
            return i
    return 0

def first_bad_version_divide_and_conquer(n): #linear search
    def first_bad_version_helper(beg_n, end_n):
        if beg_n == end_n:
            return beg_n
        mid_n = int((beg_n + end_n) / 2)
        if isBadVersion(mid_n):
            return first_bad_version_helper(beg_n, mid_n)
        else:
            return first_bad_version_helper(mid_n+1, end_n)
    return first_bad_version_helper(1, n)
