"""Divide and Conquer approach with filling in sequence
"""
pile = 1


def _fill_(board, top_left, filled, size):
    """Fill L blocks on bard

    Args:
        board: 2-demension list to store the filled values.
        top_left: the top-left cell coordinate: (row_index, column_index); e.g. (0, 0)
        filled: the filled cell coordinate: (row_index, column_index); e.g. (0, 0)
        size: size of square
    """
    if size == 1:
        return

    global pile
    fill_val = pile = pile + 1

    s = size // 2

    # fill top-left
    if filled[0] < (top_left[0] + s) and filled[1] < (top_left[1] + s):
        _fill_(board, top_left, filled, s)
    else:
        board[top_left[0] + s - 1][top_left[1] + s - 1] = fill_val
        _fill_(board, top_left, (top_left[0] + s - 1, top_left[1] + s - 1), s)

    # fill top-right
    if filled[0] < (top_left[0] + s) and filled[1] >= (top_left[1] + s):
        _fill_(board, (top_left[0], top_left[1] + s), filled, s)
    else:
        board[top_left[0] + s - 1][top_left[1] + s] = fill_val
        _fill_(board, (top_left[0], top_left[1] + s),
               (top_left[0] + s - 1, top_left[0] + s), s)

    # fill bottom-left
    if filled[0] >= (top_left[0] + s) and filled[1] < (top_left[1] + s):
        _fill_(board, (top_left[0] + s, top_left[1]), filled, s)
    else:
        board[top_left[0] + s][top_left[1] + s - 1] = fill_val
        _fill_(board, (top_left[0] + s, top_left[1]),
               (top_left[0] + s, top_left[1] + s - 1), s)

    # fill bottom-right
    if filled[0] >= (top_left[0] + s) and filled[1] >= (top_left[1] + s):
        _fill_(board, (top_left[0] + s, top_left[1] + s), filled, s)
    else:
        board[top_left[0] + s][top_left[1] + s] = fill_val
        _fill_(board, (top_left[0] + s, top_left[1] + s),
               (top_left[0] + s, top_left[1] + s), s)


def l_fill(n):
    if n < 1:
        return []

    global pile
    pile = 0

    size = pow(2, n)
    result = [[None for i in range(size)] for j in range(size)]

    # 1st, fill the center
    result[size // 2 - 1][size // 2 - 1] \
        = result[size // 2][size // 2 - 1] \
        = result[size // 2][size // 2] \
        = 0

    # 2nd, fill the divided sub-board except the top-right
    degrade_size = size // 2
    _fill_(result, (0, 0), (degrade_size - 1, degrade_size - 1), degrade_size)
    _fill_(result, (degrade_size, 0),
           (degrade_size, degrade_size - 1), degrade_size)
    _fill_(result, (degrade_size, degrade_size),
           (degrade_size, degrade_size), degrade_size)

    return result


if __name__ == '__main__':
    from utils import print_board, time_costing
    func = time_costing(l_fill)
    board = func(3)
    print_board(board)
