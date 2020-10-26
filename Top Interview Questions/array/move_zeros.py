def move_zeros(nums):
    expected_execute_times = len(nums)
    execute_times = 0
    def move_zeros_subprocess(check_index, execute_times):
        if execute_times == expected_execute_times:
            return
        else:
            execute_times += 1
            if nums[check_index] == 0:
                del nums[check_index]
                nums.append(0)
            else:
                check_index += 1
            return move_zeros_subprocess(check_index, execute_times)
    move_zeros_subprocess(0, execute_times)
