def sort_pair(x):
    if x[1] > x[0]:
        return x
    x = x[1], x[0]
    return x
#print(sort_pair((4,2)))
