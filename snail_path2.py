# -*- coding:utf-8 -*-
"""Snail game. Matrix can be represented by two lists."""

import copy

def upper_row(list1, path):
    if list1:
        list2 = copy.deepcopy(list1)
        for items in list2[0]:
            path.append(list1[0].pop(0))
        if list1.count([]):
            list1.remove([])    
    return list1, path

def right_column(list1, path):
    if list1:
        counter2 = 0
        matrix_length = len(list1) -1
        while counter2 <= matrix_length:
            path.append(list1[counter2].pop(-1))
            counter2 += 1
    return list1, path

def bottom_row(list1, path):
    if list1:
        list2 = copy.deepcopy(list1)
        for items in list2[-1]:
            path.append(list1[-1].pop(-1))
        if list1.count([]):
            list1.remove([])
    return list1, path

def left_column(list1, path):
    if list1:
        matrix_length = len(list1)
        counter4 = 1
        while counter4 <= matrix_length:
            path.append(list1[-counter4].pop(0))
            counter4 += 1
    return list1, path

def get_snail_path(list1, path):
    upper_row(list1, path)
    right_column(list1, path)
    bottom_row(list1, path)
    left_column(list1, path)
    if list1:
        get_snail_path(list1, path)
    return list1, path

def snail_path(list1):
    path = []
    if not list1 or list1 == [] or list1 == [[]]:
        return path
    elif list1 == [0] or list1 == [[0]]:
        path = [0]
        return path
    elif len(list1[0]) == 1:
        i = 0
        while i < len(list1):
            path.extend(list1[i])
            i += 1
    else:
        for items in list1:
            get_snail_path(list1, path)
    return path


print(snail_path([[1, 2, 3, 4]]))
print(snail_path([[1, 2], [3, 4]]))
print(snail_path([[1, 2, 3, 4], [5, 6, 7, 8]]))
print(snail_path([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]))
print(snail_path([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]))

print(snail_path([
    [1, 2, 3,  4,  5,  6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17],
    [18, 19, 20, 21, 22],
    [23, 24, 25, 26, 27]
]))




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
