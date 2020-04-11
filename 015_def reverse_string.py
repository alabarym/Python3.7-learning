def reverse_string(string):
    index=len(string) - 1
    reverse_string = ''

    while index >= 0:
        current_char = string[index]
        reverse_string = reverse_string + current_char
        index = index -1
    
    return reverse_string

print (reverse_string('Reverse String'))
