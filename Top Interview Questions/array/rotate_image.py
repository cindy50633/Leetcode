def rotate_image(matrix):
    row_len = len(matrix[0])
    column_len = len(matrix)
    count_outer = 0
    while count_outer < int(column_len/2):
        for i in range(count_outer, column_len - count_outer):
            count_inner = 0
            for j in range(count_outer, row_len - count_outer):
                count_inner += 1
                end_index = row_len - 1 - i
                relative_index = row_len - 1 - j
                replaced = matrix[j][end_index]
                matrix[j][end_index] = matrix[i][j]
                matrix[i][j] = matrix[relative_index][i]
                matrix[relative_index][i] = matrix[end_index][relative_index]
                matrix[end_index][relative_index] = replaced
                print(i)
                if count_inner == row_len - 1 - 2 * count_outer:
                    break
            count_outer += 1
            # print(matrix)
            break
    print(matrix)


matrix1 = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
rotate_image(matrix1)
