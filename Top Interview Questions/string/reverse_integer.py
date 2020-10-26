def reverse_integer(x):
    reverse_int = 0
    is_minus_x = True if x < 0 else False
    x = abs(x)
    while x > 0:
        reverse_int = (10 * reverse_int) + x % 10
        x //= 10
    if is_minus_x:
        reverse_int = -reverse_int
        if reverse_int < -(2**31):
            return 0
    else:
        if reverse_int > 2**31 - 1:
            return 0
    return reverse_int
