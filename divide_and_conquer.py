"""Divide and Conquer approach.
"""
pile = 1


def _fill_(arr, top_left, size):
    """Fill L blocks.

    Args:
        arr: 2-demension list to store the filled values.
        top_left: the top-left cell coordinate: (row_index, column_index); e.g. (0, 0)
        size: the size of a board, should be even; e.g. 4
    """
    if size <= 1:
        return

    global pile
    fill_val = pile = pile + 1

    delta = size // 2

    # top-left cell is filled
    if arr[top_left[0]][top_left[1]] is not None:
        arr[top_left[0] + delta - 1][top_left[1] + delta] \
            = arr[top_left[0] + delta][top_left[1] + delta - 1] \
            = arr[top_left[0] + delta][top_left[1] + delta] \
            = fill_val
    # top-right cell is filled
    elif arr[top_left[0]][top_left[1] + size - 1] is not None:
        arr[top_left[0] + delta - 1][top_left[1] + delta - 1] \
            = arr[top_left[0] + delta][top_left[1] + delta - 1] \
            = arr[top_left[0] + delta][top_left[1] + delta] \
            = fill_val
    # bottom-right cell is filled
    elif arr[top_left[0] + size - 1][top_left[1] + size - 1] is not None:
        arr[top_left[0] + delta - 1][top_left[1] + delta - 1] \
            = arr[top_left[0] + delta - 1][top_left[1] + delta] \
            = arr[top_left[0] + delta][top_left[1] + delta - 1] \
            = fill_val
    # bottom-left cell is filled
    elif arr[top_left[0] + size - 1][top_left[1]] is not None:
        arr[top_left[0] + delta - 1][top_left[1] + delta - 1] \
            = arr[top_left[0] + delta - 1][top_left[1] + delta] \
            = arr[top_left[0] + delta][top_left[1] + delta] \
            = fill_val

    # fill sub-board
    degrade_size = size // 2
    _fill_(arr, top_left, degrade_size)
    _fill_(arr, (top_left[0], top_left[1] + degrade_size), degrade_size)
    _fill_(arr, (top_left[0] + degrade_size,
           top_left[1] + degrade_size), degrade_size)
    _fill_(arr, (top_left[0] + degrade_size, top_left[1]), degrade_size)


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
    _fill_(result, (degrade_size, degrade_size), degrade_size)
    _fill_(result, (degrade_size, 0), degrade_size)
    _fill_(result, (0, 0), degrade_size)

    return result


if __name__ == '__main__':
    from utils import print_board, time_costing
    func = time_costing(l_fill)
    board = func(3)
    print_board(board)
