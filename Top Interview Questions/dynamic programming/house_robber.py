def rob_recurseive(nums): # recursive O(2**n)
    if not nums:
        return 0
    index_limit = len(nums) - 1
    def rob_helper(index, index_limit):
        if index > index_limit:
            return 0

        return max(nums[index] + rob_helper(index+2, index_limit), rob_helper(index+1, index_limit))
    print(rob_helper(2,index_limit))
    print('QQ')
    return rob_helper(0, index_limit)

print(rob_recurseive([2,1,1,2]))

def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    index_limit = len(nums)
    rob_table = [0 for i in range(index_limit)]
    rob_table.extend([0, 0])
    for i in range(index_limit-1, -1, -1):
        rob_table[i] = max(nums[i] + rob_table[i+2], rob_table[i+1])
    print(rob_table)
    return rob_table[0]

print(rob([2,1,1,2]))
