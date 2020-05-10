def find_second_index(search_pattern, original_data):
        data = iter(original_data)
        counter = 0
        for (index, item) in enumerate(data):
            if search_pattern == item and counter == 1:
                return index
            if search_pattern == item:
                counter += 1


print(find_second_index('!', 'abc') is None)
print(find_second_index(42, []) is None)
print(find_second_index('t', 'kitten'))
print(find_second_index(5, [1,2,3,4,5,6,7,5,8,10,5]))
