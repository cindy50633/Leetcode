def two_sum(nums, target):
    def two_sum_subprocess(candiate1_index, candiate2_index_list, target):
        candiate1 = nums[candiate1_index]
        # if candiate1 > target:
        #     return two_sum_subprocess(candiate2_index_list[0], candiate2_index_list[1:], target)
        # else:
        for i in candiate2_index_list:
            if nums[i] == (target - candiate1):
                return [candiate1_index, i]
        return two_sum_subprocess(candiate2_index_list[0], candiate2_index_list[1:], target)
    return two_sum_subprocess(0, range(1, len(nums)), target)

two_sum([-1,-2,-3,-4,-5], -8)
