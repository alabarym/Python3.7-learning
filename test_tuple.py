import tuple

def tet_sort_pair():
    assert tuple.sort_pair((5, 1)) == (1, 5)
    assert tuple.sort_pair((2.,2)) == (2, 2)
    assert tuple.sort_pair((7, 8)) == (7, 8)