def find_first_unique_in_str(s):
    str_count_dict = {}
    result_pair = [float('inf'), -1]
    for index, sub_s in enumerate(s):
        if sub_s in str_count_dict:
            str_count_dict[sub_s][1] += 1
        else:
            str_count_dict[sub_s] = [index, 1]
    for sub_s, current_result_pair in str_count_dict.items():
        if current_result_pair[1] == 1 and current_result_pair[0] < result_pair[0]:
            result_pair[0] = current_result_pair[0]
            result_pair[1] = current_result_pair[1]
    if result_pair[1] == -1:
        return -1
    else:
        return result_pair[0]
