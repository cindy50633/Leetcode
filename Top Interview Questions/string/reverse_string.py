def reverse_string(s):
    replace_times = int(len(s)/2)
    for i in range(replace_times):
        tmp_string = s[i]
        s[i] = s[-(i+1)]
        s[-(i+1)] = tmp_string
