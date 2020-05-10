def find_index(search_pattern, data):
        for (index, item) in enumerate(data):
            if search_pattern == item:
                return index


def find_second_index(search_pattern, old_data):
        data = iter(old_data)
        first_index = find_index(search_pattern, data)
        for (index, item) in enumerate(data):
            if search_pattern == item:
                return first_index + index + 1

# print(find_index('!', 'abc') is None)
# print(find_index(42, []) is None)
# print(find_index('t', 'cat'))
# print(find_index(5, [1, 2, 3, 4, 5, 6, 7]))

print(find_second_index('!', 'abc') is None)
print(find_second_index(42, []) is None)
print(find_second_index('t', 'kitten'))
print(find_second_index(5, [1,2,3,4,5,6,7,5,8,10,5]))
