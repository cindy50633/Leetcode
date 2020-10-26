def valid_anagram1(s, t):
    s_str_count_dict = {}
    for s_sub_str in s:
        if s_sub_str in s_str_count_dict:
            s_str_count_dict[s_sub_str] += 1
        else:
            s_str_count_dict[s_sub_str] = 1
    for t_sub_str in t:
        try:
            s_str_count_dict[t_sub_str] -= 1
            if s_str_count_dict[t_sub_str] < 0:
                return False
        except:
            return False
    if sum(s_str_count_dict.values()) != 0:
        return False
    else:
        return True


def valid_anagram2(s, t):
    s_str_count_dict = {}
    for s_sub_str in s:
        if s_sub_str in s_str_count_dict:
            s_str_count_dict[s_sub_str] += 1
        else:
            s_str_count_dict[s_sub_str] = 1
    for t_sub_str in t:
        try:
            s_str_count_dict[t_sub_str] -= 1
            if s_str_count_dict[t_sub_str] < 0:
                return False
        except:
            return False
    if sum(s_str_count_dict.values()) != 0:
        return False
    else:
        return True

valid_anagram('anagram', 'nagaram')
