def is_arguments_for_substr_correct(string, index, string_length):
    if index < 0 : 
        return False
    elif string_length < 0:
        return False
    elif index > string_length -1 :
        return False
    elif len(string) < (string_length + index ) :
        return False     
    else: 
        return True   
  
string = 'Sansa Stark'
print(is_arguments_for_substr_correct(string, -1, 3))
print(is_arguments_for_substr_correct(string, 4, 100)) 
print(is_arguments_for_substr_correct(string, 10, 10)) 
print(is_arguments_for_substr_correct(string, 11, 1))  
print(is_arguments_for_substr_correct(string, 3, 3))  
print(is_arguments_for_substr_correct(string, 0, 5))