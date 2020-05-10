def find_index(search_pattern, data):
        for (index, item) in enumerate(data):
            if search_pattern == item:
                return index


print(find_index('!', 'abc') is None)
print(find_index(42, []) is None)
print(find_index('t', 'cat'))
print (find_index(5, [1,2,3,4,5,6,7]))
