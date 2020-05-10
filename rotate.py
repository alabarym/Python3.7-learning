def rotate(some_list):
    if len(some_list) > 0:
        last_value = some_list.pop()
        some_list.insert(0,last_value)
        
list1 = []
print(len(list1))
print(list1, end='\n')
rotate(list1)
print(list1, end='\n')
