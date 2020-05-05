def get_range(number):
    sequence = []
    if number == 0:
        return sequence
    elif number < 0:
        return sequence
    elif number > 0:
        counter = 0
        while counter < number:
            sequence.append(counter)
            counter += 1
        return sequence

print (get_range(5))