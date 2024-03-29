import g_o_l


def board_testing():
    row, col = 100, 100

    n, m = 10, 300
    assert g_o_l.board_testing(n, m, row, col) == False

    n, m = -10, 100
    assert g_o_l.board_testing(n, m, row, col) == False

    n, m = 100, 100
    assert g_o_l.board_testing(n, m, row, col) == True


def neighbour_tester():
    is_neighbour = [[False, True], [True, False]]
    result = [[2, 1], [1, 2]]
    assert g_o_l.neighbours_count(is_neighbour) == result

    is_neighbour = [[False, True, False],
                       [True, False, False],
                       [True, False, True]]
    result = [[2, 1, 1], [2, 4, 2], [1, 3, 0]]
    assert g_o_l.neighbours_count(is_neighbour) == result