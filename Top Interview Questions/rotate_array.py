def rotate_array(nums, key) -> list:
    left_nums = nums[:key+1]
    right_nums = nums[-key:]
    nums = right_nums + left_nums
    return nums

def rotate_array_in_place(nums, key) -> list:
    previous_i = 0
    print(previous_i)
    previous_value = nums[previous_i]
    replace_times = 0
    while replace_times < len(nums):
        replace_i = (previous_i + key) % len(nums)
        print(replace_i)
        replace_value = nums[replace_i]
        nums[replace_i] = previous_value
        previous_i = replace_i

        previous_value = replace_value
        print(previous_i)
        replace_times += 1
        print(nums)
    return nums


rotate_array_in_place([0,1,2,3,4,5,6,7,8], 3)
                       # 3,4,5,1,2,3
