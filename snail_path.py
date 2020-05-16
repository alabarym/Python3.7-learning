# -*- coding:utf-8 -*-
"""Snail game. Matrix can be represented by two lists."""


def snail_path(list1):
    matrix_column, matrix_row = len(list1[0]), len(list1)
    path = []
    if matrix_column == 2 and matrix_row ==2:
        path.extend(list1[0][:])
        path.extend(list1[-1][::-1])
    elif matrix_column == 3 and matrix_row == 3:
        path.extend(list1[0][:])
        path.extend(list1[1][-1:])
        path.extend(list1[-1][::-1])
        path.extend(list1[1][:-1])
    print (path, end=' ')
    print ('\n')

snail_path([[1, 2], [3, 4]])    
snail_path([[1,2,3], [5,7,8], [9,11,13]])
snail_path([['b', 'c', 'a'], ['3', True, 11], [None, 'foo', 0]])



# 1   2   3   5
# 5   7   8   9
# 9   11  13  1
# 4   8   9   0
