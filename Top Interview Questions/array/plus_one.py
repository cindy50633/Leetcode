def plus_one(digits):
    check_index = -1
    def plus_one_subprocess(check_index, digits):
        if check_index < -len(digits):
            return [1] + digits
        else:
            if digits[check_index] != 9:
                digits[check_index] += 1
                return digits
            else:
                digits[check_index] = 0
                return plus_one_subprocess(check_index-1, digits)
    return plus_one_subprocess(check_index, digits)
