def decimal_2_binary (number):
    result = ''
    while number > 0 :
        result = str(number % 2) + result
        number = number // 2
        if number // 2 == 0:
            return str(1)+result 
print (decimal_2_binary(255))
        
