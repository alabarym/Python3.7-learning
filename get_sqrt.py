import math


def get_square_roots(number):
    sqrt_values = []
    if number == 0:
        sqrt_values.append(0)
        return sqrt_values
    elif number < 0:
        return sqrt_values
    elif number > 0:
        sqrt_values.append(-math.sqrt(number))
        sqrt_values.append(math.sqrt(number))
        return sqrt_values

print (get_square_roots(-1))
print(get_square_roots(0))
print(get_square_roots(25))
