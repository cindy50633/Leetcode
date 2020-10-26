def get_square_id(index):
    if index in (0, 1, 2):
        index_id = 1
    elif i in (3, 4, 5):
        index_id = 4
    else:
        index_id = 7
    return index_id

print(get_square_id(8))
