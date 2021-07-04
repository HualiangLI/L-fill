"""Dynamic Programming approach."""


def transform(board):
    size = len(board)

    tl = [[None for i in range(size)] for j in range(size)]
    br = [[None for i in range(size)] for j in range(size)]

    for row in range(size):
        for col in range(size):
            tl[row][col] = board[size - col - 1][row]
            br[row][col] = board[col][size - row - 1]

    return tl, br


def l_fill(n):
    if n < 1:
        return[]

    if n == 1:
        return [
            [1, 0],
            [1, 1],
        ]

    if n == 2:
        return [
            [1, 1, None, None],
            [1, 0, None, None],
            [2, 0,    0,    3],
            [2, 2,    3,    3],
        ]

    size = pow(2, n)
    result = [[None for i in range(size)] for j in range(size)]

    # top-left
    base = [
        [1, 1, None, None],
        [1, 0, None, None],
        [2, 0,    0,    3],
        [2, 2,    3,    3],
    ]
    for i in range(3, n+1):
        top_left, btm_right = transform(base)
        table = [[None for i in range(size)] for j in range(pow(2, i))]
        s = pow(2, i - 1)
        S = pow(2, i)
        # fill top-left
        for row in range(0, s):
            for col in range(0, s):
                table[row][col] = top_left[row][col]
        # fill bottom-left
        for row in range(s, S):
            for col in range(0, s):
                table[row][col] = base[row - s][col]
        # fill bottom-right
        for row in range(s, S):
            for col in range(s, S):
                table[row][col] = btm_right[row - s][col - s]

        center_s = pow(2, i-2)
        center_e = pow(2, i-1) + pow(2, i-2)
        # fill center
        for row in range(center_s, center_e):
            for col in range(center_s, center_e):
                table[row][col] = base[row - center_s][col - center_s]
        base = table

    return base


if __name__ == '__main__':
    from utils import print_board, time_costing
    func = time_costing(l_fill)
    board = func(4)
    print_board(board)
