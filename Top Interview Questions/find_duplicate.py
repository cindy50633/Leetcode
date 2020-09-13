def contain_duplicate(nums)->bool:
    if len(nums) > 2:
        mid = len(nums) // 2
        contain_duplicate(nums[:mid])
        contain_duplicate(nums[mid+1:])
    elif len(nums) == 2:
        if nums[0] == nums[1]:
            print('true')
            return True
    else:
        print('false')
        return False


def merge_sort(nums)->list:
    print(nums)
    if len(nums) > 1:
        mid = len(nums) // 2
        left_nums = nums[:mid]
        right_nums = nums[mid:]

        left_nums = merge_sort(left_nums)
        right_nums = merge_sort(right_nums)

        nums = []

        while len(left_nums) > 0 and len(right_nums) > 0:
            print('left_nums = ' + str(left_nums))
            print('right_nums = ' + str(right_nums))
            if left_nums[0] < right_nums[0]:
                print('before pop:' + str(left_nums))
                nums.append(left_nums.pop(0))
                print('after pop:' + str(left_nums))
            else:
                print('before pop:' + str(right_nums))
                nums.append(right_nums.pop(0))
                print('before pop:' + str(right_nums))
            print('nums = ' + str(nums))
            # print(nums)
        for v in left_nums:
            nums.append(v)
        for v in right_nums:
            nums.append(v)
        return nums

merge_sort([9,8,7,6,5,4,3,2,1])
