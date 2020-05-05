def duplicate(original_list):
    original_list.extend(original_list) 
    print (original_list)

original_list = [1, 2]
duplicate(original_list)