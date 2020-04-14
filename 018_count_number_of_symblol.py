#018_count_number_of_symblol.py
def count_chars(string, symbol):
    counter = 0
    while_counter = 0
    while while_counter < len(string):
        current_char = string[while_counter]
        if current_char == symbol : 
            counter += 1
        while_counter += 1
    return counter

print (count_chars("sansa stark","s"))
