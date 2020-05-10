tries = 3
while tries:
    print('>>> ', end='')
    command = input()
    if not command:
        continue
    if command in ('echo', 'cd', 'help'):
        break
    print('Unknown command!')
    tries -= 1
else:
    print('Too many bad tries!')
    command = None