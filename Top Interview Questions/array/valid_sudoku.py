def is_valid_sudoku(board):
    check_column_set_dict = {j:set() for j in range(9)}
    check_square_set_dict = {
        (1,1):set(),
        (1,4):set(),
        (1,7):set(),
        (4,1):set(),
        (4,4):set(),
        (4,7):set(),
        (7,1):set(),
        (7,4):set(),
        (7,7):set()
    }
    def get_square_id(index):
        if index in (0, 1, 2):
            index_id = 1
        elif index in (3, 4, 5):
            index_id = 4
        else:
            index_id = 7
        return index_id
    def check_if_exist(current_sudoku_num, target_set):
        if current_sudoku_num in target_set:
            return True
        else:
            target_set.add(current_sudoku_num)
            return False
    for i in range(9):
        check_row_set = set()
        for j in range(9):
            current_sudoku_num = board[i][j]
            i_id = get_square_id(i)
            j_id = get_square_id(j)
            if current_sudoku_num == '.':
                continue
            if check_if_exist(current_sudoku_num, check_row_set):
                return False
            if check_if_exist(current_sudoku_num, check_column_set_dict[j]):
                return False
            if check_if_exist(current_sudoku_num, check_square_set_dict[(i_id, j_id)]):
                return False
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


print(is_valid_sudoku(board))
# print(board[4])
