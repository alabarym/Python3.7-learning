def shouter(string):
    length = len(string)
    result = ''
    if  length > 0 and \
        length < 5:
            return string
    elif length == 5:
        counter5 = 0
        while counter5 != 10:
            result += string
            counter5 += 1
    elif length > 5:
        counter = 0
        while counter != 100:
            result += string
            counter += 1
    return result

print (shouter("123456"))
