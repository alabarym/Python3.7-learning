def my_substr(string, length):
    index = 0
    substring = ''
    while index < length:
        current_char = string[index]
        substring = substring + current_char
        index = index +1
    return substring

print(my_substr('123456789',5))
