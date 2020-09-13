def contain_duplicate(nums)->bool:
    if nums:
        nums = merge_sort(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
    return False


n = 0
def merge_sort(nums)->list:
    global n
    n += 1
    if len(nums) > 1:
        mid = len(nums) // 2
        left_nums = nums[:mid]
        right_nums = nums[mid:]
        left_nums = merge_sort(left_nums)
        right_nums = merge_sort(right_nums)

        nums = []
        w = 0

        while len(left_nums) > 0 and len(right_nums) > 0:
            w += 1
            if left_nums[0] < right_nums[0]:
                nums.append(left_nums.pop(0))
            else:
                nums.append(right_nums.pop(0))
        l = 0
        for v in left_nums:
            l += 0
            nums.append(v)
        r = 0
        for v in right_nums:
            r += 1
            nums.append(v)
        n += max(l, r, w)
    return nums

merge_sort([i for i in range(500000)])
print(n)
