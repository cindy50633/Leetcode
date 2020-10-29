def maximum_subarray(nums):
    ori_nums = nums.copy()
    max_sum = nums[0]
    start_index = 0
    end_index = 0
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        if max_sum < nums[i]:
            if nums[i-1] < 0:
                start_index = i
            max_sum = nums[i]
            end_index = i
    print(ori_nums[start_index:end_index+1])
    return max_sum

# print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(maximum_subarray([1]))
