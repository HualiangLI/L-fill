from time import time


def print_board(arr, width=5):
    """Print a 2-demension array prettily

    Args:
        arr: the 2-demension array
    """
    size = len(arr)

    def g(x): return f'{x}'.rjust(width, ' ')

    for i in range(size):
        for j in range(size):
            print(g(arr[i][j]), end='')
        print('')


def time_costing(func):
    """Calculate the running time of a function"""
    def _wrapper_(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('time costing:', time() - start)
        return result
    return _wrapper_
