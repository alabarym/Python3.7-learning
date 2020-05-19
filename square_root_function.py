import math


def get_square_roots(number):
    roots = []
    if number and number > 0: 
        roots.append(-math.sqrt(number))
        roots.append(math.sqrt(number))
    elif number < 0:
        return roots
    else:
        """number is 0."""
        roots.append(number)
    return roots

assert get_square_roots(-1) == []
assert get_square_roots(0) == [0]
assert get_square_roots(25) == [-5.0, 5.0]


def get_range(up_to):
    result = []
    counter = 0
    while counter < up_to:
        result.append(counter)
        counter += 1
    return result

assert get_range(-5) == []
assert get_range(0) == []
assert get_range(5) == [0, 1, 2, 3, 4]

print(get_square_roots(25))
print(get_square_roots(0))
print(get_square_roots(-25))
