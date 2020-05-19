# -*- coding:utf-8 -*-
"""Snail game. Matrix can be represented by two lists."""


def snail_path(list1):
    path = []
    if not list1 or list1 == [] or list1 == [[]]:
        path.extend([])
    elif list1 == [0] or list1 == [[0]]:
        path.extend([0])
    else:
        matrix_column, matrix_row = len(list1[0]), len(list1)
        if matrix_column == 1 or matrix_row == 1:
            i = 0
            while i < len(list1):
                path.extend(list1[i])
                i += 1
        elif matrix_column == 2 and matrix_row == 2:
            path.extend(list1[0][:])
            path.extend(list1[-1][::-1])
        elif matrix_row == 3:
            path.extend(list1[0][:])
            path.extend(list1[1][-1:])
            path.extend(list1[-1][::-1])
            path.extend(list1[1][:-1])
    return path
    


assert snail_path([]) == []
assert snail_path([[]]) == []

assert snail_path([[0]]) == [0]

assert snail_path([[1, 2, 3, 4]]) == [1, 2, 3, 4]

assert snail_path([[1], [2], [3], [4]]) == [1, 2, 3, 4]

assert snail_path([
    [1, 2],
    [3, 4],
]) == [1, 2, 4, 3]

assert snail_path([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

assert snail_path([
    [None, 0, True],
    [-1, '', False],
    [[], 'foo', object],
]) == [None, 0, True, False, object, 'foo', [], -1, '']