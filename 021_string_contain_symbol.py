def does_contain(string, symbol):
    counter = 0
    while_counter = 0
    while while_counter < len(string):
        current_char = string[while_counter]
        if current_char == symbol:
            return True
        while_counter += 1
    return False

print(does_contain("sansa stark", "s"))
print(does_contain("sansa stark", "z"))
