from time import time
from divide_and_conquer import l_fill as fill_dc
from divide_and_conquer_seq import l_fill as fill_dcs
from dynamic_programming import l_fill as fill_dp


def main():
    RANGE_S = 4
    RANGE_E = 10

    performance = [[[None]
                    for i in range(RANGE_S, RANGE_E + 1)] for j in range(3)]

    algorithms = [fill_dc, fill_dcs, fill_dp]

    for idx, fill_func in enumerate(algorithms):
        for n in range(RANGE_S, RANGE_E + 1):
            start = time()
            fill_func(n)
            time_costing = time() - start
            performance[idx][n - RANGE_S] = time_costing

    for row in performance:
        for col in row:
            print('{:.5f}'.format(col).rjust(10, ' '), end='')
        print()


if __name__ == '__main__':
    main()
