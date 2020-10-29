def climb_stairs(n):
    climb_way_table = [1, 2]
    m = 2
    while m < 45:
        climb_way_table.append(climb_way_table[m-1] + climb_way_table[m-2])
        m += 1
    return climb_way_table[n-1]
