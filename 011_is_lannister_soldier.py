def is_lannister_soldier(armor_colour, shield_symbol):
    return (armor_colour == 'red' and shield_symbol is None) or (shield_symbol == 'lion') 
print is_lannister_soldier('red', 'whale')
print is_lannister_soldier('white', 'lion')
